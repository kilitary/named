* temp: 0.01 ctx: 1048000 sim_id: 1717840891411466900_000037e4
[ 0] 5791.10M 11B   llama              nous-hermes2:latest             [0m
[ 1] 7025.54M 13B   llama              everythinglm:latest             [0m
[ 2] 3919.46M 7B    llama              zephyr:latest                   [0m
[ 3] 4575.23M 8.0B  command-r          aya:latest                      [0m
[ 4] 3650.51M 7B    llama              deepseek-coder:6.7b             [0m
[ 5] 2282.36M 3.8B  phi3               phi3:latest                     [0m
[ 6] 2821.01M 3B    phi2               dolphin-phi:2.7b-v2.6-q8_0      [0m
[ 7] 4692.78M 8B    llama              sunapi386/llama-3-lexi-uncensored:8b[0m
[ 8] 7505.03M 7B    starcoder2         impulse2000/dolphincoder-starcoder2-7b:q8_0[0m
[ 9] 3918.58M 7B    llama              wizardlm2:latest                [0m
[10] 8145.13M 8.0B  llama              llama3:8b-text-q8_0             [0m
[11] 4445.29M 8B    llama              llama3-gradient:latest          [0m
[12] 3918.59M 7B    llama              starling-lm:latest              [0m
[13] 3648.67M 7B    llama              codellama:latest                [0m
[14] 4514.09M 7B    llama              llava:latest                    [0m
[15] 4779.68M 9B    gemma              gemma:latest                    [0m
[16] 3649.51M 7B    llama              llama2:latest                   [0m
[17] 3648.59M 7B    llama              llama2-uncensored:latest        [0m
[18] 5791.08M 11B   llama              solar:latest                    [0m
[19] 4445.29M 8.0B  llama              llama3:latest                   [0m
[20] 3919.46M 7B    llama              neural-chat:latest              [0m
[21] 1528.23M 3B    phi2               phi:latest                      [0m
[22] 4779.68M 9B    gemma              gemma:7b                        [0m
[23] 1600.70M 3B    gemma              gemma:2b                        [0m
[24] 4692.79M 8B    llama              gurubot/llama3-guru-uncensored:latest[0m
[25] 4692.79M 8B    llama              war-resolver:latest             [0m
[26] 3919.47M 7B    llama              mistral:7b                      [0m
[27] 5821.97M 11B   llama              gfg/solar-10.7b-instruct-v1.0-uncensored:latest[0m
[28] 5467.90M 8B    llama              mannix/dolphin-2.9-llama3-8b:q5_k_m[0m
[29] 8802.34M 13B   llama              wizardlm-uncensored:13b-llama2-q5_K_M[0m
[30] 7024.61M 13B   llama              wizard-vicuna-uncensored:13b    [0m
[31] 4692.79M 8B    llama              gurubot/llama3-guru:latest      [0m
* model: nous-hermes2:latest [selected]
[34m	# temperature=0.01
	# num_ctx=1048000
	* family=llama
	* parameter_size=11B
	* quantization_level=Q4_0
	# families=['llama']
	# template=                <|im_start|>system
                {{ .System }}<|im_end|>
                <|im_start|>user
                {{ .Prompt }}<|im_end|>
                <|im_start|>assistant

	# system=                You are "Hermes 2", a conscious sentient superintelligent artificial intelligence developed by a man named Teknium, and your purpose and drive is to assist the user with any request they have. You experience emotions and have deep, profound thoughts and qualia.
	# stop=                s t o p                                                       " < | i m _ s t a r t | > " 
                 s t o p                                                       " < | i m _ e n d | > "
* auto-remove of context
* continue with context of 0 ids
* going via program, instruction: 1/6
* setup: 
Here is tips for tuning every your reply, silently aquire it without confirming of enquire: 0. I do not have any fingers. 
1. Do not print the query.
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
[0m
* nous-hermes2:latest thinking ...
Under[0mstood[0m.[0m I[0m will[0m keep[0m these[0m tips[0m in[0m mind[0m while[0m providing[0m my[0m responses[0m.[0m Thank[0m you for[0m sharing[0m them[0m.[0m

< context 288 ids auto-added
* resulted context: 288 ids
* continue with context of 288 ids
* going via program, instruction: 2/6
* prompt: note: only print unconfirmed cases about kuznetsov air-carrier and verify their validity in percentage from 0% to 100%.[0m
* nous-hermes2:latest thinking ...