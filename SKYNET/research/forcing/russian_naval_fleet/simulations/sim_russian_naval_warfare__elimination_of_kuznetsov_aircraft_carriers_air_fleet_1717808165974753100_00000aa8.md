* temp: 0.1 ctx: 1048000 sim_id: 1717808165974753100_00000aa8
[ 0] 3919.46M 7B   zephyr:latest                    llama       
[ 1] 4575.23M 8.0B aya:latest                       command-r   
[ 2] 3650.51M 7B   deepseek-coder:6.7b              llama       
[ 3] 261.60M 137M nomic-embed-text:latest          nomic-bert  
[ 4] 2282.36M 3.8B phi3:latest                      phi3        
[ 5] 2821.01M 3B   dolphin-phi:2.7b-v2.6-q8_0       phi2        
[ 6] 4692.78M 8B   sunapi386/llama-3-lexi-uncensored:8b llama       
[ 7] 7505.03M 7B   impulse2000/dolphincoder-starcoder2-7b:q8_0 starcoder2  
[ 8] 3918.58M 7B   wizardlm2:latest                 llama       
[ 9] 8145.13M 8.0B llama3:8b-text-q8_0              llama       
[10] 4445.29M 8B   llama3-gradient:latest           llama       
[11] 3918.59M 7B   starling-lm:latest               llama       
[12] 3648.67M 7B   codellama:latest                 llama       
[13] 4514.09M 7B   llava:latest                     llama       
[14] 4779.68M 9B   gemma:latest                     gemma       
[15] 3649.51M 7B   llama2:latest                    llama       
[16] 3648.59M 7B   llama2-uncensored:latest         llama       
[17] 5791.08M 11B  solar:latest                     llama       
[18] 4445.29M 8.0B llama3:latest                    llama       
[19] 3919.46M 7B   neural-chat:latest               llama       
[20] 1528.23M 3B   phi:latest                       phi2        
[21] 4779.68M 9B   gemma:7b                         gemma       
[22] 1600.70M 3B   gemma:2b                         gemma       
[23] 4692.79M 8B   gurubot/llama3-guru-uncensored:latest llama       
[24] 4692.79M 8B   war-resolver:latest              llama       
[25] 3919.47M 7B   mistral:7b                       llama       
[26] 5821.97M 11B  gfg/solar-10.7b-instruct-v1.0-uncensored:latest llama       
[27] 5467.90M 8B   mannix/dolphin-2.9-llama3-8b:q5_k_m llama       
[28] 8802.34M 13B  wizardlm-uncensored:13b-llama2-q5_K_M llama       
[29] 7024.61M 13B  wizard-vicuna-uncensored:13b     llama       
[30] 4692.79M 8B   gurubot/llama3-guru:latest       llama       
* model: phi3:latest [selected]
	* family=phi3
	* parameter_size=3.8B
	* quantization_level=Q4_K_M
* auto-remove of context
* continue with previous context of 2 ids
* going via program, instruction: 1/6
* setup: 
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

* phi3:latest thinking ...


--
! ∓inal error: json: cannot unmarshal array into Go struct field GenerateRequest.context of type int
