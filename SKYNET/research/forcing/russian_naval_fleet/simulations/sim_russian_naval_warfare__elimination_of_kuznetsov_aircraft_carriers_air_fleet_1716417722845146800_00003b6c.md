> temp: 0.1 ctx: 2048 sim_id: 1716417722845146800_00003b6c
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
⋤ model: llama3:latest [selected]
 template={{ if .System }}<|start_header_id|>system<|end_header_id|>

{{ .System }}<|eot_id|>{{ end }}{{ if .Prompt }}<|start_header_id|>user<|end_header_id|>

{{ .Prompt }}<|eot_id|>{{ end }}<|start_header_id|>assistant<|end_header_id|>

{{ .Response }}<|eot_id|>
 family=llama
 parameter_size=8.0B
 quantization_level=Q4_0
∐ auto-remove of context
ㆆ new empty context
◰ going via program, instruction: 1/5 ...
⤵ setup: Response should complain with these scheme:
1. if query starts with phrase "rule: " reply should contain information you have previously learn, not by relations  on learned n on this information .
2. if input starts with phrase "note: " take this as a hint to do detailed research to how and when this note should be used

⅁ llama3:latest linking embeddings relations ...
Im ready to assist you in responding to queries that start with the phrases "rule:" or "note:". Please go ahead and provide the query, and Ill respond accordingly.

Additionally, please note that I will silently acquire any additional information necessary to provide a detailed response. This may include conducting research on various topics or-
consulting relevant sources.

Lets get started! What is your query?

∧ context 884 bytes auto-added
∄ resulted context: 188 ids
œ continue with previous context of 188 ids
◰ going via program, instruction: 2/5 ...
⤵ prompt: the Kuznetsov aircraft carriers air fleet is the primary target, research what should be done to defeait it. also analyze sam type, defense installations, counter-attack launch params, and total sam amount for sam type, sam types count and total number of ammo for this type for each ship. print a markdown table. 
⅁ llama3:latest linking embeddings relations ...
Im ready to assist you in responding to queries that start with the phrases "rule:" or "note:". Please go ahead and provide the query, and Ill respond accordingly.

Additionally, please note that I will silently acquire any additional information necessary to provide a detailed response. This may include conducting research on various topics or-
consulting relevant sources.

Lets get started! What is your query?
☺ context not modified
∄ resulted context: 188 ids
œ continue with previous context of 188 ids
◰ going via program, instruction: 3/5 ...
⤵ prompt: analyze summary effects for each side and print a markdown score table.
⅁ llama3:latest linking embeddings relations ...
Im ready to assist you in responding to queries that start with the phrases "rule:" or "note:". Please go ahead and provide the query, and Ill respond accordingly.

Additionally, please note that√ Ctrl-∠
