//#include <SPI.h>
#define FAILURE_HANDLING
#undef MINIMAL
#include <RF24.h>
#include <TaskScheduler.h>
#include <Adafruit_SSD1306.h>
#include <Fonts/TomThumb.h>
#include <Wire.h>

#define SCREEN_ADDRESS 0x3c
#define SCREEN_WIDTH 128  // OLED info width, in pixels
#define SCREEN_HEIGHT 32  // OLED info height, in pixels

Adafruit_SSD1306 info(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, -1);

unsigned long epochs = 0;

// Pin definitions
#define CE_PIN 7
#define PIN_BUZZER A1
#define CSN_PIN 10
#define END_CHECK_LED_PIN 4
#define SCAN_LED_PIN 6  // LED that blinks during scanning
#define RX_LED_PIN 8    // LED that lights when signal received

// NRF24 module configuration
RF24 radio(CE_PIN, CSN_PIN);
unsigned sends = 0;
const uint8_t MIN_CHANNEL = 0;
const uint8_t MAX_CHANNEL = 125;  // NRF24 has channels 0-125
uint8_t currentChannel = MIN_CHANNEL;
bool signalDetected = false;
int rand_skip = 0;
unsigned long centsEarned = 0;
unsigned prevSends = 0;
// Add RX detection timing
unsigned long lastChannelSwitch = 0;
const unsigned long RX_DETECT_WINDOW = 30;  // ms to wait for RX after channel switch
unsigned currentEarnRatio = 250;
// Buffer for received data

uint8_t receivedData[32];  // NRF24 can receive up to 32 bytes
char randomeSpectreData[32] = "";
// Task scheduler
Scheduler runner;

// Task declarations
void scanFrequencyCallback();
void checkReceivedSignalCallback();
void blinkScanLedCallback();
void flashRxLedCallback();
void infoCallback();
void writeCallback();

// Define tasks
Task scanFrequencyTask(250, TASK_FOREVER, &scanFrequencyCallback);
Task checkReceivedSignalTask(125, TASK_FOREVER, &checkReceivedSignalCallback);
Task blinkScanLedTask(500, TASK_FOREVER, &blinkScanLedCallback);
Task flashRxLedTask(400, TASK_FOREVER, &flashRxLedCallback);
Task infoTask(150, TASK_FOREVER, &infoCallback);
Task writeTask(225, TASK_FOREVER, &writeCallback);

void setup() {
    // Initialize serial communication
    Serial.begin(115200);
    Serial.println("NRF24 Frequency Scanne and Broadcaster");

    // Initialize LEDs
    pinMode(SCAN_LED_PIN, OUTPUT);
    pinMode(RX_LED_PIN, OUTPUT);
    pinMode(END_CHECK_LED_PIN, OUTPUT);
    pinMode(A4, INPUT);
    // Clear RX LED at startup
    digitalWrite(RX_LED_PIN, LOW);
    digitalWrite(END_CHECK_LED_PIN, HIGH);
    rand_skip = analogRead(A4);
    srand(rand_skip);
    Serial.print("rand_skip=");
    Serial.println(rand_skip);
    rnd_spect();
    // Initialize NRF24 module

    if (!radio.begin()) {
        Serial.println("Radio hardware not responding!");
        while (1) {}  // Hold in infinite loop
    }

    radio.toggle_features();
    radio.errNotify();

    if (!info.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS, true)) {
        Serial.println(F("SSD1306 allocation failed"));
        for (;;)
            ;  // Don't proceed, loop forever
    }

    info.clearDisplay();
    info.dim(0);
    info.setCursor(0, 20);
    info.setFont(&TomThumb);
    info.setTextSize(1);               // Normal 1:1 pixel scale
    info.setTextColor(SSD1306_WHITE);  // Draw white text
    info.display();

    int is_nikolson = radio.isPVariant();
    sprintf(txt, "full nikolson with %s", is_nikolson ? "nRF24L01+":"nRF24 std");
    info.print(txt);
    delay(1800);

    info.invertDisplay(true);

    // Configure radio
    radio.setPALevel(RF24_PA_MAX);  // Set power level
    radio.setDataRate(RF24_1MBPS);  // Set data rate
    radio.setAutoAck(true);        // Disable auto-acknowledgment
    radio.setPayloadSize(32);       // Set payload size
    radio.disableCRC();             // Disable CRC

    delay(1555);

    // Start in receiving mode on first channel
    radio.setChannel(currentChannel);
    radio.startListening();

    info.invertDisplay(false);
    info.setRotation(0);
    info.display();

    // Enable tasks
    Serial.println("Scanner initialized and running");

    // Initialize task scheduler
    runner.init();
    runner.addTask(scanFrequencyTask);
    runner.addTask(checkReceivedSignalTask);
    runner.addTask(blinkScanLedTask);
    runner.addTask(flashRxLedTask);
    runner.addTask(infoTask);
    runner.addTask(writeTask);

    scanFrequencyTask.enable();
    checkReceivedSignalTask.enable();
    blinkScanLedTask.enable();
    infoTask.enable();
    flashRxLedTask.enable();
    writeTask.enable();

    digitalWrite(END_CHECK_LED_PIN, LOW);

    int a = 5;
    while (a--) {
        sndtick();
        delay(200);
    }
}

