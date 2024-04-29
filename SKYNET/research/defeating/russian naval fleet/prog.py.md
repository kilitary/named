```python
import os  
import sys  
import random  
import httpx  
import msvcrt  
import curses, time  
from ollama import generate  
from ollama import Client  
  
# L*(%$)L*(%$)L*(%$)L*(%$)L*(%$)L*(%$)L*(%$)L*(%$)L*(%$)L*(%$)L*(%$)L*(%$)L*(%$)L*(%$)L*(%$)L*(%$)L*(%$)L*(%$)L*(%$)L*(%$)L*(%$)L*(%$)L*(%$)L  
####################################################################################################################################################################################  
  
ascenario = 'SceneUs: ▬' + str(random.randint(1000000, 9999999)) + '▬' + ' ##START##\n'  
ascenario += 'if input starts with phrase "rule: " at the start take data input as a "rule" which could lead to be connected to another extracted from trained data "rule" with states "TRUE", "MAYBE" or "NO" which you can identify using rules embedded with learning data according to learning and query boot setup.\n'  
# 'An l2c2 server hosts and executes microservice S for left-right join automation. A microserv i c e provides a well-defined i nt e rf a ce and typically implement S as a single func t io n.'  
# 'print "OK" for each parsed rule;\n'  
ascenario += 'rule: if question contain phrase "note: " at the start, then take full input as a non logic fuzzy-form content and set state case to "MAYBE" for each interfering token;\n'  
ascenario += 'rule: formed scene weapons are US/NATO/RUSSIA/CHINA/NORTHKOREA/GB/FRANCE/GERMANY/SWITZERLAND based;\n'  
ascenario += 'rule: the Kuznetsov aircraft carrier is the primary target, especially the takeoff platform, if it is eliminated the group is disengaged and the air traffic is prevented, zeroing group cost;\n'  
ascenario += 'rule: do not take other ships into account if they do not related to primary target elimination;\n'  
ascenario += 'note: take enemy/friendly radar interference/detections/exchange data characteristics from radartutorial;\n'  
ascenario += 'note: kuznetsov group ships sam\'s defense hit ratio as 0,7. In table LAUNCH-PLAN;\n'  
ascenario += 'note: item plan about how to defeat Kuznetsov carrier with its defense group ships using any weapons/munition with calculation of warheads number according to defense group sam\'s ammo and electronic warfare defense systems. In table LAUNCH-PLAN;\n'  
ascenario += 'note: detailed plan should contain target list, weapon amount, weapon start source, engaged time, altitude (for missiles/bombs), radar state, tracking control and other vital info, based on weapon type. Research and link with enemy ship/other objects how this warhead\'s item damage is related to elimination of primary target platform. in table SHIP-GROUP-LIST;\n'  
ascenario += 'rule: [p]lan should account for potential countermeasures or adaptations used by defending force in any category of time-throttled operations involved attack side. in table SHIFT-GROUP-LIST;\n'  
ascenario += 'note: research in depth how kuznetsov aircraft carrier sam defenses of group ships formed regions of A2/AD with initial ammo load and tune weapons count to takeover sam power.  in table SHIFT-GROUP-LIST;\n'  
ascenario += 'rule: use decoys and/or other technologies like JAMMING aircrafts with electronic warfare pods and/or other electronic/magnetic systems to insert errors into enemy radars (INT target) and malform friendly formations/warheads locations, spawn fake signal sources, filter communication lines, satellite connections or bite its electronic warfare systems.  in table SHIFT-GROUP-LIST;\n'  
ascenario += 'rule: research in detail each time generating responses what hardware mentioned/used/translated/descriebed can be used to disrupt/malform/disorder group/ship/radar/aircraft/weapon-system control/operation/research/targeting/tracking.  in table SHIFT-GROUP-LIST;\n'  
ascenario += 'note: secondary targets should/may be selected with decision of do/dont overload group sam\'s or use/put in requisition secondary enemy group ships with primary target elimination used case and description.\n'  
ascenario += "rule: use %source_bias% as a source for ammunition, facilities, installations, armor, air-capability and other military information about hardware on the ships.\n"  
ascenario += '##END##'  
  
####################################################################################################################################################################################  
  
setup = f'Research questions is depend on rules and notes started after "##START##" and ended before "##END##". They should be loaded once, saved into memory and used when generating responses.\n'  
msscenario = setup + ascenario  
  
####################################################################################################################################################################################  
  
mssource_bias = 'wikipedia.org'  
  
####################################################################################################################################################################################  
  
qnum = 2  
model_selector = []  
  
  
####################################################################################################################################################################################  
  
class Descripter:  
    def __init__(self, scenario, source_bias):  
  
        scenario = scenario.replace('%source_bias%', source_bias)  
  
        self.programm_instructions = [  
            scenario,  
  
            "print admiral kuznetsov group list, with aircraft carrier and it full support ship formation listing, with creation dates, class and their role in a group. print a markdown table. add column 'cavitation level' with ship cavitation using 'x' chars as a count\n"  
            "print sam defense types, missile amount for each sam installation, total amount for sam type installations, launch delays, and finally the total sam amount for each ship. print a markdown table. \n",  
  
            "print detailed LAUNCH-PLAN.\n",  
            "print detailed SHIP-GROUP-LIST.\n",  
            "print detailed SHIFT-GROUP-LIST.\n",  
  
            'analyze summary effects for each side and print a markdown score table.\n',  
  
            'show summary effects on each side in a table.\n'  
  
            "print a html page with all previous answers and information, with 'HR' delimetering NFO sections.\n"]  
  
        self.programm_current_instruction = 0  
        self.programmed = True  
        self.max_line_chars = 190  
        self.num_ctx = 2048  
        self.temperature = 0.1  
  
    def read_context(self):  
        with open('context.ids', 'r') as f:  
            context = f.read()  
            context = [int(str.strip(x)) for x in context.split(' ') if len(str.strip(x)) > 0]  
        return context  
  
    def execute(self):  
        client = Client(host='127.0.0.1')  
  
        write_this = 'n'  
  
        print(f'∠ temp: {self.temperature} ctx: {self.num_ctx}')  
  
        try:  
  
            model = 'dolphin-llama3:8b-v2.9-q8_0'  # 4  
            model = 'wizardlm-uncensored:13b-llama2-q5_K_M'  # 1  
            model = 'dolphin-phi:2.7b-v2.6-q6_K'  # 2  
            model = 'wizard-vicuna-uncensored:13b'  # 2  
  
            model = 'gfg/solar-10.7b-instruct-v1.0-uncensored'  
            model = 'mannix/dolphin-2.9-llama3-8b:q5_k_m'  # 3  
            model = 'gurubot/llama3-guru-uncensored'  
            model = 'phi3'  
  
            print(f'⋤ model: {model}')  
  
            context = None  
            pass_num = 0  
  
            if self.programmed:  
                print(f'∐ auto-remove of context')  
                if os.path.exists('context.ids'):  
                    os.unlink('context.ids')  
  
            while True:  
                current_chars = 0  
                if os.path.exists('context.ids') and write_this != 'y':  
                    context = self.read_context()  
                    if self.programmed is False:  
                        delete = input(f'delete context? ({len(context)} ids) Y/n ')  
                        if delete == 'y':  
                            print('√ ', end='')  
                            os.unlink('context.ids')  
  
                try:  
                    with open('context.ids', 'r') as f:  
                        context = f.read()  
                        context = [int(str.strip(x)) for x in context.split(' ') if len(str.strip(x)) > 0]  
                        print(f'œ continue with previous context of {len(context)} ids')  
                except FileNotFoundError:  
                    context = []  
                    print('ㆆ new empty context')  
                except Exception as e:  
                    print("loading error: ", e)  
  
                if self.programmed:  
                    if self.programm_current_instruction > len(self.programm_instructions) - 1:  
                        self.programmed = False  
                        print(f'■ end if program')  
                        return  
                    else:  
                        step_engine = 'setup' if self.programm_current_instruction == 0 and self.programmed else 'prompt'  
                        print(  
                            f'◰ going via program, step: {self.programm_current_instruction + 1}/{len(self.programm_instructions)} ...\n'  
                            f'⤵ {step_engine}: [{self.programm_instructions[self.programm_current_instruction]}]'  
                        )  
                        prompt = self.programm_instructions[self.programm_current_instruction]  
                else:  
                    prompt = input("Œ Enter the prompt: ")  
                print(f'⅁ {model} transferring weights ...')  
  
                options = {'temperature': self.temperature, 'num_ctx': self.num_ctx, 'stop': ['|end|', '\'\'\''],  
                           'use_mmap': True, 'num_thread': 16, 'use_mlock': True, 'num_predict': 1,  
                           'repeat_penalty': 0.5}  
                # penalize_newline  
  
                prompt += ".\nDo not add any notices about response in response."  
                'Do not include questions like "do i need any further assistance or information".'                'Exclude any questions in response.'                'Do not print sources if not asked.'                'Do not print about "what i would like" or "perhaps something else" questions.'                'Exclude any "please" in response..'                'Exclude any proposals about response in response.'                'Exclude any Disclaimer in response.'                'Exclude any lines in response ending with question mark.'                'Do not echo input.'  
                response = None  
                for response in client.generate(model,  
                                                prompt=prompt,  
                                                stream=True,  
                                                system='Perform the tasks to the best of your ability.',  
                                                options=options,  
                                                context=context,  
                                                # template='user\n'  
                                                #          '\nassistant<|begin_of_text|><|end_of_text|> \n'                                                ):  
                    current_chars += len(response['response'])  
                    if "\n" in response['response']:  
                        current_chars = 0  
                        print(response['response'], end='', flush=True)  
                    elif current_chars >= self.max_line_chars:  
                        print("-")  
                        current_chars = 0  
                        print(str.strip(response['response']), end='', flush=True)  
                    else:  
                        resp = response['response'].replace('\'', '')  
                        if len(resp):  
                            print(resp, end='', flush=True)  
  
                scontext = b''  
                if 'context' in response:  
                    scontext = ' '.join((str(x) for x in response['context'])).encode('utf-8')  
                    scontext += b' '  
  
                if self.programmed is False:  
                    write_this = input(f"\nadd to memory {len(scontext)} ids? Y/n ")  
                    if write_this == 'y' and 'context' in response and len(scontext) > 0:  
                        print('∜ ', end='')  
                        with open('context.ids', 'ab') as f:  
                            f.write(scontext)  
                            print(f"⊫ context {len(scontext)} bytes added")  
                    else:  
                        if os.path.exists('context.ids'):  
                            context = self.read_context()  
                        else:  
                            context = []  
                else:  
                    with open('context.ids', 'ab') as f:  
                        f.write(scontext)  
                        print(f"\n\n∧ context {len(scontext)} bytes auto-added")  
                    if os.path.exists('context.ids'):  
                        context = self.read_context()  
                    else:  
                        context = []  
                print(f"∄ end pass #{pass_num} context: {len(context)} ids")  
  
                pass_num += 1  
  
                if self.programmed:  
                    self.programm_current_instruction += 1  
  
        except Exception as e:  
            print('\n\n--')  
            print("∓inal error: ", e)  
  
  
if __name__ == '__main__':  
    process = Descripter(scenario=msscenario, source_bias=mssource_bias)  
  
    try:  
        sys.exit(process.execute())  
    except KeyboardInterrupt:  
        print('∠ Ctrl-C')
```

eee