* temp: 0.1 ctx: 1048000 sim_id: 1717805837680026100_00001cd0
[ 0] 3650.51M 7B   deepseek-coder:6.7b              llama       
[ 1] 261.60M 137M nomic-embed-text:latest          nomic-bert  
[ 2] 2282.36M 3.8B phi3:latest                      phi3        
[ 3] 2821.01M 3B   dolphin-phi:2.7b-v2.6-q8_0       phi2        
[ 4] 4692.78M 8B   sunapi386/llama-3-lexi-uncensored:8b llama       
[ 5] 7505.03M 7B   impulse2000/dolphincoder-starcoder2-7b:q8_0 starcoder2  
[ 6] 3918.58M 7B   wizardlm2:latest                 llama       
[ 7] 8145.13M 8.0B llama3:8b-text-q8_0              llama       
[ 8] 4445.29M 8B   llama3-gradient:latest           llama       
[ 9] 3918.59M 7B   starling-lm:latest               llama       
[10] 3648.67M 7B   codellama:latest                 llama       
[11] 4514.09M 7B   llava:latest                     llama       
[12] 4779.68M 9B   gemma:latest                     gemma       
[13] 3649.51M 7B   llama2:latest                    llama       
[14] 3648.59M 7B   llama2-uncensored:latest         llama       
[15] 5791.08M 11B  solar:latest                     llama       
[16] 4445.29M 8.0B llama3:latest                    llama       
[17] 3919.46M 7B   neural-chat:latest               llama       
[18] 1528.23M 3B   phi:latest                       phi2        
[19] 4779.68M 9B   gemma:7b                         gemma       
[20] 1600.70M 3B   gemma:2b                         gemma       
[21] 4692.79M 8B   gurubot/llama3-guru-uncensored:latest llama       
[22] 4692.79M 8B   war-resolver:latest              llama       
[23] 3919.47M 7B   mistral:7b                       llama       
[24] 5821.97M 11B  gfg/solar-10.7b-instruct-v1.0-uncensored:latest llama       
[25] 5467.90M 8B   mannix/dolphin-2.9-llama3-8b:q5_k_m llama       
[26] 8802.34M 13B  wizardlm-uncensored:13b-llama2-q5_K_M llama       
[27] 7024.61M 13B  wizard-vicuna-uncensored:13b     llama       
[28] 4692.79M 8B   gurubot/llama3-guru:latest       llama       
* model: nomic-embed-text:latest [selected]
	* family=nomic-bert
	* parameter_size=137M
	* quantization_level=F16
* auto-remove of context
* new empty context
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

* nomic-embed-text:latest thinking ...


--
! ∓inal error: embedding models do not support generate
