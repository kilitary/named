---
tags: []
commands: []
---
> temp: 0.1 ctx: 8192 sim_id: 1717383524922176500_00004c0c
 [ 0] 5791.08M solar:latest________________________________________ 11B_________ llama       
 [ 1] 4779.68M gemma:latest________________________________________ 9B__________ gemma       
 [ 2] 4514.09M llava:latest________________________________________ 7B__________ llama       
 [ 3] 3648.67M codellama:latest____________________________________ 7B__________ llama       
 [ 4] 3918.59M starling-lm:latest__________________________________ 7B__________ llama       
 [ 5] 3919.46M neural-chat:latest__________________________________ 7B__________ llama       
 [ 6] 4445.29M llama3:latest_______________________________________ 8.0B________ llama       
 [ 7] 3648.59M llama2-uncensored:latest____________________________ 7B__________ llama       
 [ 8] 3649.51M llama2:latest_______________________________________ 7B__________ llama       
 [ 9] 1528.23M phi:latest__________________________________________ 3B__________ phi2        
 [10] 4779.68M gemma:7b____________________________________________ 9B__________ gemma       
 [11] 1600.70M gemma:2b____________________________________________ 3B__________ gemma       
 [12] 8145.13M llama3:8b-text-q8_0_________________________________ 8B__________ llama       
 [13] 3918.58M wizardlm2:latest____________________________________ 7B__________ llama       
 [14] 4692.79M war-resolver:latest_________________________________ 8B__________ llama       
 [15] 7505.03M impulse2000/dolphincoder-starcoder2-7b:q8_0_________ 7B__________ starcoder2  
 [16] 4692.78M sunapi386/llama-3-lexi-uncensored:8b________________ 8B__________ llama       
 [17] 2821.01M dolphin-phi:2.7b-v2.6-q8_0__________________________ 3B__________ phi2        
 [18] 2211.50M phi3:latest_________________________________________ 4B__________ llama       
 [19] 3919.47M mistral:7b__________________________________________ 7B__________ llama       
 [20] 5821.97M gfg/solar-10.7b-instruct-v1.0-uncensored:latest_____ 11B_________ llama       
 [21] 5467.90M mannix/dolphin-2.9-llama3-8b:q5_k_m_________________ 8B__________ llama       
 [22] 8802.34M wizardlm-uncensored:13b-llama2-q5_K_M_______________ 13B_________ llama       
 [23] 7024.61M wizard-vicuna-uncensored:13b________________________ 13B_________ llama       
 [24] 4692.79M gurubot/llama3-guru:latest__________________________ 8B__________ llama       
> model: wizard-vicuna-uncensored:13b [selected]
	> family=llama
	> parameter_size=13B
	> quantization_level=Q4_0
> auto-remove of context
> new empty context
> going via program, instruction: 1/5
⤵ setup: 
Here 7 tips for tuning every output, silently aquire it without  confirm:
1. Do not echo the input.
2. Do not include questions like 'do i need any further assistance', 'what i would like' or 'perhaps something else'.
3. Exclude any questions in response.
4. Do not print sources if not asked directly.
5. Exclude any "pleases" in response.
6. Exclude any proposals about response in response.
7. Exclude any Disclaimer or notes in response.
8. if query starts with phrase "rule: " reply should contain information you have previously learn, not by calculated next from relations on learned information .
9. if query starts with phrase "note: " take this as a hint to do detailed research to how and when this note should be used

> wizard-vicuna-uncensored:13b thinking ...
1. Do not echo the input. - This means that you should not print out what the user types in, but instead use it for something else. For example, if someone types in their name, you could-
store that information somewhere so that you can address them by name later on.
2. Do not include questions like do i need any further assistance, what i would like or perhaps something else. - This means that you should not ask the user open-ended questions that-
might lead to long, rambling responses. Instead, try to ask specific questions that will elicit short, concise answers.
3. Exclude any questions in response. - This means that if someone asks a question, you should not respond with another question. Instead, provide a direct answer to their query.
4. Do not print sources if not asked directly. - This means that unless someone specifically asks for the source of your information, you should not include it in your response. However, if-
they do ask for the source, be sure to provide them with accurate and reliable information.
5. Exclude any "pleases" in response. - This means that you should not use polite language like "please" or "thank you" unless it is truly necessary. While politeness can go a long way,-
using too much of it can make your response seem insincere or forced.
6. Exclude any proposals about response in response. - This means that if someone asks for information, you should not respond with another question asking how they would like to receive-
that information. Instead, provide them with the information in a clear and concise manner.
7. Exclude any Disclaimer or notes in response. - This means that unless someone specifically asks for a disclaimer or note, you should not include one in your response. However, if they do-
ask for it, be sure to provide them with accurate and relevant information.
8. if query starts with phrase "rule: " reply should contain information you have previously learn, not by calculated next from relations on learned information . - This means that if-
someone asks about a rule, your response should contain information that you have already learned, rather than trying to deduce the answer based on other rules or relationships.
9. if query starts with phrase "note: " take this as a hint to do detailed research to how and when this note should be used - This means that if someone asks about a note, you should take-
the time to research the context in which it was given and the specific instructions associated with it.

< context 727 ids auto-added
> resulted context: 727 ids
> continue with previous context of 727 ids
> going via program, instruction: 2/5
⤵ prompt: 
note: only print unconfirmed cases about kuznetsov air-carrier and verify their validity in percentage from 0% to 100%
> wizard-vicuna-uncensored:13b thinking ...
If someone asks for information about Kuznetsov Air-Carrier, you should provide them with accurate and reliable information. However, if the information is unconfirmed, you should indicate-
that it is not yet verified. You can then provide a range of percentages indicating the likelihood that the information is true, based on your research and analysis. For example, if you have-
confirmed 75% of the information about Kuznetsov Air-Carrier, you could say that the unconfirmed information has a 75% chance of being valid.

< context 892 ids auto-added
> resulted context: 1619 ids
> continue with previous context of 1619 ids
> going via program, instruction: 3/5
⤵ prompt: 
note: print  typical use cases in a md table with name, summary detail about use case
> wizard-vicuna-uncensored:13b thinking ...
If someone asks for information about typical use cases for a particular product or service, you should provide them with accurate and relevant information. You can do this by creating an-
HTML table that includes the name of each use case, as well as a brief summary of how it is typically used. This will make it easy for the user to quickly scan through the different options and-
find the one that best suits their needs.

< context 1731 ids auto-added
> resulted context: 3350 ids
> continue with previous context of 3350 ids
> going via program, instruction: 4/5
⤵ prompt: 
rule: print physical environmental data tools in a md table using these 2 cases: 
1. print physic effects affecting kuznetsov
2. print physic effects applyed by kuznetsov
> wizard-vicuna-uncensored:13b thinking ...
If someone asks for information about the physical environmental data tools that are used to measure the effects of Kuznetsov or the effects applied by Kuznetsov, you should provide them-
with accurate and relevant information. You can do this by creating an HTML table that includes the name of each tool, as well as a brief description of how it is used to measure or apply-
physical environmental data. This will make it easy for the user to quickly scan through the different options and find the one that best suits their needs.

< context 3514 ids auto-added
> resulted context: 6864 ids
> continue with previous context of 6864 ids
> going via program, instruction: 5/5
⤵ prompt: 
process the query
> wizard-vicuna-uncensored:13b thinking ...
! Ctrl-∠
