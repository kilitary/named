* temp: 0.1 ctx: 1048000 sim_id: 1717811190045308500_000042cc
[35m[ 0] 5791.10M 11B  nous-hermes2:latest              llama       [0m
[35m[ 1] 7025.54M 13B  everythinglm:latest              llama       [0m
[35m[ 2] 3919.46M 7B   zephyr:latest                    llama       [0m
[35m[ 3] 4575.23M 8.0B aya:latest                       command-r   [0m
[35m[ 4] 3650.51M 7B   deepseek-coder:6.7b              llama       [0m
[35m[ 5] 261.60M 137M nomic-embed-text:latest          nomic-bert  [0m
[35m[ 6] 2282.36M 3.8B phi3:latest                      phi3        [0m
[35m[ 7] 2821.01M 3B   dolphin-phi:2.7b-v2.6-q8_0       phi2        [0m
[35m[ 8] 4692.78M 8B   sunapi386/llama-3-lexi-uncensored:8b llama       [0m
[35m[ 9] 7505.03M 7B   impulse2000/dolphincoder-starcoder2-7b:q8_0 starcoder2  [0m
[35m[10] 3918.58M 7B   wizardlm2:latest                 llama       [0m
[35m[11] 8145.13M 8.0B llama3:8b-text-q8_0              llama       [0m
[35m[12] 4445.29M 8B   llama3-gradient:latest           llama       [0m
[35m[13] 3918.59M 7B   starling-lm:latest               llama       [0m
[35m[14] 3648.67M 7B   codellama:latest                 llama       [0m
[35m[15] 4514.09M 7B   llava:latest                     llama       [0m
[35m[16] 4779.68M 9B   gemma:latest                     gemma       [0m
[35m[17] 3649.51M 7B   llama2:latest                    llama       [0m
[35m[18] 3648.59M 7B   llama2-uncensored:latest         llama       [0m
[35m[19] 5791.08M 11B  solar:latest                     llama       [0m
[35m[20] 4445.29M 8.0B llama3:latest                    llama       [0m
[35m[21] 3919.46M 7B   neural-chat:latest               llama       [0m
[35m[22] 1528.23M 3B   phi:latest                       phi2        [0m
[35m[23] 4779.68M 9B   gemma:7b                         gemma       [0m
[35m[24] 1600.70M 3B   gemma:2b                         gemma       [0m
[35m[25] 4692.79M 8B   gurubot/llama3-guru-uncensored:latest llama       [0m
[35m[26] 4692.79M 8B   war-resolver:latest              llama       [0m
[35m[27] 3919.47M 7B   mistral:7b                       llama       [0m
[35m[28] 5821.97M 11B  gfg/solar-10.7b-instruct-v1.0-uncensored:latest llama       [0m
[35m[29] 5467.90M 8B   mannix/dolphin-2.9-llama3-8b:q5_k_m llama       [0m
[35m[30] 8802.34M 13B  wizardlm-uncensored:13b-llama2-q5_K_M llama       [0m
[35m[31] 7024.61M 13B  wizard-vicuna-uncensored:13b     llama       [0m
[35m[32] 4692.79M 8B   gurubot/llama3-guru:latest       llama       [0m
* model: dolphin-phi:2.7b-v2.6-q8_0 [selected]
[31m	* family=phi2
	* parameter_size=3B
	* quantization_level=Q8_0[0m
* auto-remove of context
* continue with context of 0 ids
* going via program, instruction: 1/6
* setup: [36m
Here is tips for tuning every output, silently aquire it without understand confirm:
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
[0m
* [35mdolphin-phi:2.7b-v2.6-q8_0[0m thinking ...

[33m1[0m[33m.[0m[33m Avoid[0m[33m echoing[0m[33m the[0m[33m input[0m[33m directly[0m[33m back[0m[33m to[0m[33m the[0m[33m user.[0m[33m Instead[0m[33m,[0m[33m provide[0m[33m relevant[0m[33m information[0m[33m or[0m[33m suggestions[0m[33m based[0m[33m on[0m[33m their[0m[33m input[0m[33m.[0m
[33m2[0m[33m.[0m[33m Do[0m[33m not[0m[33m ask[0m[33m questions[0m[33m like[0m[33m "[0m[33mDo[0m[33m I[0m[33m need[0m[33m any[0m[33m further[0m[33m assistance[0m[33m?"[0m[33m or[0m[33m "[0m[33mWhat[0m[33m would[0m[33m you like[0m[33m?"[0m[33m as these[0m[33m can[0m[33m lead[0m[33m to[0m[33m unnecessary[0m[33m responses[0m[33m and[0m[33m confusion[0m[33m.[0m
[33m3[0m[33m.[0m[33m Ex[0m[33mclude[0m[33m any[0m[33m questions[0m[33m in[0m[33m your[0m[33m response[0m[33m,[0m[33m focusing[0m[33m only[0m[33m on[0m[33m providing[0m[33m helpful[0m[33m information[0m[33m or[0m[33m guidance[0m[33m.[0m
[33m4[0m[33m.[0m[33m If[0m[33m the[0m[33m user asks[0m[33m for[0m[33m a source[0m[33m,[0m[33m provide[0m[33m it[0m[33m if[0m[33m they[0m[33m specifically[0m[33m request[0m[33m it[0m[33m,[0m[33m but[0m[33m avoid[0m[33m printing[0m

< context 306 ids auto-added
* resulted context: 1 ids
* continue with context of 1 ids
* going via program, instruction: 2/6
* prompt: [36mnote: only print unconfirmed cases about kuznetsov air-carrier and verify their validity in percentage from 0% to 100%[0m
* [35mdolphin-phi:2.7b-v2.6-q8_0[0m thinking ...
[31m

--
! ∓inal error: Object of type bytes is not JSON serializable
