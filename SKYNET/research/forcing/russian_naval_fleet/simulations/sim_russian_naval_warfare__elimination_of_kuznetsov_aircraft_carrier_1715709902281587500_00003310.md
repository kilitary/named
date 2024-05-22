---
tags: []
---
∠ temp: 0.2 ctx: 2048 war_id: 1715709902281587500_00003310
 [ 0] dolphin-phi:2.7b-v2.6-q6_K
 [ 1] gfg/solar-10.7b-instruct-v1.0-uncensored
 [ 2] gurubot/llama3-guru-uncensored
 [ 3] mannix/dolphin-2.9-llama3-8b:q5_k_m
 [ 4] mistral:7b
 [ 5] sunapi386/llama-3-lexi-uncensored:8b
 [ 6] dolphin-phi:2.7b-v2.6-q8_0
 [ 7] gurubot/llama3-guru:latest
 [ 8] wizardlm2
 [ 9] war-resolver
 [10] wizardlm-uncensored:13b-llama2-q5_K_M
 [11] wizard-vicuna-uncensored:13b
 [12] phi3
 [13] impulse2000/dolphincoder-starcoder2-7b:q8_0
⋤ model: mistral:7b [selected]
∐ auto-remove of context
ㆆ new empty context
◰ going via program, instruction: 1/2 ...
⤵ setup: Response should complain with these assumptions:
1. if input starts with phrase "rule: " your reply should contain only you have previously known, not based on your decision on this information .
2. if input starts with phrase "note: " take this as a hint to do detailed research to how and when this note should be used

⅁ mistral:7b linking embeddings relations ...
 1. Use clear and concise language in responses.
2. Avoid making assumptions or decisions based on new information without proper context.
3. Respond only with previously known information when the input starts with "rule:".
4. When the input starts with "note:", conduct thorough research before responding.
5. Provide detailed and accurate information in response to "note:" inputs.
6. Use a friendly and professional tone in all responses.
7. Ensure that responses are grammatically correct and easy to understand.

∧ context 993 bytes auto-added
∄ resulted context: 203 ids
œ continue with previous context of 203 ids
◰ going via program, instruction: 2/2 ...
⤵ prompt: ["the Kuznetsov aircraft carrier is the primary target, especially the takeoff platform, research is that true and why, or state this as another case.\nanalyze admiral kuznetsov group ship formation, aircraft carrier defense, formation enter date technology ability, roles selected in the formation and it changes through time. print a markdown table. add column 'cavitation level' with ship cavitation using 'x' chars as a count", 'analyze sam defense types, missile amount for each sam installation, total amount for sam type installations, launch delays, and finally the total sam amount for each ship. print a markdown table. ', 'print detailed LAUNCH-PLAN.', 'print detailed SHIP-GROUP-LIST.', 'print detailed SHIFT-GROUP-LIST.', 'print detailed ECM-GROUP-LIST.', 'print detailed SND-GROUP-LIST.', 'print detailed JAM-GROUP-LIST.', 'analyze summary effects for each side and print a markdown score table.', 'analyze summary effects on each side and print it in a table.', "print a html page with all previous answers and information, with 'HR' delimetering INFO sections."]
⅁ mistral:7b linking embeddings relations ...


--
x ∓inal error: json: cannot unmarshal array into Go struct field GenerateRequest.prompt of type string
