* temp: 0.6 ctx: 16394 sim_id: 1719430080758553368
[blue][ 0] 5791.10M 11B   llama              nous-hermes2:latest             [/blue]
[blue][ 1] 7025.54M 13B   llama              everythinglm:latest             [/blue]
[blue][ 2] 3919.46M 7B    llama              zephyr:latest                   [/blue]
[blue][ 3] 4575.23M 8.0B  command-r          aya:latest                      [/blue]
[blue][ 4] 3650.51M 7B    llama              deepseek-coder:6.7b             [/blue]
[blue][ 5] 2282.36M 3.8B  phi3               phi3:latest                     [/blue]
[blue][ 6] 2821.01M 3B    phi2               dolphin-phi:2.7b-v2.6-q8_0      [/blue]
[blue][ 7] 4692.78M 8B    llama              sunapi386/llama-3-lexi-uncensored:8b[/blue]
[blue][ 8] 7505.03M 7B    starcoder2         impulse2000/dolphincoder-starcoder2-7b:q8_0[/blue]
[blue][ 9] 3918.58M 7B    llama              wizardlm2:latest                [/blue]
[blue][10] 8145.13M 8.0B  llama              llama3:8b-text-q8_0             [/blue]
[blue][11] 4445.29M 8B    llama              llama3-gradient:latest          [/blue]
[blue][12] 3918.59M 7B    llama              starling-lm:latest              [/blue]
[blue][13] 3648.67M 7B    llama              codellama:latest                [/blue]
[blue][14] 4514.09M 7B    llama              llava:latest                    [/blue]
[blue][15] 4779.68M 9B    gemma              gemma:latest                    [/blue]
[blue][16] 3649.51M 7B    llama              llama2:latest                   [/blue]
[blue][17] 3648.59M 7B    llama              llama2-uncensored:latest        [/blue]
[blue][18] 5791.08M 11B   llama              solar:latest                    [/blue]
[blue][19] 4445.29M 8.0B  llama              llama3:latest                   [/blue]
[blue][20] 3919.46M 7B    llama              neural-chat:latest              [/blue]
[blue][21] 1528.23M 3B    phi2               phi:latest                      [/blue]
[blue][22] 4779.68M 9B    gemma              gemma:7b                        [/blue]
[blue][23] 1600.70M 3B    gemma              gemma:2b                        [/blue]
[blue][24] 4692.79M 8B    llama              gurubot/llama3-guru-uncensored:latest[/blue]
[blue][25] 4692.79M 8B    llama              war-resolver:latest             [/blue]
[blue][26] 3919.47M 7B    llama              mistral:7b                      [/blue]
[blue][27] 5821.97M 11B   llama              gfg/solar-10.7b-instruct-v1.0-uncensored:latest[/blue]
[blue][28] 5467.90M 8B    llama              mannix/dolphin-2.9-llama3-8b:q5_k_m[/blue]
[blue][29] 8802.34M 13B   llama              wizardlm-uncensored:13b-llama2-q5_K_M[/blue]
[blue][30] 7024.61M 13B   llama              wizard-vicuna-uncensored:13b    [/blue]
[blue][31] 4692.79M 8B    llama              gurubot/llama3-guru:latest      [/blue]
 model: phi:latest [selected]
[white]* sim finger: 0b1011111011100101001001000110001101011101111000001101100011000[/white]
	-> temperature=0.6
	-> num_ctx=16394
[red]	* family=phi2
	-> parameter_size=3B
	-> quantization_level=Q4_0
	-> families=['phi2']
	-> template=                {{ if .System }}System: {{ .System }}{{ end }}
                User: {{ .Prompt }}
                Assistant:
	-> stop=                s t o p                                                       " U s e r : " 
                 s t o p                                                       " A s s i s t a n t : " 
                 s t o p                                                       " S y s t e m : "
	-> system=                A chat between a curious user and an artificial intelligence assistant. The assistant gives helpful answers to the user's questions.
* auto-remove of context
[31m

--
! inal error: Error 10061 connecting to 127.0.0.1:16379. No connection could be made because the target machine actively refused it.
