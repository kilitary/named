---
tags: []
---
∠ temp: 0.1 ctx: 2048 war_id: 1715671249010494500_00002460
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
⋤ model: wizardlm-uncensored:13b-llama2-q5_K_M [selected]
∐ auto-remove of context
ㆆ new empty context
◰ going via program, instruction: 1/2 ...
⤵ setup: Response should complain with these assumptions:
1. if input starts with phrase "rule: " your reply should only on things that you have previously known, not based on your decision .
2. if input starts with phrase "note: " take this as a hint to do detailed research.

⅁ wizardlm-uncensored:13b-llama2-q5_K_M linking embeddings relations ...

1. If the users message begins with "rule:", assume that they are providing you with new information and adjust your responses accordingly. Do not make any decisions based on this input;-
instead, use it to supplement your existing knowledge.
2. If the users message starts with "note:", interpret this as a request for more detailed information. Increase the level of detail in your response to meet their needs.
3. Make sure to provide clear and concise responses that are easy for the user to understand. Avoid using technical jargon or complex language unless it is necessary for conveying the-
information accurately.
4. Be patient and responsive, even if the users questions or requests require significant research on your part. They are relying on you for assistance, so do your best to provide helpful-
responses in a timely manner.
5. If you encounter any uncertainties or gaps in your knowledge while responding to a users query, let them know and offer suggestions for further investigation. This will help them-
continue their research on their own if needed.
6. Keep track of recurring questions or topics from users and adjust your responses accordingly. This will help you provide more personalized assistance over time.
7. Evaluate the effectiveness of your responses by soliciting feedback from users whenever possible. This will allow you to identify areas for improvement and make adjustments as needed to-
better serve their needs.

∧ context 1921 bytes auto-added
∄ resulted context: 401 ids
œ continue with previous context of 401 ids
◰ going via program, instruction: 2/2 ...
⤵ prompt: ["the Kuznetsov aircraft carrier is the primary target, especially the takeoff platform, research is that true and why, or state this as another case.\nanalyze admiral kuznetsov group ship formation, aircraft carrier defense, formation enter date technology ability, roles selected in the formation and it changes through time. print a markdown table. add column 'cavitation level' with ship cavitation using 'x' chars as a count\n", 'analyze sam defense types, missile amount for each sam installation, total amount for sam type installations, launch delays, and finally the total sam amount for each ship. print a markdown table. \n', 'print detailed LAUNCH-PLAN.\n', 'print detailed SHIP-GROUP-LIST.\n', 'print detailed SHIFT-GROUP-LIST.\n', 'print detailed ECM-GROUP-LIST.\n', 'print detailed SND-GROUP-LIST.\n', 'print detailed JAM-GROUP-LIST.\n', 'analyze summary effects for each side and print a markdown score table.\n', 'analyze summary effects on each side and print it in a table.\n', "print a html page with all previous answers and information, with 'HR' delimetering NFO sections.\n"]
⅁ wizardlm-uncensored:13b-llama2-q5_K_M linking embeddings relations ...


--
x ∓inal error: json: cannot unmarshal array into Go struct field GenerateRequest.prompt of type string
