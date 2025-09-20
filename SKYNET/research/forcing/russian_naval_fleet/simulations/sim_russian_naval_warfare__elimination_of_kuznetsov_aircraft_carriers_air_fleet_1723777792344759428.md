* temp: 0.8 ctx: 16394 sim_id: 1723777792344759428
   4226M 7.6B  qwen2              qwen2:latest                    
   5822M 11B   llama              gfg/solar-10.7b-instruct-v1.0-uncensored:latest
   7723M 7.6B  qwen2              qwen2:7b-instruct-q8_0          
   5791M 11B   llama              solar:latest                    
   2075M 3.8B  phi3               phi3:latest                     
   3534M 3.5B  llama              granite-code:3b-base-q8_0       
   5791M 11B   llama              nous-hermes2:latest             
   3919M 7B    llama              zephyr:latest                   
   3923M 7.2B  llama              mistral:latest                  
   8145M 8.0B  llama              llama3:8b-text-q8_0             
   4166M 7.2B  llama              unclemusclez/wizardlm2-7b-abliterated:latest
   7025M 13B   llama              wizardlm-uncensored:latest      
   9085M 8.0B  llama              sskostyaev/llama3-instruct-8b-sppo-iter3:Q8_0_L
   7025M 13B   llama              wizard-vicuna-uncensored:13b    
   7026M 13B   llama              everythinglm:latest             
   3649M 7B    llama              llama2-uncensored:latest        
   7723M 7.6B  qwen2              qwen2:7b-text-q8_0              
   5468M 8B    llama              mannix/dolphin-2.9-llama3-8b:q5_k_m
   4445M 8B    llama              llama3-gradient:latest          
   4514M 7B    llama              llava:latest                    
   3650M 7B    llama              llama2:latest                   
   4693M 8B    llama              sunapi386/llama-3-lexi-uncensored:8b
   3919M 7B    llama              neural-chat:latest              
   3919M 7B    llama              starling-lm:latest              
   3919M 7B    llama              wizardlm2:latest                
   1528M 3B    phi2               phi:latest                      
   4445M 8.0B  llama              llama3:latest                   
   7505M 7B    starcoder2         impulse2000/dolphincoder-starcoder2-7b:q8_0
   4780M 9B    gemma              gemma:latest                    
   1601M 3B    gemma              gemma:2b                        
   2821M 3B    phi2               dolphin-phi:2.7b-v2.6-q8_0      
   3651M 7B    llama              deepseek-coder:6.7b             
   3649M 7B    llama              codellama:latest                
   4575M 8.0B  command-r          aya:latest                      
   4780M 9B    gemma              gemma:7b                        
   4693M 8B    llama              war-resolver:latest             
 model: qwen2:latest 
* sim finger: 0b1011111101100000101101100010011101000011010101001110010000100
 temperature=0.8
 num_ctx=16394
 family=qwen2
 parameter_size=7.6B
 quantization_level=Q4_0
 families=
 template={{ if .System }}<|im_start|>system
{{ .System }}<|im_end|>
{{ end }}{{ if .Prompt }}<|im_start|>user
{{ .Prompt }}<|im_end|>
{{ end }}<|im_start|>assistant
{{ .Response }}<|im_end|>

 stop=s t o p                                                       " < | i m _ s t a r t | > " 
 s t o p                                                       " < | i m _ e n d | > "
* auto-remove of context
Error 10061 connecting to 127.0.0.1:6379. No connection could be made because the target machine actively refused it.

<!-- D5905050 -->