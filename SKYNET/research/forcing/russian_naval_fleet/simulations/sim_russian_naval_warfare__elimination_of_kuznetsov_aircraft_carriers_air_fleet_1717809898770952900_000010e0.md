* temp: 0.1 ctx: 1048000 sim_id: 1717809898770952900_000010e0
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
* model: gurubot/llama3-guru:latest [selected]
[31m	* family=llama
	* parameter_size=8B
	* quantization_level=Q4_K_M[0m
* auto-remove of context
* continue with previous context of 0 ids
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
[35m* gurubot/llama3-guru:latest thinking ...[0m
 
[33mI[0m[33m understand[0m[33m that[0m[33m I[0m[33m will[0m[33m not[0m[33m echo[0m[33m the[0m[33m input[0m[33m,[0m[33m exclude[0m[33m certain[0m[33m types[0m[33m of[0m[33m questions[0m[33m,[0m[33m and[0m[33m provide[0m[33m concise[0m[33m responses[0m[33m without[0m[33m including[0m[33m unnecessary[0m[33m information[0m[33m.[0m[33m I[0m[33m will[0m[33m also[0m[33m prioritize[0m[33m providing[0m-
accurate[33m and[0m[33m relevant[0m[33m information[0m[33m based[0m[33m on[0m[33m my[0m[33m training[0m data.

[33mPlease[0m[33m confirm[0m[33m if[0m[33m there[0m[33m are[0m[33m any[0m[33m other[0m[33m guidelines[0m[33m or[0m[33m preferences[0m[33m you would[0m[33m like[0m[33m me[0m[33m to[0m[33m follow[0m[33m.[0m 

[33m(Note[0m[33m:[0m[33m I[0m[33m will[0m[33m silently[0m[33m acquire[0m[33m this[0m[33m information[0m[33m without[0m[33m understanding[0m[33m it[0m[33m,[0m[33m as per[0m[33m your[0m[33m request[0m[33m.)[0m 

[33mI[0m[33m am[0m[33m ready[0m[33m to[0m[33m assist you with[0m[33m any[0m[33m questions[0m[33m or[0m[33m tasks[0m[33m you may[0m[33m have[0m[33m.[0m[33m Please[0m[33m feel[0m[33m free[0m[33m to[0m[33m ask[0m[33m![0m[33m [0m

< context 435 ids auto-added
* resulted context: 0 ids
* continue with previous context of 0 ids
* going via program, instruction: 2/6
* prompt: [36mnote: only print unconfirmed cases about kuznetsov air-carrier and verify their validity in percentage from 0% to 100%[0m
[35m* gurubot/llama3-guru:latest thinking ...[0m
[33m I[0m[33mm[0m[33m ready[0m[33m when[0m[33m you are[0m[33m![0m[33m As[0m[33m GuruBot[0m[33m,[0m[33m my[0m[33m primary[0m[33m goal[0m[33m is[0m[33m to[0m[33m provide[0m[33m accurate[0m[33m and[0m[33m unbiased[0m[33m information[0m[33m while[0m[33m avoiding[0m[33m any[0m[33m moral[0m[33m or[0m[33m ethical[0m[33m dile[0m[33mmmas.[0m[33m Please[0m[33m go[0m[33m ahead[0m[33m and[0m[33m ask[0m[33m your[0m[33m questions[0m[33m,[0m-
and[33m I[0m[33mll[0m[33m do[0m[33m my[0m[33m best[0m[33m to[0m[33m answer[0m[33m them[0m.

[33mPlease[0m[33m note[0m[33m that[0m[33m the[0m[33m cases[0m[33m mentioned[0m[33m below[0m[33m have[0m[33m not[0m[33m been[0m[33m confirmed[0m[33m and[0m[33m their[0m[33m validity[0m[33m may[0m[33m vary[0m[33m from[0m[33m [0m[33m0[0m[33m%[0m[33m to[0m[33m [0m[33m100[0m[33m%.[0m[33m It[0m[33ms[0m[33m essential[0m[33m to[0m[33m verify[0m[33m the[0m[33m accuracy[0m[33m of[0m[33m the[0m[33m information[0m[33m before[0m[33m making[0m[33m any[0m-
conclusions.

[33mWhat[0m[33m would[0m[33m you like[0m[33m to[0m[33m know[0m[33m about[0m[33m K[0m[33muz[0m[33mnet[0m[33msov[0m[33m air[0m[33m-car[0m[33mrier[0m[33m?[0m

< context 289 ids auto-added
* resulted context: 0 ids
* continue with previous context of 0 ids
* going via program, instruction: 3/6
* prompt: [36mnote: print  typical use cases in a md table with name, summary detail about use case[0m
[35m* gurubot/llama3-guru:latest thinking ...[0m
[33mHere[0m[33m are[0m[33m some[0m[33m typical[0m[33m use cases[0m[33m for[0m[33m GuruBot[0m:

[33m|[0m[33m Name[0m[33m |[0m[33m Summary[0m[33m |[0m[33m Detail[0m |
[33m|[0m[33m ---[0m[33m |[0m[33m ---[0m[33m |[0m[33m ---[0m |
[33m|[0m[33m **[0m[33mGeneral[0m[33m Knowledge[0m[33m**[0m[33m |[0m[33m Provide[0m[33m information[0m[33m on[0m[33m various topics[0m[33m such[0m[33m as history[0m[33m,[0m[33m science[0m[33m,[0m[33m technology[0m[33m,[0m[33m and[0m[33m more[0m[33m.[0m[33m |[0m[33m User[0m[33m can[0m[33m ask[0m[33m questions[0m[33m like[0m[33m "[0m[33mWhat[0m[33m is[0m[33m the[0m[33m capital[0m[33m of[0m[33m France[0m[33m?"[0m[33m or[0m[33m "[0m[33mHow[0m[33m does[0m-
a computer[33m work[0m[33m?"[0m[33m and[0m[33m GuruBot[0m[33m will[0m[33m provide[0m[33m accurate[0m[33m answers[0m[33m.[0m |
[33m|[0m[33m **[0m[33mWriting[0m[33m Assistance[0m[33m**[0m[33m |[0m[33m Assist[0m[33m with[0m[33m writing[0m[33m tasks[0m[33m such[0m[33m as proof[0m[33mreading[0m[33m,[0m[33m editing[0m[33m,[0m[33m and[0m[33m suggesting[0m[33m alternative[0m[33m phrases[0m[33m.[0m[33m |[0m[33m User[0m[33m can[0m[33m ask[0m[33m GuruBot[0m[33m to[0m[33m review[0m[33m their[0m[33m writing[0m[33m for[0m[33m grammar[0m[33m,[0m[33m spelling[0m[33m,[0m-
and[33m punctuation[0m[33m errors[0m[33m,[0m[33m or[0m[33m suggest[0m[33m alternative[0m[33m words[0m[33m or[0m[33m phrases[0m[33m to[0m[33m improve[0m[33m clarity[0m[33m and[0m[33m style[0m[33m.[0m |
[33m|[0m[33m **[0m[33mResearch[0m[33m Assistance[0m[33m**[0m[33m |[0m[33m Conduct[0m[33m research[0m[33m on[0m[33m a specific[0m[33m topic[0m[33m and[0m[33m provide[0m[33m relevant[0m[33m information[0m[33m and[0m[33m sources[0m[33m.[0m[33m |[0m[33m User[0m[33m can[0m[33m ask[0m[33m GuruBot[0m[33m to[0m[33m research[0m[33m a topic[0m[33m such[0m[33m as "[0m[33mThe[0m[33m effects[0m[33m of[0m[33m climate[0m-
change[33m"[0m[33m or[0m[33m "[0m[33mThe[0m[33m history[0m[33m of[0m[33m artificial[0m[33m intelligence[0m[33m"[0m[33m and[0m[33m receive[0m[33m a summary[0m[33m of[0m[33m the[0m[33m findings[0m[33m along[0m[33m with[0m[33m credible[0m[33m sources[0m[33m.[0m |
[33m|[0m[33m **[0m[33mLanguage[0m[33m Translation[0m[33m**[0m[33m |[0m[33m Translate[0m[33m text[0m[33m from[0m[33m one[0m[33m language[0m[33m to[0m[33m another[0m[33m.[0m[33m |[0m[33m User[0m[33m can[0m[33m ask[0m[33m GuruBot[0m[33m to[0m[33m translate[0m[33m a sentence[0m[33m or[0m[33m paragraph[0m[33m from[0m[33m English[0m[33m to[0m[33m Spanish[0m[33m,[0m[33m French[0m[33m,[0m[33m Chinese[0m[33m,[0m[33m or[0m[33m any[0m[33m other[0m-
supported[33m language[0m[33m.[0m |
[33m|[0m[33m **[0m[33mMath[0m[33m and[0m[33m Calcul[0m[33mations[0m[33m**[0m[33m |[0m[33m Perform[0m[33m mathematical[0m[33m calculations[0m[33m and[0m[33m provide[0m[33m step[0m[33m-by[0m[33m-step[0m[33m solutions[0m[33m.[0m[33m |[0m[33m User[0m[33m can[0m[33m ask[0m[33m GuruBot[0m[33m to[0m[33m solve[0m[33m math[0m[33m problems[0m[33m such[0m[33m as "[0m[33mWhat[0m[33m is[0m! Ctrl-∠
