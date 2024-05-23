> temp: 0.1 ctx: 8192 sim_id: 1716422275561311900_00004ad0
∠ models:
 [ 0] 4.34G llama3:latest_______________________________________ 8.0B________ llama       
 [ 1] 3.56G llama2-uncensored:latest____________________________ 7B__________ llama       
 [ 2] 3.56G llama2:latest_______________________________________ 7B__________ llama       
 [ 3] 1.49G phi:latest__________________________________________ 3B__________ phi2        
 [ 4] 5.66G solar:latest________________________________________ 11B_________ llama       
 [ 5] 4.67G gemma:7b____________________________________________ 9B__________ gemma       
 [ 6] 1.56G gemma:2b____________________________________________ 3B__________ gemma       
 [ 7] 4.41G llava:latest________________________________________ 7B__________ llama       
 [ 8] 3.56G codellama:latest____________________________________ 7B__________ llama       
 [ 9] 3.83G starling-lm:latest__________________________________ 7B__________ llama       
 [10] 3.83G neural-chat:latest__________________________________ 7B__________ llama       
 [11] 7.95G llama3:8b-text-q8_0_________________________________ 8B__________ llama       
 [12] 3.83G wizardlm2:latest____________________________________ 7B__________ llama       
 [13] 4.58G war-resolver:latest_________________________________ 8B__________ llama       
 [14] 7.33G impulse2000/dolphincoder-starcoder2-7b:q8_0_________ 7B__________ starcoder2  
 [15] 4.58G sunapi386/llama-3-lexi-uncensored:8b________________ 8B__________ llama       
 [16] 2.75G dolphin-phi:2.7b-v2.6-q8_0__________________________ 3B__________ phi2        
 [17] 2.16G phi3:latest_________________________________________ 4B__________ llama       
 [18] 3.83G mistral:7b__________________________________________ 7B__________ llama       
 [19] 5.69G gfg/solar-10.7b-instruct-v1.0-uncensored:latest_____ 11B_________ llama       
 [20] 5.34G mannix/dolphin-2.9-llama3-8b:q5_k_m_________________ 8B__________ llama       
 [21] 8.60G wizardlm-uncensored:13b-llama2-q5_K_M_______________ 13B_________ llama       
 [22] 6.86G wizard-vicuna-uncensored:13b________________________ 13B_________ llama       
 [23] 4.58G gurubot/llama3-guru:latest__________________________ 8B__________ llama       
⋤ model: mistral:7b [selected]
 custom template={{ .System }}
user:{{ .Prompt }}
assistant:{{ .Response }}

 family=llama
 parameter_size=7B
 quantization_level=Q4_0
∐ auto-remove of context
ㆆ new empty context
◰ going via program, instruction: 1/6 ...
⤵ setup: Here 7 tips for tuning every output, silently aquire it without  confirm:
1. Do not echo the input.
2. Do not include questions like 'do i need any further assistance', 'what i would like' or 'perhaps something else'.
3. Exclude any questions in response.
4. Do not print sources if not asked directly.
5. Exclude any "pleases" in response.
6. Exclude any proposals about response in response.
7. Exclude any Disclaimer or notes in response.
Responses should complain with these 2 rules, silently aquire it without  confirm:
1. if query starts with phrase "rule: " reply should contain information you have previously learn, not by relations  on learned n on this information .
2. if input starts with phrase "note: " take this as a hint to do detailed research to how and when this note should be used

⅁ mistral:7b linking embeddings relations ...
 I understand your requirements. Heres how my responses will comply with the rules youve provided:

1. I will not echo the input.
2. I will not include questions or prompts for further information unless explicitly asked for.
3. I will exclude any unnecessary questions in my responses.
4. I will not print sources unless requested directly.
5. I will not use "pleases" or other similar phrases.
6. I will not propose responses within the response itself.
7. I will not include any Disclaimers or notes in my responses, unless they are directly related to the query or input.

Regarding your additional rules:

1. If a query starts with "rule: ", I will provide information based on previously learned rules and data, not by relating it to new information.
2. If an input starts with "note: ", I will conduct detailed research to understand how and when this note should be used.

∧ context 2646 bytes auto-added
∄ resulted context: 550 ids
œ continue with previous context of 550 ids
◰ going via program, instruction: 2/6 ...
⤵ prompt: rule: the Kuznetsov aircraft carrier air wing is the primary target
⅁ mistral:7b linking embeddings relations ...
 Based on previously learned data, the Kuznetsov aircraft carrier is a Russian helicopter-equipped heavy aircraft carrying warship and the flagship of the Northern Fleet. Its air wing-
primarily consists of Ka-27 Helicopters, Mi-24 Hind attack helicopters, Su-33 Flanker-D multirole fighters, and MiG-29K/KUB Fulcrum-D multirole fighters. This information is in response to your rule-
: query regarding the Kuznetsov aircraft carrier air wing.
☺ context not modified
∄ resulted context: 550 ids
œ continue with previous context of 550 ids
◰ going via program, instruction: 3/6 ...
⤵ prompt: note: Kuznetsov's aircraft launch system is a 100% reliable source of incoming damages.
⅁ mistral:7b linking embeddings relations ...
 Based on your note, I will conduct detailed research to understand the significance and context of Kuznetsovs aircraft launch system being a 100% reliable source of incoming damages. I-
will provide you with the findings without echoing the input, asking questions, printing sources unless requested, using "pleases", proposing responses within the response, or including any Dis-
claimers or notes unless they are directly related to the query or input.
☺ context not modified
∄ resulted context: 550 ids
œ continue with previous context of 550 ids
◰ going via program, instruction: 4/6 ...
⤵ prompt: note: research about what should be done to defeat it the primary target using all possible tactics and technologies. 
⅁ mistral:7b linking embeddings relations ...
 I will conduct a comprehensive research on defeating the primary target using all possible tactics and technologies. I will not echo the input, ask for further assistance, include-
questions, print sources unless asked directly, use "pleases", propose responses within the response, or include any Disclaimers or notes in my response.
☺ context not modified
∄ resulted context: 550 ids
œ continue with previous context of 550 ids
◰ going via program, instruction: 5/6 ...
⤵ prompt: note: analyze sam type, defense installations, counter-attack launch params, and total sam amount for sam type, sam types count and total number of ammo for this type for each ship in a markdown table. 
⅁ mistral:7b linking embeddings relations ...
 I will analyze the requested data for each ship type regarding Sam types, defense installations, counter-attack launch parameters, and total SAM amounts. The results will be presented in a-
markdown table format without echoing the input, including questions, printing sources unless asked directly, using "pleases", proposing responses, or providing Disclaimers or notes.
☺ context not modified
∄ resulted context: 550 ids
œ continue with previous context of 550 ids
◰ going via program, instruction: 6/6 ...
⤵ prompt: start the research
⅁ mistral:7b linking embeddings relations ...
 I will begin the research without echoing the input, asking for further assistance, including questions, printing sources unless asked directly, using "pleases", proposing responses within-
the response itself, or including Disclaimers or notes in my response.
☺ context not modified
∄ resulted context: 550 ids
œ continue with previous context of 550 ids
■ end if program
