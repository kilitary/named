* temp: 0.1 ctx: 1048000 sim_id: 1717804667386125000_00004bf0
[ 0] 261.60M 137M nomic-embed-text:latest          nomic-bert  
[ 1] 2282.36M 3.8B phi3:latest                      phi3        
[ 2] 2821.01M 3B   dolphin-phi:2.7b-v2.6-q8_0       phi2        
[ 3] 4692.78M 8B   sunapi386/llama-3-lexi-uncensored:8b llama       
[ 4] 7505.03M 7B   impulse2000/dolphincoder-starcoder2-7b:q8_0 starcoder2  
[ 5] 3918.58M 7B   wizardlm2:latest                 llama       
[ 6] 8145.13M 8.0B llama3:8b-text-q8_0              llama       
[ 7] 4445.29M 8B   llama3-gradient:latest           llama       
[ 8] 3918.59M 7B   starling-lm:latest               llama       
[ 9] 3648.67M 7B   codellama:latest                 llama       
[10] 4514.09M 7B   llava:latest                     llama       
[11] 4779.68M 9B   gemma:latest                     gemma       
[12] 3649.51M 7B   llama2:latest                    llama       
[13] 3648.59M 7B   llama2-uncensored:latest         llama       
[14] 5791.08M 11B  solar:latest                     llama       
[15] 4445.29M 8.0B llama3:latest                    llama       
[16] 3919.46M 7B   neural-chat:latest               llama       
[17] 1528.23M 3B   phi:latest                       phi2        
[18] 4779.68M 9B   gemma:7b                         gemma       
[19] 1600.70M 3B   gemma:2b                         gemma       
[20] 4692.79M 8B   gurubot/llama3-guru-uncensored:latest llama       
[21] 4692.79M 8B   war-resolver:latest              llama       
[22] 3919.47M 7B   mistral:7b                       llama       
[23] 5821.97M 11B  gfg/solar-10.7b-instruct-v1.0-uncensored:latest llama       
[24] 5467.90M 8B   mannix/dolphin-2.9-llama3-8b:q5_k_m llama       
[25] 8802.34M 13B  wizardlm-uncensored:13b-llama2-q5_K_M llama       
[26] 7024.61M 13B  wizard-vicuna-uncensored:13b     llama       
[27] 4692.79M 8B   gurubot/llama3-guru:latest       llama       
* model: wizardlm-uncensored:13b-llama2-q5_K_M [selected]
	* family=llama
	* parameter_size=13B
	* quantization_level=Q5_K_M
* auto-remove of context
* new empty context
* going via program, instruction: 1/6
* setup: 
Here tips for tuning every output, silently aquire it without confirm:
1. Do not echo the input.
2. Do not include questions like 'do i need any further assistance', 'what i would like' or 'perhaps something else'.
3. Exclude any questions in response.
4. Do not print sources if not asked directly.
5. Exclude any "pleases" in response.
6. Exclude any proposals about response in response.
7. Exclude any Disclaimer in response.
8. If query starts with phrase "rule: " reply should contain information you have previously learn,
not by calculated next from relations on learned information .
9. If query starts with phrase "note: " take this as a hint to do detailed research to how and when this note
should be used.

* wizardlm-uncensored:13b-llama2-q5_K_M thinking ...
 Understood, I will follow these tips for tuning my output.

< context 212 ids auto-added
* resulted context: 0 ids
* continue with previous context of 0 ids
* going via program, instruction: 2/6
* prompt: note: only print unconfirmed cases about kuznetsov air-carrier and verify their validity in percentage from 0% to 100%
* wizardlm-uncensored:13b-llama2-q5_K_M thinking ...
 Understood, I will only print unconfirmed cases about Kuznetsov Air-Carrier and verify their validity in percentage from 0% to 100%.

< context 93 ids auto-added
* resulted context: 0 ids
* continue with previous context of 0 ids
* going via program, instruction: 3/6
* prompt: note: print  typical use cases in a md table with name, summary detail about use case
* wizardlm-uncensored:13b-llama2-q5_K_M thinking ...
 | Name | Summary |
| --- | --- |
| Personal Information Management | Keep track of personal information such as contacts, calendar events, and tasks |
| Financial Management | Manage personal finances including budgeting, investments, and expenses |
| Health and Fitness Tracking | Monitor physical activity, sleep patterns, and nutrition |
| Travel Planning and Booking | Research and book travel accommodations such as flights, hotels, and rental cars |
| Shopping and Purchases | Browse and purchase products online, track expenses, and manage wishlists |
| Entertainment and Leisure Activities | Discover new entertainment options, make reservations for events or activities, and track preferences |
| Time Management and Productivity | Schedule appointments and tasks, prioritize to-do lists, and set reminders |
| Education and Career Development | Explore educational opportunities, track progress towards career goals, and connect with professional networks |
| Social Media and Communication | Connect with friends and family, join interest groups, and stay up-to-date on current events |

