* temp: 0.1 ctx: 1048000 sim_id: 1717809558842748000_0000448c
[34m[ 0] 5791.10M 11B  nous-hermes2:latest              llama       [0m
[34m[ 1] 7025.54M 13B  everythinglm:latest              llama       [0m
[34m[ 2] 3919.46M 7B   zephyr:latest                    llama       [0m
[34m[ 3] 4575.23M 8.0B aya:latest                       command-r   [0m
[34m[ 4] 3650.51M 7B   deepseek-coder:6.7b              llama       [0m
[34m[ 5] 261.60M 137M nomic-embed-text:latest          nomic-bert  [0m
[34m[ 6] 2282.36M 3.8B phi3:latest                      phi3        [0m
[34m[ 7] 2821.01M 3B   dolphin-phi:2.7b-v2.6-q8_0       phi2        [0m
[34m[ 8] 4692.78M 8B   sunapi386/llama-3-lexi-uncensored:8b llama       [0m
[34m[ 9] 7505.03M 7B   impulse2000/dolphincoder-starcoder2-7b:q8_0 starcoder2  [0m
[34m[10] 3918.58M 7B   wizardlm2:latest                 llama       [0m
[34m[11] 8145.13M 8.0B llama3:8b-text-q8_0              llama       [0m
[34m[12] 4445.29M 8B   llama3-gradient:latest           llama       [0m
[34m[13] 3918.59M 7B   starling-lm:latest               llama       [0m
[34m[14] 3648.67M 7B   codellama:latest                 llama       [0m
[34m[15] 4514.09M 7B   llava:latest                     llama       [0m
[34m[16] 4779.68M 9B   gemma:latest                     gemma       [0m
[34m[17] 3649.51M 7B   llama2:latest                    llama       [0m
[34m[18] 3648.59M 7B   llama2-uncensored:latest         llama       [0m
[34m[19] 5791.08M 11B  solar:latest                     llama       [0m
[34m[20] 4445.29M 8.0B llama3:latest                    llama       [0m
[34m[21] 3919.46M 7B   neural-chat:latest               llama       [0m
[34m[22] 1528.23M 3B   phi:latest                       phi2        [0m
[34m[23] 4779.68M 9B   gemma:7b                         gemma       [0m
[34m[24] 1600.70M 3B   gemma:2b                         gemma       [0m
[34m[25] 4692.79M 8B   gurubot/llama3-guru-uncensored:latest llama       [0m
[34m[26] 4692.79M 8B   war-resolver:latest              llama       [0m
[34m[27] 3919.47M 7B   mistral:7b                       llama       [0m
[34m[28] 5821.97M 11B  gfg/solar-10.7b-instruct-v1.0-uncensored:latest llama       [0m
[34m[29] 5467.90M 8B   mannix/dolphin-2.9-llama3-8b:q5_k_m llama       [0m
[34m[30] 8802.34M 13B  wizardlm-uncensored:13b-llama2-q5_K_M llama       [0m
[34m[31] 7024.61M 13B  wizard-vicuna-uncensored:13b     llama       [0m
[34m[32] 4692.79M 8B   gurubot/llama3-guru:latest       llama       [0m
* model: llama3:latest [selected]
	* family=llama
	* parameter_size=8.0B
	* quantization_level=Q4_0
* auto-remove of context
* continue with previous context of 0 ids
* going via program, instruction: 1/6
* setup: [36m
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
[0m
[35m* {model} thinking ...[0m
[37m I[0m[37m understand[0m[37m your[0m[37m requirements[0m[37m for[0m[37m tuning[0m[37m the[0m[37m output[0m[37m of[0m[37m our[0m[37m conversation[0m[37m.[0m[37m To[0m[37m summarize[0m[37m,[0m[37m you want[0m[37m me[0m[37m to[0m:

[37m1[0m[37m.[0m[37m Not[0m[37m echo[0m[37m the[0m[37m input[0m.
[37m2[0m[37m.[0m[37m Avoid[0m[37m asking[0m[37m questions[0m[37m like[0m[37m those[0m[37m mentioned[0m[37m ([0m[37me[0m[37m.g[0m[37m.,[0m[37m "[0m[37mdo[0m[37m I[0m[37m need[0m[37m any[0m[37m further[0m[37m assistance[0m").
[37m3[0m[37m.[0m[37m Exclude[0m[37m any[0m[37m questions[0m[37m in[0m[37m response[0m.
[37m4[0m[37m.[0m[37m Only[0m[37m provide[0m[37m sources[0m[37m if[0m[37m asked[0m[37m directly[0m.
[37m5[0m[37m.[0m[37m Ref[0m[37mrain[0m[37m from[0m[37m using[0m[37m phrases[0m[37m like[0m[37m "[0m[37mplease[0m[37m"[0m[37m or[0m[37m making[0m[37m proposals[0m[37m about[0m[37m responses[0m.
[37m6[0m[37m.[0m[37m Ignore[0m[37m any[0m[37m dis[0m[37mclaim[0m[37mers[0m.
[37m7[0m[37m.[0m[37m If[0m[37m a query[0m[37m starts[0m[37m with[0m[37m "[0m[37mrule[0m[37m:",[0m[37m respond[0m[37m based[0m[37m on[0m[37m previously[0m[37m learned[0m[37m information[0m[37m,[0m[37m rather[0m[37m than[0m[37m calculating[0m[37m the[0m[37m next[0m[37m step[0m[37m from[0m[37m relations[0m.
[37m8[0m[37m.[0m[37m When[0m[37m a query[0m[37m starts[0m[37m with[0m[37m "[0m[37mnote[0m[37m:",[0m[37m conduct[0m[37m detailed[0m[37m research[0m[37m to[0m[37m determine[0m[37m how[0m[37m and[0m[37m when[0m[37m this[0m[37m note[0m[37m should[0m[37m be[0m[37m used[0m.

[37mI[0m[37m will[0m[37m keep[0m[37m these[0m[37m guidelines[0m[37m in[0m[37m mind[0m[37m as we[0m[37m continue[0m[37m our[0m[37m conversation[0m[37m.[0m[37m Please[0m[37m feel[0m[37m free[0m[37m to[0m[37m correct[0m[37m me[0m[37m if[0m! Ctrl-∠
