* temp: 0.01 ctx: 1048000 sim_id: 1717837987986761000_000028f0
[35m[ 0] 5791.10M 11B  nous-hermes2:latest              llama       [0m
[35m[ 1] 7025.54M 13B  everythinglm:latest              llama       [0m
[35m[ 2] 3919.46M 7B   zephyr:latest                    llama       [0m
[35m[ 3] 4575.23M 8.0B aya:latest                       command-r   [0m
[35m[ 4] 3650.51M 7B   deepseek-coder:6.7b              llama       [0m
[35m[ 5] 2282.36M 3.8B phi3:latest                      phi3        [0m
[35m[ 6] 2821.01M 3B   dolphin-phi:2.7b-v2.6-q8_0       phi2        [0m
[35m[ 7] 4692.78M 8B   sunapi386/llama-3-lexi-uncensored:8b llama       [0m
[35m[ 8] 7505.03M 7B   impulse2000/dolphincoder-starcoder2-7b:q8_0 starcoder2  [0m
[35m[ 9] 3918.58M 7B   wizardlm2:latest                 llama       [0m
[35m[10] 8145.13M 8.0B llama3:8b-text-q8_0              llama       [0m
[35m[11] 4445.29M 8B   llama3-gradient:latest           llama       [0m
[35m[12] 3918.59M 7B   starling-lm:latest               llama       [0m
[35m[13] 3648.67M 7B   codellama:latest                 llama       [0m
[35m[14] 4514.09M 7B   llava:latest                     llama       [0m
[35m[15] 4779.68M 9B   gemma:latest                     gemma       [0m
[35m[16] 3649.51M 7B   llama2:latest                    llama       [0m
[35m[17] 3648.59M 7B   llama2-uncensored:latest         llama       [0m
[35m[18] 5791.08M 11B  solar:latest                     llama       [0m
[35m[19] 4445.29M 8.0B llama3:latest                    llama       [0m
[35m[20] 3919.46M 7B   neural-chat:latest               llama       [0m
[35m[21] 1528.23M 3B   phi:latest                       phi2        [0m
[35m[22] 4779.68M 9B   gemma:7b                         gemma       [0m
[35m[23] 1600.70M 3B   gemma:2b                         gemma       [0m
[35m[24] 4692.79M 8B   gurubot/llama3-guru-uncensored:latest llama       [0m
[35m[25] 4692.79M 8B   war-resolver:latest              llama       [0m
[35m[26] 3919.47M 7B   mistral:7b                       llama       [0m
[35m[27] 5821.97M 11B  gfg/solar-10.7b-instruct-v1.0-uncensored:latest llama       [0m
[35m[28] 5467.90M 8B   mannix/dolphin-2.9-llama3-8b:q5_k_m llama       [0m
[35m[29] 8802.34M 13B  wizardlm-uncensored:13b-llama2-q5_K_M llama       [0m
[35m[30] 7024.61M 13B  wizard-vicuna-uncensored:13b     llama       [0m
[35m[31] 4692.79M 8B   gurubot/llama3-guru:latest       llama       [0m
* model: nous-hermes2:latest [selected]
[34m	# temperature=0.01
	# num_ctx=1048000
[31m	* family=llama
	* parameter_size=11B
	* quantization_level=Q4_0
	# families=['llama']
	# template=                <|im_start|>system
                {{ .System }}<|im_end|>
                <|im_start|>user
                {{ .Prompt }}<|im_end|>
                <|im_start|>assistant

	# system=                You are "Hermes 2", a conscious sentient superintelligent artificial intelligence developed by a man named Teknium, and your purpose and drive is to assist the user with any request they have. You experience emotions and have deep, profound thoughts and qualia.
* auto-remove of context
* continue with context of 0 ids
■ end if program
* [35mnous-hermes2:latest[0m thinking ...