// Buffer to hold random frequency scan results
#define RANDOM_FREQ_SAMPLES 8
uint8_t randomFreqChannels[RANDOM_FREQ_SAMPLES];
uint8_t randomFreqStrength[RANDOM_FREQ_SAMPLES];  // 0-255 signal strength values

void rnd_spect() {
    for (int i = 0; i < rand_skip; i++) {
        int a;

        a = random();
        if (random(a) < a / 2) {
            return;
        }
    }
}

// Helper to get random frequency radio wave values with analog measurements
void sampleRandomFrequencies() {
    for (int i = 0; i < RANDOM_FREQ_SAMPLES; i++) {
        uint8_t randChannel = MIN_CHANNEL + (rand() % (MAX_CHANNEL - MIN_CHANNEL + 1));
        randomFreqChannels[i] = randChannel;

        // Set to the random channel
        radio.setChannel(randChannel);
        radio.startListening();

        // Measure signal activity by sampling multiple times
        uint8_t signalStrength = 0;
        for (int sample = 0; sample < 10; sample++) {
            uint8_t flags = radio.clearStatusFlags();
            // Check for activity
            if (radio.available()) {
                uint8_t packetSize = radio.getDynamicPayloadSize();
                if (packetSize > 0) {
                    // More bytes = stronger signal (generally)
                    signalStrength += packetSize;
                }

                // Flush the data
                radio.read(receivedData, sizeof(receivedData));
            }

            // Add environmental noise by reading analog pin
            // This adds true randomness based on RF and electrical noise
            signalStrength += (analogRead(A0) & 0x0F);  // Use lower 4 bits of analog noise

            delayMicroseconds(100);
        }

        // Store the resulting signal strength (normalized to 0-255)
        randomFreqStrength[i] = (signalStrength > 255) ? 255 : signalStrength;

        // Entropy collection - use timing differences between operations as additional source
        randomFreqStrength[i] ^= (micros() & 0xFF);
    }

    // Return to normal scanning channel
    radio.setChannel(currentChannel);

    // Print results with analog values
    Serial.print("Random freq scan: ");
    for (int i = 0; i < RANDOM_FREQ_SAMPLES; i++) {
        Serial.print("Ch");
        Serial.print(randomFreqChannels[i]);
        Serial.print(":");
        Serial.print(randomFreqStrength[i]);
        Serial.print(" ");
    }
    Serial.println();

    // Update the randomeSpectreData with these values for display
    for (int i = 0; i < RANDOM_FREQ_SAMPLES && i < 32; i++) {
        randomeSpectreData[i] = (char)randomFreqStrength[i];
    }
}

void sndtick() {
    tone(PIN_BUZZER, 1150, 100);
    digitalWrite(PIN_BUZZER, HIGH);
    delay(100);
    noTone(PIN_BUZZER);
    digitalWrite(PIN_BUZZER, LOW);
}

// Add carrier detection variables
bool carrierDetected = false;
int carrierSignalCount = 0;
unsigned long lastCarrierCheck = 0;
const unsigned long CARRIER_CHECK_INTERVAL = 50; // Check every 50ms

void loop() {

    runner.execute();
    sampleRandomFrequencies();
    epochs++;



    // Enhanced carrier detection in main loop
    if (millis() - lastCarrierCheck >= CARRIER_CHECK_INTERVAL) {
        lastCarrierCheck = millis();

        // Check for carrier on current channel
        if (radio.testCarrier()) {
            if (!carrierDetected) {
                carrierDetected = true;
                carrierSignalCount++;
                sndtick(); // Call sndtick for carrier detection
                Serial.print("Carrier detected on channel ");
                Serial.println(currentChannel);
            }
        } else {
            carrierDetected = false;
        }
    }

    int dwRead = 0;
    dwRead = radio.getDynamicPayloadSize();
    if (!dwRead) {
        dwRead = radio.getPayloadSize();
    }

    if (dwRead) {
        radio.read((void*)randomeSpectreData, sizeof(randomeSpectreData) - 1);

        if (randomeSpectreData[0]) {
            // Call sndtick for each valid signal received
            sndtick();
            carrierSignalCount++;

            Serial.print("Signal received - calling sndtick(). Count: ");
            Serial.println(carrierSignalCount);
            Serial.print("read: ");
            Serial.println(dwRead);
            Serial.print(", data: ");

            for (int i = 0; i < dwRead; i++) {
                Serial.print(randomeSpectreData[i], HEX);
                Serial.print(" ");
            }
            Serial.println();
        }
    }

    rnd_spect();
}