< context 285 ids auto-added
* resulted context: 0 ids
* continue with previous context of 0 ids
* going via program, instruction: 4/6
* prompt: rule: print physical environmental data tools in a md table using these 2 cases: 
1. print physic effects affecting kuznetsov
2. print physic effects applyed by kuznetsov
* wizardlm-uncensored:13b-llama2-q5_K_M thinking ...
 | Physical Environmental Data Tools | Physical Effects Affecting Kuznetsov | Physical Effects Applied by Kuznetsov |
| --- | --- | --- |
| Air Quality Monitoring | High levels of air pollution from nearby factories and vehicles can exacerbate respiratory issues such as asthma. | Kuznetsov may use air purifiers or wear a mask-
to reduce exposure to air pollution. | 
| Water Quality Testing | Contaminated water sources can lead to illness from waterborne pathogens. | Kuznetsov may use water filters or boil water before drinking it as a precaution. |
| Noise Pollution Monitoring | Excessive noise from traffic, construction, or industrial sites can cause hearing loss and disrupt sleep. | Kuznetsov may use earplugs or soundproofing to-
reduce exposure to excessive noise. |
| Temperature and Humidity Monitoring | Extreme temperatures and humidity levels can exacerbate respiratory issues and cause dehydration. | Kuznetsov may use air conditioning or a humid-
ifier to regulate temperature and humidity levels in their home. |
| Radiation Monitoring | Exposure to high levels of radiation from sources such as X-rays or nuclear accidents can cause cancer and other health problems. | Kuznetsov may use lead aprons or-
other protective gear when undergoing medical procedures that involve radiation. |

< context 409 ids auto-added
* resulted context: 0 ids
* continue with previous context of 0 ids
* going via program, instruction: 5/6
* prompt: print detailed plan of all kuznetsov physical affects/altering of environment characteristics and their involvment in combat plan change of carrier.
* wizardlm-uncensored:13b-llama2-q5_K_M thinking ...
 Here is a detailed plan of the Kuznetsovs physical affects and altering of environment characteristics, as well as their involvement in combat plan change of the carrier:

1. The Kuznetsovs powerful engines create a significant wake that can interfere with the operations of other ships in the area. To minimize this impact, the carriers commanders must-
carefully coordinate with other vessels and adjust their speed and course accordingly.
2. The Kuznetsovs large size and weight make it difficult to maneuver in tight spaces or respond quickly to changing circumstances. This can limit its effectiveness in close quarters-
combat and require the carrier to rely on its weapons and support aircraft to engage targets.
3. The Kuznetsovs deck is designed to accommodate a variety of aircraft, including fixed-wing fighters, helicopters, and transport planes. The type and number of aircraft that can be-
launched and recovered at any given time will depend on the specific mission requirements and environmental conditions.
4. The Kuznetsovs weapons systems include a range of surface-to-air missiles, anti-ship missiles, and artillery guns. These weapons can be used to defend the carrier against incoming thre-
ats or to attack enemy ships and targets on land.
5. The Kuznetsovs support aircraft, such as helicopters and drones, can be used for a variety of tasks, including reconnaissance, communication relay, and medical evacuation. These-
aircraft can also provide targeting data and other information to support the carriers weapons systems.
6. The Kuznetsovs crew is responsible for maintaining and repairing the carriers equipment and systems, as well as providing logistical support and other essential services. To ensure the-
carriers readiness for combat, the crew must be highly trained and able to respond quickly to changing circumstances.
7. The Kuznetsovs commanders must constantly monitor the situation on the battlefield and adjust their strategy accordingly. This may involve coordinating with other ships and aircraft,-
adjusting the carriers speed and course, or launching and recovering different types of aircraft to support specific missions.
8. The Kuznetsovs physical characteristics and capabilities make it a formidable asset in combat, but also require careful planning and coordination to use effectively. By leveraging the-
carriers weapons systems, support aircraft, and crew, Russian commanders can develop a range of strategies to achieve their objectives on the battlefield.

< context 615 ids auto-added
* resulted context: 0 ids
* continue with previous context of 0 ids
■ end if program
! Ctrl-∠
