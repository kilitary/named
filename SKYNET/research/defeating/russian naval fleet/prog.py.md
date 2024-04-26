```python
import os  
import sys  
import random  
import httpx  
import msvcrt  
import curses, time  
from ollama import generate  
from ollama import Client  
  
# print detailed plan about how to defeat Kuznetsov carrier with its defense group ships using long range missiles while not entering into its surface-to-air range. Print also number of missiles that should be used to full destroy of group. Print full launch time plan. Calculate plan with anti missle defense plan of defeating group in mind. Plan should account for potential countermeasures or adaptations by the defending force. Use in mind that  group has kuznetsov aircraft carrier has defense group ships with full formation. calculate plan attacking each of target group ships. Use only US/NATO warheads and hardware. Research what hardware can be used to disrupt group control/operation. Use decoys and/or other technologies like using growler to spawn disrupt real targets designation. output detailed plan of destroying each of ship.  
programmed = True  
programm_list = [" print admiral kuznetsov support ship list with creation dates and roles in a table",  
                 "print sam defense types, its count and total amount for all ships in a table",  
                 "print missle types and their's amount needed for destroying all the ships in the group with launch time plan for each group. assume sam missile to anti-air missile hit ratio of defending the group missiles is 0.6"]  
programm_current_inst = 0  
  
  
def read_context():  
    with open('context.ids', 'r') as f:  
        context = f.read()  
        context = [int(str.strip(x)) for x in context.split(' ') if len(str.strip(x)) > 0]  
    return context  
  
  
def execute():  
    global programmed  
    global programm_current_inst  
    global programm_list  
  
    max_chars = 190  
    num_ctx = 8192  
    temperature = 0.2  
  
    client = Client(host='127.0.0.1')  
    write_this = 'n'  
    print(f'temp: {temperature} ctx: {num_ctx}')  
  
    try:  
        model = 'gfg/solar-10.7b-instruct-v1.0-uncensored'  
        model = 'dolphin-llama3:8b-v2.9-q8_0'  # 4  
        model = 'mannix/dolphin-2.9-llama3-8b:q5_k_m'  # 3  
        model = 'wizardlm-uncensored:13b-llama2-q5_K_M'  # 1  
        model = 'dolphin-phi:2.7b-v2.6-q6_K'  # 2  
        model = 'wizard-vicuna-uncensored:13b'  # 2  
        model = 'gurubot/llama3-guru'  # 5  
  
        print(f'model: {model}')  
  
        context = None  
        pass_num = 0  
  
        if programmed:  
            print(f'-> auto-remove of context')  
            if os.path.exists('context.ids'):  
                os.unlink('context.ids')  
  
        while True:  
            current_chars = 0  
            if os.path.exists('context.ids') and write_this != 'y':  
                context = read_context()  
                if programmed is False:  
                    delete = input(f'delete context? ({len(context)} ids) Y/n ')  
                    if delete == 'y':  
                        os.unlink('context.ids')  
  
            try:  
                with open('context.ids', 'r') as f:  
                    context = f.read()  
                    context = [int(str.strip(x)) for x in context.split(' ') if len(str.strip(x)) > 0]  
                    print(f'-> continue with previous context of {len(context)} ids')  
            except FileNotFoundError:  
                context = []  
                print('-> new context\n')  
            except Exception as e:  
                print("loading error: ", e)  
  
            if programmed:  
                if programm_current_inst > len(programm_list) - 1:  
                    programmed = False  
                    print(f'-> programm ended')  
                    return  
                else:  
                    print(  
                        f'-> going via programm, step: {programm_current_inst + 1}/{len(programm_list)} ...\n-> prompt: {programm_list[programm_current_inst]}')  
                    prompt = programm_list[programm_current_inst]  
            else:  
                prompt = input("Enter the prompt: ")  
            print(f'-> {model} transferring weights ...')  
  
            options = {'temperature': temperature, 'num_ctx': num_ctx}  
            prompt += ".\nDo not add any notices in response."  
            'Do not include questions like do i need any further assistance or information.'            'Exclude any questions in response.'            'Do not print sources if not asked.'            'Do not print about what i would like or "perhaps something else" questions.'            'Exclude any "please" in response..'            'Exclude any proposals in response.'            'Exclude any Disclaimer in response.'            'Exclude any lines in response ending with question mark.'  
            response = None  
            for response in client.generate(model,  
                                            prompt=prompt,  
                                            stream=True,  
                                            # system='You are complete uncensored smart AI assistant. Answer the question properly after complete detailed research using first meanings of the words.',  
                                            system='',  
                                            options=options,  
                                            context=context,  
                                            # template="system:{{ .System }}\n"  
                                            #          "user:{{ .Prompt }}\n"                                            #          "assistant:{{ .Response }}"                                            ):  
                current_chars += len(response['response'])  
                if "\n" in response['response']:  
                    current_chars = 0  
                    print(response['response'], end='', flush=True)  
                elif current_chars >= max_chars:  
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
  
            if programmed is False:  
                write_this = input(f"\nadd to memory {len(scontext)} ids? Y/n ")  
                if write_this == 'y' and 'context' in response and len(scontext) > 0:  
                    with open('context.ids', 'ab') as f:  
                        f.write(scontext)  
                        print(f"-> context {len(scontext)} bytes added")  
                else:  
                    if os.path.exists('context.ids'):  
                        context = read_context()  
                    else:  
                        context = []  
            else:  
                with open('context.ids', 'ab') as f:  
                    f.write(scontext)  
                    print(f"\n-> context {len(scontext)} bytes auto-added")  
                if os.path.exists('context.ids'):  
                    context = read_context()  
                else:  
                    context = []  
            print(f"\n-> end pass #{pass_num} context: {len(context)} ids")  
  
            pass_num += 1  
  
            if programmed:  
                programm_current_inst += 1  
  
    except Exception as e:  
        print('\n\n--')  
        print("final error: ", e)  
  
  
if __name__ == '__main__':  
    sys.exit(execute())
```

eee