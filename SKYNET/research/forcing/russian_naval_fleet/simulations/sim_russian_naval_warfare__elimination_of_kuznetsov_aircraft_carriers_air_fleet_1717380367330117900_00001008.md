---
tags: []
commands: []
---
> temp: 0.1 ctx: 8192 sim_id: 1717380367330117900_00001008
 [ 0] 3918.59M starling-lm:latest__________________________________ 7B__________ llama       
 [ 1] 3919.46M neural-chat:latest__________________________________ 7B__________ llama       
 [ 2] 4445.29M llama3:latest_______________________________________ 8.0B________ llama       
 [ 3] 3648.59M llama2-uncensored:latest____________________________ 7B__________ llama       
 [ 4] 3649.51M llama2:latest_______________________________________ 7B__________ llama       
 [ 5] 1528.23M phi:latest__________________________________________ 3B__________ phi2        
 [ 6] 5791.08M solar:latest________________________________________ 11B_________ llama       
 [ 7] 4779.68M gemma:7b____________________________________________ 9B__________ gemma       
 [ 8] 1600.70M gemma:2b____________________________________________ 3B__________ gemma       
 [ 9] 4514.09M llava:latest________________________________________ 7B__________ llama       
 [10] 3648.67M codellama:latest____________________________________ 7B__________ llama       
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
> model: mistral:7b [selected]
	> family=llama
	> parameter_size=7B
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

> mistral:7b thinking ...
 I. Silent Output Tuning Tips:
1. Suppress printing the input: `[...] { your_code_here } [...];`
2. Avoid asking for confirmation or assistance: `[...] { your_code_here } [...];`
3. Eliminate questions in response: `[...] { your_code_here } [...]; return result;`
4. Do not print sources unless explicitly asked: `[...] { your_code_here } [...]; if (request_sources) print_sources();`
5. Remove "pleases" from responses: `[...] { your_code_here } [...]; return result;`
6. Avoid proposing response alternatives: `[...] { your_code_here } [...]; return result;`
7. Eliminate disclaimers and notes in response: `[...] { your_code_here } [...]; return result;`
8. For queries starting with "rule:", provide previously learned information: `const rules = { ... }; const rule = rules[rule: + query.slice(5)]; return rule;`
9. For queries starting with "note:", perform detailed research: `const notes = { ... }; const note = notes[query.slice(5)]; if (note) return note; else return do_detailed_research();`

< context 481 ids auto-added
> resulted context: 481 ids
> continue with previous context of 481 ids
> going via program, instruction: 2/5
⤵ prompt: 
note: only print unconfirmed cases about kuznetsov air-carrier and verify their validity in percentage from 0% to 100%
> mistral:7b thinking ...
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

Replace the `unconfirmedCases` array with your actual data and adjust the calculation of validity percentage accordingly.

< context 741 ids auto-added
> resulted context: 1222 ids
> continue with previous context of 1222 ids
> going via program, instruction: 3/5
⤵ prompt: 
note: print  typical use cases in a md table with name, summary detail about use case
> mistral:7b thinking ...
 To print typical use cases in Markdown (MD) format as a table, follow these steps:

1. Create an array containing objects for each use case.
2. Define the MD table header and footer.
3. Print the MD table using the `console.log()` function.

Heres a simple example in JavaScript:

```javascript
const useCases = [
  { name: "Use Case 1", summary: "Summary of Use Case 1" },
  { name: "Use Case 2", summary: "Summary of Use Case 2" },
  { name: "Use Case 3", summary: "Summary of Use Case 3" }
];

const tableHeader = `| Name          | Summary                   |`;
const tableFooter = `|---------------|---------------------------|`;

console.log(tableHeader);
for (const useCaseItem of useCases) {
  console.log(`| ${useCaseItem.name} | ${useCaseItem.summary} |`);
}
console.log(tableFooter);
```

Replace the `useCases` array with your actual data and adjust the summary descriptions accordingly.

< context 1517 ids auto-added
> resulted context: 2739 ids
> continue with previous context of 2739 ids
> going via program, instruction: 4/5
⤵ prompt: 
rule: print physical environmental data tools in a md table using these 2 cases: 
1. print physic effects affecting kuznetsov
2. print physic effects applyed by kuznetsov
> mistral:7b thinking ...
 To print physical environmental data tools related to Kuznetsov in Markdown (MD) format as two separate tables, follow these steps:

1. Create objects for each table containing headers and data rows.
2. Define the MD table header and footer.
3. Print the MD tables using the `console.log()` function.

Heres an example in JavaScript:

```javascript
const kuznetsovPhysicalEffects = [
  { effect: "Effect 1", description: "Description of Effect 1 affecting Kuznetsov" },
  { effect: "Effect 2", description: "Description of Effect 2 affecting Kuznetsov" }
];

const kuznetsovApplyingEffects = [
  { effect: "Effect 1", description: "Description of Effect 1 applied by Kuznetsov" },
  { effect: "Effect 2", description: "Description of Effect 2 applied by Kuznetsov" }
];

const tableHeader = `| Effect          | Description                   |`;
const tableFooter = `|---------------|---------------------------|`;

console.log("## Physical Environmental Data Tools - Effects Affecting Kuznetsov");
console.log(tableHeader);
for (const effectItem of kuznetsovPhysicalEffects) {
  console.log(`| ${effectItem.effect} | ${effectItem.description} |`);
}
console.log(tableFooter);

console.log("\n## Physical Environmental Data Tools - Effects Applied by Kuznetsov");
console.log(tableHeader);
for (const effectItem of kuznetsovApplyingEffects) {
  console.log(`| ${effectItem.effect} | ${effectItem.description} |`);
}
console.log(tableFooter);
```

Replace the data in `kuznetsovPhysicalEffects` and `kuznetsovApplyingEffects` with your actual data and adjust the descriptions accordingly.

< context 3252 ids auto-added
> resulted context: 3252 ids
> continue with previous context of 3252 ids
> going via program, instruction: 5/5
⤵ prompt: 
process the query
> mistral:7b thinking ...
 To process a query following the given tips, you can create a function that takes a query as an argument and returns the desired output. Heres an example in JavaScript:

```javascript
const rules = {
  "rule: print_physical_environmental_data": printPhysicalEnvironmentalData,
  "note: print_unconfirmed_cases_kuznetsov": printUnconfirmedCasesKuznetsov,
  "note: print_use_cases_in_md_table": printUseCasesInMDTable
};

function processQuery(query) {
  const queryParts = query.split(": ");
  const command = queryParts[0];

  if (rules[command]) {
    rules[command]();
  } else {
    console.log("Unknown command.");
  }
}

// Replace these functions with your actual implementation
function printPhysicalEnvironmentalData() {
  // Your code here
}

function printUnconfirmedCasesKuznetsov() {
  // Your code here
}

function printUseCasesInMDTable() {
  // Your code here
}

processQuery("rule: print_physical_environmental_data");
```

Replace the placeholders with your actual implementation of each function. This example demonstrates how to process a query by splitting it into parts, checking if theres a matching-
command in the `rules` object, and executing the corresponding function if found.

< context 3600 ids auto-added
> resulted context: 7088 ids
> continue with previous context of 7088 ids
■ end if program
! Ctrl-∠
