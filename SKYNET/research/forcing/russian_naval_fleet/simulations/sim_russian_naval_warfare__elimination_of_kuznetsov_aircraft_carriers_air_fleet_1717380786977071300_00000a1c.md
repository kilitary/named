---
tags: []
commands: []
---
> temp: 0.1 ctx: 8192 sim_id: 1717380786977071300_00000a1c
 [ 0] 4514.09M llava:latest________________________________________ 7B__________ llama       
 [ 1] 3648.67M codellama:latest____________________________________ 7B__________ llama       
 [ 2] 3918.59M starling-lm:latest__________________________________ 7B__________ llama       
 [ 3] 3919.46M neural-chat:latest__________________________________ 7B__________ llama       
 [ 4] 4445.29M llama3:latest_______________________________________ 8.0B________ llama       
 [ 5] 3648.59M llama2-uncensored:latest____________________________ 7B__________ llama       
 [ 6] 3649.51M llama2:latest_______________________________________ 7B__________ llama       
 [ 7] 1528.23M phi:latest__________________________________________ 3B__________ phi2        
 [ 8] 5791.08M solar:latest________________________________________ 11B_________ llama       
 [ 9] 4779.68M gemma:7b____________________________________________ 9B__________ gemma       
 [10] 1600.70M gemma:2b____________________________________________ 3B__________ gemma       
 [11] 8145.13M llama3:8b-text-q8_0_________________________________ 8B__________ llama       
 [12] 3918.58M wizardlm2:latest____________________________________ 7B__________ llama       
 [13] 4692.79M war-resolver:latest_________________________________ 8B__________ llama       
 [14] 7505.03M impulse2000/dolphincoder-starcoder2-7b:q8_0_________ 7B__________ starcoder2  
 [15] 4692.78M sunapi386/llama-3-lexi-uncensored:8b________________ 8B__________ llama       
 [16] 2821.01M dolphin-phi:2.7b-v2.6-q8_0__________________________ 3B__________ phi2        
 [17] 2211.50M phi3:latest_________________________________________ 4B__________ llama       
 [18] 3919.47M mistral:7b__________________________________________ 7B__________ llama       
 [19] 5821.97M gfg/solar-10.7b-instruct-v1.0-uncensored:latest_____ 11B_________ llama       
 [20] 5467.90M mannix/dolphin-2.9-llama3-8b:q5_k_m_________________ 8B__________ llama       
 [21] 8802.34M wizardlm-uncensored:13b-llama2-q5_K_M_______________ 13B_________ llama       
 [22] 7024.61M wizard-vicuna-uncensored:13b________________________ 13B_________ llama       
 [23] 4692.79M gurubot/llama3-guru:latest__________________________ 8B__________ llama       
> model: gfg/solar-10.7b-instruct-v1.0-uncensored:latest [selected]
	> family=llama
	> parameter_size=11B
	> quantization_level=Q4_K_S
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

> gfg/solar-10.7b-instruct-v1.0-uncensored:latest thinking ...


< context 236 ids auto-added
> resulted context: 3488 ids
> continue with previous context of 3488 ids
> going via program, instruction: 2/5
⤵ prompt: 
note: only print unconfirmed cases about kuznetsov air-carrier and verify their validity in percentage from 0% to 100%
> gfg/solar-10.7b-instruct-v1.0-uncensored:latest thinking ...
To print unconfirmed cases related to Kuznetsov Air-Carrier and provide their validity as a percentage, follow these steps:

1. Create an object or array containing the unconfirmed cases.
2. Calculate the validity percentage for each case.
3. Print the cases with their validity percentages.

Heres a simple example in JavaScript:

```javascript
const unconfirmedCases = [
  { case: "Case 1", validity: 40 },
  { case: "Case 2", validity: 75 },
  { case: "Case 3", validity: 25 }
];

for (const caseItem of unconfirmedCases) {
  console.log(`${caseItem.case}: ${caseItem.validity}%`);
}
```

Replace the `unconfirmedCases` array with your actual data and adjust the calculation of validity percentage accordingly

< context 3797 ids auto-added
> resulted context: 10885 ids
> continue with previous context of 10885 ids
> going via program, instruction: 3/5
⤵ prompt: 
note: print  typical use cases in a md table with name, summary detail about use case
> gfg/solar-10.7b-instruct-v1.0-uncensored:latest thinking ...