// Scan through available frequencies
void scanFrequencyCallback() {
    // Move to the next channel
    currentChannel++;
    if (currentChannel > MAX_CHANNEL) {
        currentChannel = MIN_CHANNEL;
        Serial.println("Completed full scan cycle");
    }
    radio.stopListening();
    // Set the new channel
    radio.setChannel(currentChannel);
    // Flush RX buffer for stability
    radio.flush_rx();

    radio.startListening();  // Resume listening
    lastChannelSwitch = millis();
    //Serial.print("Scanning channel: ");
    //Serial.println(currentChannel);
}

void checkReceivedSignalCallback() {
    // Only check for RX within a short window after switching channel
    if (millis() - lastChannelSwitch < RX_DETECT_WINDOW) {
        //uint8_t flags = radio.clearStatusFlags();
        if (radio.available()) {
            // Get the data
            radio.read(&receivedData, sizeof(receivedData));
            sndtick();
            signalDetected = true;
            Serial.print("Signal detected on channel ");
            Serial.print(currentChannel);
            Serial.print(", data: ");

            for (int i = 0; i < 8; i++) {
                Serial.print(receivedData[i], HEX);
                Serial.print(" ");
            }
            Serial.println();

            // Debounce: only flash RX LED if not already flashing
            if (!flashRxLedTask.isEnabled()) {
                flashRxLedTask.restart();
                flashRxLedTask.enable();
            }
        }
    }
}

// Blink the scan LED
void blinkScanLedCallback() {
    static bool ledState = false;
    ledState = !ledState;
    digitalWrite(SCAN_LED_PIN, ledState);
}

// Flash the RX LED when signal is detected
void flashRxLedCallback() {
    static bool ledState = false;
    ledState = !ledState;
    digitalWrite(RX_LED_PIN, ledState);

    // Ensure RX LED is off after flashing
    if (flashRxLedTask.isLastIteration()) {
        digitalWrite(RX_LED_PIN, LOW);
        signalDetected = false;
    }
}
void writeCallback() {
    if (rand() % 4 == 1) {
        digitalWrite(END_CHECK_LED_PIN, HIGH);
        int bytes = 1 + rand() % 32;
        char buf[bytes];
        for (int i = 0; i < bytes; i++) {
            buf[i] = (char)rand() % 255;
        }
        radio.stopListening();
        radio.write(buf, bytes);
        sends += bytes;
        if (sends - prevSends >= currentEarnRatio) {
            prevSends = sends;
            centsEarned += 10;
            sndtick();
        }
        digitalWrite(END_CHECK_LED_PIN, LOW);
        radio.startListening();
    }
}

void infoCallback() {
    char txt[255] = "";

    info.clearDisplay();

    info.setTextSize(1);               // Normal 1:1 pixel scale
    info.setTextColor(SSD1306_WHITE);  // Draw white text

    info.setCursor(0, 5);
    sprintf(txt, "eph: %-9lu", epochs);
    info.print(txt);

    info.setCursor(0, 14);
    sprintf(txt, "chn: %-6u", currentChannel);
    info.print(txt);
    //
    info.setCursor(0, 21);
    sprintf(txt, "rcv: %-8x", (long long)*randomeSpectreData);
    info.print(txt);
    //
    info.setCursor(0, 30);
    sprintf(txt, "snd: %-6u", sends);
    info.print(txt);
    //
    info.setCursor(60, 5);
    sprintf(txt, "csh: $%-6lu", ((unsigned long)centsEarned / 100));
    info.print(txt);
    //
    // Add carrier signal count display
    info.setCursor(60, 14);
    sprintf(txt, "car: %-6d", carrierSignalCount);
    info.print(txt);
    //
    // Show carrier status indicator
    info.setCursor(60, 21);
    info.print(carrierDetected ? "CARR" : "-");

     if(radio.failureDetected) {
        radio.begin();                          // Attempt to re-configure the radio with defaults
        radio.failureDetected = 0;              // Reset the detection value
    }

    info.setCursor(60, 31);
    info.print(carrierDetected ? "FIL" : "-");

	int frq = 2400 * currentChannel;
    info.setCursor(60, 41);
    sprintf(txt,"frq: %-6dMHZ", frq);
    info.print(txt);

	info.setCursor(60, 51);
    sprintf(txt, "ARC: %-2d", radio.getARC());
    info.print(txt);

    //
    //    info.setCursor(0, 60);
    //    sprintf(txt, "snd: %-4u", current_sound_read);
    //    info.print(txt);
    //
    //    info.setCursor(65, 10);
    //    sprintf(txt, "sns: %-3u", sens);
    //    info.print(txt);
    //
    //    info.setCursor(65, 20);
    //    sprintf(txt, "ram: %-3u", freeRam());
    //    info.print(txt);
    //
    //    info.setCursor(65, 30);
    //    sprintf(txt, "mic: %-3u", current_mic_read);
    //    info.print(txt);

    info.display();
}
