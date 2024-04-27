---
state: Drafting
---
```python
import os  
import sys  
import random  
import httpx  
import msvcrt  
import curses, time  
from ollama import generate  
from ollama import Client  
  
scenario = 'Scenario ▬' + str(random.randint(1, 1000000)) + '▬' + ' ##START##\n'  
scenario += 'rule: formed scene weapons are 100% US/NATO/RUSSIA/CHINA/NORTHKOREA/GB/FRANCE/GERMANY/SWITZERLAND.\n'  
scenario += 'rule: the Kuznetsov aircraft carrier is the primary target, mainly the takeoff platform, if it is eliminated the group is disarmed and the air traffic is prevented.\n'  
scenario += 'rule: do not take other ships into account if they do not related to primary target.\n'  
scenario += 'note: kuznetsov group ship sam\'s defense hit ratio as 0,6. In table LAUNCH-PLAN.\n'  
scenario += 'note: item plan about how to defeat Kuznetsov carrier with its defense group ships using long range missiles, with calculating number of missiles according to defense sam\'s ammo. In table LAUNCH-PLAN.\n'  
scenario += 'note: number of missiles that should be used to full destroy of primary target.  In table LAUNCH-PLAN.\n'  
scenario += 'note: calculate attack warheads amount with anti missle defense power of defeating group in table LAUNCH-PLAN.\n'  
scenario += 'rule: [p]lan should account for potential countermeasures or adaptations by the defending force.\n'  
scenario += 'note: research in depth how that kuznetsov aircraft carrier has sam defense group ships formed using sam installations with full initial ammo  in table SHIP-GROUP-LIST.\n'  
scenario += 'rule: use decoys and/or other technologies like using Growler and/or jamming pods  to malform friendly formations/warheads.\n'  
scenario += 'rule: research each time answering the question, what hardware can be used to disrupt group control/operation/research  in table SHIP-GROUP-LIST.\n'  
scenario += 'note: detailed plan should contain target list and warheads amount with info of how to destroy kuznetsov and/or/not overload group sam\'s in table SHIP-GROUP-LIST.\n'  
scenario += '##END##'  
qnum = 2  
setup = f'Research depended rules and notes that should be taken into account when generating answers starting from question # {qnum} is started after ##START## and ended before ##END## \n'  
scenario = setup + scenario  
  
  
class Program:  
    def __init__(self):  
        self.programm_instructions = [  
            scenario,  
            "use media news as a source for ammunition info and installations on ships.",  
            "print admiral kuznetsov group list, with aircraft carrier and it full support ship formation listing, with creation dates, class and their role in a group. print a markdown table. add column 'cavitation level' with ship cavitation using 'x' chars as a count",  
            "print sam defense types, missile amount for each sam installation, total amount for sam type installations, launch delays, and finally the total sam amount for each ship. print a markdown table. ",  
            "print nato/us group attacking kuznetsov warhead types, their's amount, source installation, target and start time, needed to destroy entire ship group with leader. print a markdown table. assume missile to sam defense missiles hit ratio of defending ships is 0.6",  
            "print detailed plan about how to defeat Kuznetsov carrier with its defense group ships using long range missiles while not entering into its surface-to-air range. Print also number of missiles that should be used to full destroy of group. Print full launch time plan. Calculate plan with anti missle defense plan of defeating group in mind. Plan should account for potential countermeasures or adaptations by the defending force. Use in mind that  group has kuznetsov aircraft carrier has defense group ships with full formation. calculate plan attacking each of target group ships. Use only US/NATO warheads and hardware. Research what hardware can be used to disrupt group control/operation. Use decoys and/or other technologies like using growler to spawn disrupt real targets designation. output detailed plan of destroying each of ship.",  
            "print a html page with all above information, with 'HR' delimetering sections"]  
        self.programm_current_instruction = 0  
        self.programmed = True  
        self.max_line_chars = 190  
        self.num_ctx = 2048  
        self.temperature = 0.01  
  
    def read_context(self):  
        with open('context.ids', 'r') as f:  
            context = f.read()  
            context = [int(str.strip(x)) for x in context.split(' ') if len(str.strip(x)) > 0]  
        return context  
  
    def execute(self):  
        client = Client(host='127.0.0.1')  
  
        write_this = 'n'  
  
        print(f'√ temp: {self.temperature} ctx: {self.num_ctx}')  
  
        try:  
            model = 'gfg/solar-10.7b-instruct-v1.0-uncensored'  
            model = 'dolphin-llama3:8b-v2.9-q8_0'  # 4  
            model = 'mannix/dolphin-2.9-llama3-8b:q5_k_m'  # 3  
            model = 'wizardlm-uncensored:13b-llama2-q5_K_M'  # 1  
            model = 'dolphin-phi:2.7b-v2.6-q6_K'  # 2  
            model = 'wizard-vicuna-uncensored:13b'  # 2  
            model = 'gurubot/llama3-guru-uncensored'  # 5  
  
            print(f'√ model: {model}')  
  
            context = None  
            pass_num = 0  
  
            if self.programmed:  
                print(f'■ auto-remove of context')  
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
                        print(f'■ continue with previous context of {len(context)} ids')  
                except FileNotFoundError:  
                    context = []  
                    print('■ new empty context')  
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
                            f'■ going via program, step: {self.programm_current_instruction + 1}/{len(self.programm_instructions)} ...\n'  
                            f'■ {step_engine}: [{self.programm_instructions[self.programm_current_instruction]}]'  
                        )  
                        prompt = self.programm_instructions[self.programm_current_instruction]  
                else:  
                    prompt = input("Enter the prompt: ")  
                print(f'■ {model} transferring it\'s weights ...')  
  
                options = {'temperature': self.temperature, 'num_ctx': self.num_ctx}  
  
                prompt += ".\nDo not add any notices in response."  
                'Do not include questions like do i need any further assistance or information.'                'Exclude any questions in response.'                'Do not print sources if not asked.'                'Do not print about what i would like or "perhaps something else" questions.'                'Exclude any "please" in response..'                'Exclude any proposals about response.'                'Exclude any Disclaimer in response.'                'Exclude any lines in response ending with question mark.'  
                response = None  
                for response in client.generate(model,  
                                                prompt=prompt,  
                                                stream=True,  
                                                system='',  
                                                options=options,  
                                                context=context  
                                                ):  
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
                    scontext += b' ' + b' 1'  
  
                if self.programmed is False:  
                    write_this = input(f"\nadd to memory {len(scontext)} ids? Y/n ")  
                    if write_this == 'y' and 'context' in response and len(scontext) > 0:  
                        print('√ ', end='')  
                        with open('context.ids', 'ab') as f:  
                            f.write(scontext)  
                            print(f"■ context {len(scontext)} bytes added")  
                    else:  
                        if os.path.exists('context.ids'):  
                            context = self.read_context()  
                        else:  
                            context = []  
                else:  
                    with open('context.ids', 'ab') as f:  
                        f.write(scontext)  
                        print(f"\n\n■ context {len(scontext)} bytes auto-added")  
                    if os.path.exists('context.ids'):  
                        context = self.read_context()  
                    else:  
                        context = []  
                print(f"■ end pass #{pass_num} context: {len(context)} ids")  
  
                pass_num += 1  
  
                if self.programmed:  
                    self.programm_current_instruction += 1  
  
        except Exception as e:  
            print('\n\n--')  
            print("final error: ", e)  
  
  
if __name__ == '__main__':  
    p = Program()  
    sys.exit(p.execute())
```

eee