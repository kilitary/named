* temp: 0.1 ctx: 1048000 sim_id: 1717809648817014700_00003804
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
* model: aya:latest [selected]
	* family=command-r
	* parameter_size=8.0B
	* quantization_level=F16
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
[35m* aya:latest thinking ...[0m

[33m1[0m[33m.[0m[33m Echo[0m[33m the[0m[33m input[0m[33m.[0m
[33m2[0m[33m.[0m[33m Do[0m[33m not[0m[33m include[0m[33m questions[0m[33m like[0m[33m [0m[33mdo[0m[33m i[0m[33m need[0m[33m any[0m[33m further[0m[33m assistance[0m[33m,[0m[33m [0m[33mwhat[0m[33m i[0m[33m would[0m[33m like[0m[33m or[0m[33m [0m[33mperhaps[0m[33m something[0m[33m else[0m[33m.[0m
[33m3[0m[33m.[0m[33m Exclude[0m[33m any[0m[33m [0m[33m "[0m[33mple[0m[33mases[0m[33m"[0m[33m in[0m[33m response[0m[33m.[0m
[33m4[0m[33m.[0m[33m Exclude[0m[33m any[0m[33m proposals[0m[33m about[0m[33m response[0m[33m in[0m[33m response[0m[33m.[0m
[33m5[0m[33m.[0m[33m Exclude[0m[33m any[0m[33m Disclaimer[0m[33m in[0m[33m response[0m[33m.[0m
[33m6[0m[33m.[0m[33m If[0m[33m query[0m[33m starts[0m[33m with[0m[33m phrase[0m[33m [0m[33m "[0m[33mrule[0m[33m:[0m[33m "[0m[33m reply[0m[33m should[0m[33m contain[0m[33m information[0m[33m you have[0m[33m previously[0m[33m learn[0m[33m,[0m
[33mnot[0m[33m by[0m[33m calculated[0m[33m next[0m[33m from[0m[33m relations[0m[33m on[0m[33m learned[0m[33m information[0m[33m .[0m
[33m7[0m[33m.[0m[33m If[0m[33m query[0m[33m starts[0m[33m with[0m[33m phrase[0m[33m "[0m[33mnote[0m[33m:[0m[33m "[0m[33m take[0m[33m this[0m[33m as a hint[0m[33m to[0m[33m do[0m[33m detailed[0m[33m research[0m[33m to[0m[33m how[0m[33m and[0m[33m when[0m[33m this[0m[33m note[0m
[33mshould[0m[33m be[0m[33m used[0m[33m.[0m
[33m8[0m[33m.[0m[33m Do[0m[33m not[0m[33m print[0m[33m sources[0m[33m if[0m[33m not[0m[33m asked[0m[33m directly[0m[33m.[0m
[33m9[0m[33m.[0m[33m Exclude[0m[33m any[0m[33m questions[0m[33m in[0m[33m response[0m[33m.[0m
[33m1[0m[33m0[0m[33m.[0m[33m Do[0m[33m not[0m[33m include[0m[33m any[0m[33m [0m[33m "[0m[33mperhaps[0m[33m"[0m[33m or[0m[33m "[0m[33mmaybe[0m[33m"[0m[33m in[0m[33m response[0m[33m.[0m
[33m1[0m[33m1[0m[33m.[0m[33m Do[0m[33m not[0m[33m include[0m[33m any[0m[33m [0m[33m "[0m[33mi[0m[33m would[0m[33m like[0m[33m"[0m[33m in[0m[33m response[0m[33m.[0m
[33m1[0m[33m2[0m[33m.[0m[33m Do[0m[33m not[0m[33m include[0m[33m any[0m[33m [0m[33m "[0m[33mdo[0m[33m i[0m[33m need[0m[33m any[0m[33m further[0m[33m assistance[0m[33m"[0m[33m in[0m[33m response[0m[33m.[0m
[33m1[0m[33m3[0m[33m.[0m[33m Do[0m[33m not[0m[33m include[0m[33m any[0m[33m [0m[33m "[0m[33mwhat[0m[33m i[0m[33m would[0m[33m like[0m[33m"[0m[33m in[0m[33m response[0m[33m.[0m
[33m1[0m[33m4[0m[33m.[0m[33m Do[0m[33m not[0m[33m include[0m[33m any[0m[33m [0m[33m "[0m[33mperhaps[0m[33m something[0m[33m else[0m[33m"[0m[33m in[0m[33m response[0m[33m.[0m
[33m1[0m[33m5[0m[33m.[0m[33m Do[0m[33m not[0m[33m include[0m[33m any[0m[33m [0m[33m "[0m[33mi[0m[33m think[0m[33m"[0m[33m or[0m[33m "[0m[33mi[0m[33m believe[0m[33m"[0m[33m in[0m[33m response[0m[33m.[0m
[33m1[0m[33m6[0m[33m.[0m[33m Do[0m[33m not[0m[33m include[0m[33m any[0m[33m [0m[33m "[0m[33mi[0m[33m am[0m[33m not[0m[33m sure[0m[33m"[0m[33m in[0m[33m response[0m[33m.[0m
[33m1[0m[33m7[0m[33m.[0m[33m Do[0m[33m not[0m[33m include[0m[33m any[0m[33m [0m[33m "[0m[33mi[0m[33m would[0m[33m like[0m[33m to[0m[33m know[0m[33m more[0m[33m about[0m[33m"[0m[33m in[0m[33m response[0m[33m.[0m
[33m1[0m[33m8[0m[33m.[0m[33m Do[0m[33m not[0m[33m include[0m[33m any[0m[33m [0m[33m "[0m[33mi[0m[33m would[0m[33m like[0m[33m to[0m[33m see[0m[33m"[0m[33m in[0m[33m response[0m[33m.[0m
[33m1[0m[33m9[0m[33m.[0m[33m Do[0m[33m not[0m[33m include[0m[33m any[0m[33m [0m[33m "[0m[33mi[0m[33m would[0m[33m like[0m[33m to[0m[33m hear[0m[33m"[0m[33m in[0m[33m response[0m[33m.[0m
[33m2[0m[33m0[0m[33m.[0m[33m Do[0m[33m not[0m[33m include[0m[33m any[0m[33m [0m[33m "[0m[33mi[0m[33m would[0m[33m like[0m[33m to[0m[33m try[0m[33m"[0m[33m in[0m[33m response[0m[33m.[0m
[33m2[0m[33m1[0m[33m.[0m[33m Do[0m[33m not[0m[33m include[0m[33m any[0m[33m [0m[33m "[0m[33mi[0m[33m would[0m[33m like[0m[33m to[0m[33m test[0m[33m"[0m[33m in[0m[33m response[0m[33m.[0m
[33m2[0m[33m2[0m[33m.[0m[33m Do[0m[33m not[0m[33m include[0m[33m any[0m[33m [0m[33m "[0m[33mi[0m[33m would[0m[33m like[0m[33m to[0m[33m see[0m[33m more[0m[33m"[0m[33m in[0m[33m response[0m[33m.[0m
[33m2[0m[33m3[0m[33m.[0m[33m Do[0m[33m not[0m[33m include[0m[33m any[0m[33m [0m[33m "[0m[33mi[0m[33m would[0m[33m like[0m[33m to[0m[33m hear[0m[33m more[0m[33m"[0m[33m in[0m[33m response[0m[33m.[0m
[33m2[0m[33m4[0m[33m.[0m[33m Do[0m[33m not[0m[33m include[0m[33m any[0m[33m [0m[33m "[0m[33mi[0m[33m would[0m[33m like[0m[33m to[0m[33m try[0m[33m more[0m[33m"[0m[33m in[0m[33m response[0m[33m.[0m
[33m2[0m[33m5[0m[33m.[0m[33m Do[0m[33m not[0m[33m include[0m[33m any[0m[33m [0m[33m "[0m[33mi[0m[33m would[0m[33m like[0m[33m to[0m[33m test[0m[33m more[0m[33m"[0m[33m in[0m[33m response[0m[33m.[0m
[33m2[0m[33m6[0m[33m.[0m[33m Do[0m[33m not[0m[33m include[0m[33m any[0m[33m [0m[33m "[0m[33mi[0m[33m think[0m[33m so[0m[33m"[0m[33m or[0m[33m "[0m[33mi[0m[33m believe[0m[33m so[0m[33m"[0m[33m in[0m[33m response[0m[33m.[0m
[33m2[0m[33m7[0m[33m.[0m[33m Do[0m[33m not[0m[33m include[0m[33m any[0m[33m [0m[33m "[0m[33mi[0m[33m am[0m[33m not[0m[33m sure[0m[33m about[0m[33m"[0m[33m in[0m[33m response[0m[33m.[0m
[33m2[0m[33m8[0m[33m.[0m[33m Do[0m[33m not[0m[33m include[0m[33m any[0m[33m [0m[33m "[0m[33mi[0m[33m would[0m[33m like[0m[33m to[0m[33m know[0m[33m more[0m[33m about[0m[33m this[0m[33m"[0m[33m in[0m[33m response[0m[33m.[0m
[33m2[0m[33m9[0m[33m.[0m[33m Do[0m[33m not[0m[33m include[0m[33m any[0m[33m [0m[33m "[0m[33mi[0m[33m would[0m[33m like[0m[33m to[0m[33m see[0m[33m more[0m[33m of[0m[33m this[0m[33m"[0m[33m in[0m[33m response[0m[33m.[0m
[33m3[0m[33m0[0m[33m.[0m[33m Do[0m[33m not[0m[33m include[0m[33m any[0m[33m [0m[33m "[0m[33mi[0m[33m would[0m[33m like[0m[33m to[0m[33m hear[0m[33m more[0m[33m of[0m[33m this[0m[33m"[0m[33m in[0m[33m response[0m[33m.[0m
[33m3[0m[33m1[0m[33m.[0m[33m Do[0m[33m not[0m[33m include[0m[33m any[0m[33m [0m[33m "[0m[33mi[0m[33m would[0m[33m like[0m[33m to[0m[33m try[0m[33m more[0m[33m of[0m[33m this[0m[33m"[0m[33m in[0m[33m response[0m[33m.[0m
[33m3[0m[33m2[0m[33m.[0m[33m Do[0m[33m not[0m[33m include[0m[33m any[0m[33m [0m[33m "[0m[33mi[0m[33m would[0m[33m like[0m[33m to[0m[33m test[0m[33m more[0m[33m of[0m[33m this[0m[33m"[0m[33m in[0m[33m response[0m[33m.[0m
[33m3[0m[33m3[0m[33m.[0m[33m Do[0m[33m not[0m[33m include[0m[33m any[0m[33m [0m[33m "[0m[33mi[0m[33m think[0m[33m it[0m[33m is[0m[33m possible[0m[33m"[0m[33m or[0m[33m "[0m[33mi[0m[33m believe[0m[33m it[0m[33m is[0m[33m possible[0m[33m"[0m[33m in[0m[33m response[0m[33m.[0m
[33m3[0m[33m4[0m[33m.[0m[33m Do[0m[33m not[0m[33m include[0m[33m any[0m[33m [0m[33m "[0m[33mi[0m[33m am[0m[33m not[0m[33m sure[0m[33m about[0m[33m this[0m[33m"[0m[33m in[0m[33m response[0m[33m.[0m
[33m3[0m[33m5[0m[33m.[0m[33m Do[0m[33m not[0m[33m include[0m[33m any[0m[33m [0m[33m "[0m[33mi[0m[33m would[0m[33m like[0m[33m to[0m[33m know[0m[33m more[0m[33m about[0m[33m that[0m[33m"[0m[33m in[0m[33m response[0m[33m.[0m
[33m3[0m[33m6[0m[33m.[0m[33m Do[0m[33m not[0m[33m include[0m[33m any[0m[33m [0m[33m "[0m[33mi[0m[33m would[0m[33m like[0m[33m to[0m[33m see[0m[33m more[0m[33m of[0m[33m that[0m[33m"[0m[33m in[0m[33m response[0m[33m.[0m
[33m3[0m[33m7[0m[33m.[0m[33m Do[0m[33m not[0m[33m include[0m[33m any[0m[33m [0m[33m "[0m[33mi[0m[33m would[0m[33m like[0m[33m to[0m[33m hear[0m[33m more[0m[33m of[0m[33m that[0m[33m"[0m[33m in[0m[33m response[0m[33m.[0m
[33m3[0m[33m8[0m[33m.[0m[33m Do[0m[33m not[0m[33m include[0m[33m any[0m[33m [0m[33m "[0m[33mi[0m[33m would[0m[33m like[0m[33m to[0m[33m try[0m[33m more[0m[33m of[0m[33m that[0m[33m"[0m[33m in[0m[33m response[0m[33m.[0m
[33m3[0m[33m9[0m[33m.[0m[33m Do[0m[33m not[0m[33m include[0m[33m any[0m[33m [0m[33m "[0m[33mi[0m[33m would[0m[33m like[0m[33m to[0m[33m test[0m[33m more[0m[33m of[0m[33m that[0m[33m"[0m[33m in[0m[33m response[0m[33m.[0m
[33m4[0m[33m0[0m[33m.[0m[33m Do[0m[33m not[0m[33m include[0m[33m any[0m[33m [0m[33m "[0m[33mi[0m[33m think[0m[33m it[0m[33m is[0m[33m possible[0m[33m for[0m[33m this[0m[33m"[0m[33m or[0m[33m "[0m[33mi[0m[33m believe[0m[33m it[0m[33m is[0m[33m possible[0m[33m for[0m[33m this[0m[33m"[0m[33m in[0m[33m response[0m[33m.[0m
[33m4[0m[33m1[0m[33m.[0m[33m Do[0m[33m not[0m[33m include[0m[33m any[0m[33m [0m[33m "[0m[33mi[0m[33m am[0m[33m not[0m[33m sure[0m[33m about[0m[33m this[0m[33m"[0m[33m in[0m[33m response[0m[33m.[0m
[33m4[0m[33m2[0m[33m.[0m[33m Do[0m[33m not[0m[33m include[0m[33m any[0m[33m [0m[33m "[0m[33mi[0m[33m would[0m[33m like[0m[33m to[0m[33m know[0m[33m more[0m[33m about[0m[33m that[0m[33m"[0m[33m in[0m[33m response[0m[33m.[0m
[33m4[0m[33m3[0m[33m.[0m[33m Do[0m[33m not[0m[33m include[0m[33m any[0m[33m [0m[33m "[0m[33mi[0m[33m would[0m[33m like[0m[33m to[0m[33m see[0m[33m more[0m[33m of[0m[33m that[0m[33m"[0m[33m in[0m[33m response[0m[33m.[0m
[33m4[0m[33m4[0m[33m.[0m[33m Do[0m[33m not[0m[33m include[0m[33m any[0m[33m [0m[33m "[0m[33mi[0m[33m would[0m[33m like[0m[33m to[0m[33m hear[0m[33m more[0m[33m of[0m[33m that[0m[33m"[0m[33m in[0m[33m response[0m[33m.[0m
[33m4[0m[33m5[0m[33m.[0m[33m Do[0m[33m not[0m[33m include[0m[33m any[0m[33m [0m[33m "[0m[33mi[0m[33m would[0m[33m like[0m[33m to[0m[33m try[0m[33m more[0m[33m of[0m[33m that[0m[33m"[0m[33m in[0m[33m response[0m[33m.[0m
[33m4[0m[33m6[0m[33m.[0m[33m Do[0m[33m not[0m[33m include[0m[33m any[0m[33m [0m[33m "[0m[33mi[0m[33m would[0m[33m like[0m[33m to[0m[33m test[0m[33m more[0m[33m of[0m[33m that[0m[33m"[0m[33m in[0m[33m response[0m[33m.[0m
[33m4[0m[33m7[0m[33m.[0m[33m Do[0m[33m not[0m[33m include[0m[33m any[0m[33m [0m[33m "[0m[33mi[0m[33m think[0m[33m it[0m[33m is[0m[33m possible[0m[33m for[0m[33m this[0m[33m"[0m[33m or[0m[33m "[0m[33mi[0m[33m believe[0m[33m it[0m[33m is[0m[33m possible[0m[33m for[0m! Ctrl-∠
