> temp: 0.1 ctx: 1048000 sim_id: 1717801939787463900_000045e0
[ 0] 2282.36M 3.8B phi3:latest_________________________________________ phi3         2024-06-08T00:49:56.9922306+03:00
[ 1] 2821.01M 3B   dolphin-phi:2.7b-v2.6-q8_0__________________________ phi2         2024-06-08T00:45:39.0023446+03:00
[ 2] 4692.78M 8B   sunapi386/llama-3-lexi-uncensored:8b________________ llama        2024-06-08T00:44:58.9078769+03:00
[ 3] 7505.03M 7B   impulse2000/dolphincoder-starcoder2-7b:q8_0_________ starcoder2   2024-06-08T00:43:53.3491743+03:00
[ 4] 3918.58M 7B   wizardlm2:latest____________________________________ llama        2024-06-08T00:42:08.3643667+03:00
[ 5] 8145.13M 8.0B llama3:8b-text-q8_0_________________________________ llama        2024-06-07T23:59:29.611722+03:00
[ 6] 4445.29M 8B   llama3-gradient:latest______________________________ llama        2024-06-07T23:47:20.2172392+03:00
[ 7] 3918.59M 7B   starling-lm:latest__________________________________ llama        2024-06-07T23:42:04.580176+03:00
[ 8] 3648.67M 7B   codellama:latest____________________________________ llama        2024-06-07T23:41:13.4032867+03:00
[ 9] 4514.09M 7B   llava:latest________________________________________ llama        2024-06-07T23:40:25.8048108+03:00
[10] 4779.68M 9B   gemma:latest________________________________________ gemma        2024-06-07T23:39:24.2302818+03:00
[11] 3649.51M 7B   llama2:latest_______________________________________ llama        2024-06-07T23:38:21.0519828+03:00
[12] 3648.59M 7B   llama2-uncensored:latest____________________________ llama        2024-06-07T23:37:29.373943+03:00
[13] 5791.08M 11B  solar:latest________________________________________ llama        2024-06-07T23:35:58.4772437+03:00
[14] 4445.29M 8.0B llama3:latest_______________________________________ llama        2024-06-07T23:35:49.8456609+03:00
[15] 3919.46M 7B   neural-chat:latest__________________________________ llama        2024-06-07T23:34:54.1038201+03:00
[16] 1528.23M 3B   phi:latest__________________________________________ phi2         2024-06-07T23:34:12.2576611+03:00
[17] 4779.68M 9B   gemma:7b____________________________________________ gemma        2024-06-07T23:33:53.9304791+03:00
[18] 1600.70M 3B   gemma:2b____________________________________________ gemma        2024-06-07T23:33:04.8268962+03:00
[19] 4692.79M 8B   gurubot/llama3-guru-uncensored:latest_______________ llama        2024-06-07T23:32:46.1730439+03:00
[20] 4692.79M 8B   war-resolver:latest_________________________________ llama        2024-04-30T12:41:04.6532762+03:00
[21] 3919.47M 7B   mistral:7b__________________________________________ llama        2024-04-28T18:58:05.9614997+03:00
[22] 5821.97M 11B  gfg/solar-10.7b-instruct-v1.0-uncensored:latest_____ llama        2024-04-25T01:24:58.6368726+03:00
[23] 5467.90M 8B   mannix/dolphin-2.9-llama3-8b:q5_k_m_________________ llama        2024-04-25T00:39:23.1057159+03:00
[24] 8802.34M 13B  wizardlm-uncensored:13b-llama2-q5_K_M_______________ llama        2024-04-24T23:40:25.8041534+03:00
[25] 7024.61M 13B  wizard-vicuna-uncensored:13b________________________ llama        2024-04-24T21:31:56.7422556+03:00
[26] 4692.79M 8B   gurubot/llama3-guru:latest__________________________ llama        2024-04-24T21:16:46.2144807+03:00
> model: llama3:8b-text-q8_0 [selected]
	> family=llama
	> parameter_size=8.0B
	> quantization_level=Q8_0
> auto-remove of context
> new empty context
> going via program, instruction: 1/6
> setup: 
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

> llama3:8b-text-q8_0 thinking ...
