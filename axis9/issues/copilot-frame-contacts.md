# Copilot Frame Contacts Analysis

**Issue Reference**: Sub-issue of kilitary/named#47  
**Date**: 2025-11-18  
**Plugin Version**: Copilot v3.1.3  
**Author**: Logan Yang  

---

## Executive Summary

This document provides a comprehensive analysis of all contact points (endpoints, APIs, and integration touchpoints) where the Copilot frame (Obsidian Copilot plugin) interacts with other components and external systems.

The Copilot plugin is an AI-powered assistant integrated into Obsidian that enables users to chat with their notes, perform semantic search, and utilize various AI models through external API services.

---

## 1. External AI Provider APIs (Outbound)

### 1.1 OpenAI Integration
**Direction**: Outbound  
**Purpose**: Chat completion, embeddings, and vision capabilities  

**Endpoints**:
- Primary API: `https://api.openai.com/v1`
- Models endpoint: `https://api.openai.com/v1/models`
- Proxy support via configurable `openAIProxyBaseUrl`
- Embedding proxy support via `openAIEmbeddingProxyBaseUrl`

**Configuration Fields**:
```json
{
  "openAIApiKey": "",
  "openAIOrgId": "",
  "openAIProxyBaseUrl": "",
  "openAIEmbeddingProxyBaseUrl": ""
}
```

**Models Supported**:
- gpt-5, gpt-5-mini
- gpt-4.1, gpt-4.1-mini
- text-embedding-3-small
- text-embedding-3-large

**Code Reference**: `.obsidian/plugins/copilot/main.js` (OpenAI client initialization)

---

### 1.2 Anthropic Integration
**Direction**: Outbound  
**Purpose**: Claude model access for chat completion and reasoning

**Endpoints**:
- Primary API: `https://api.anthropic.com/`
- Models endpoint: `https://api.anthropic.com/v1/models`

**Configuration Fields**:
```json
{
  "anthropicApiKey": ""
}
```

**Models Supported**:
- claude-sonnet-4-20250514 (with reasoning and vision capabilities)

**Code Reference**: `.obsidian/plugins/copilot/main.js`

---

### 1.3 Google AI Integration
**Direction**: Outbound  
**Purpose**: Gemini models for chat and embeddings

**Endpoints**:
- Google AI API (endpoint varies based on model)

**Configuration Fields**:
```json
{
  "googleApiKey": ""
}
```

**Models Supported**:
- gemini-2.5-flash
- gemini-2.5-flash-lite
- gemini-2.5-pro
- gemini-embedding-001
- text-embedding-004

**Code Reference**: `.obsidian/plugins/copilot/main.js`

---

### 1.4 Azure OpenAI Integration
**Direction**: Outbound  
**Purpose**: Enterprise OpenAI access through Azure

**Endpoints**:
- Dynamic URL: `https://{instanceName}.openai.azure.com/openai/deployments/{deploymentName}`

**Configuration Fields**:
```json
{
  "azureOpenAIApiKey": "",
  "azureOpenAIApiInstanceName": "",
  "azureOpenAIApiDeploymentName": "",
  "azureOpenAIApiVersion": "",
  "azureOpenAIApiEmbeddingDeploymentName": ""
}
```

**Code Reference**: `.obsidian/plugins/copilot/main.js`

---

### 1.5 Mistral AI Integration
**Direction**: Outbound  
**Purpose**: Mistral models for chat completion

**Endpoints**:
- Primary API: `https://api.mistral.ai`
- API version: `https://api.mistral.ai/v1`
- Models endpoint: `https://api.mistral.ai/v1/models`

**Configuration Fields**:
```json
{
  "mistralApiKey": "XUO8AySQv3QajDNYVq3Gug0D04lyNOGU"
}
```

**Models Supported**:
- pixtral-large-latest
- mistral-tiny-latest
- devstral-medium-latest
- codestral-2508
- open-mistral-7b
- open-mistral-nemo-2407
- voxtral-small-latest

**Code Reference**: `.obsidian/plugins/copilot/data.json`, `.obsidian/plugins/copilot/main.js`

---

### 1.6 Cohere AI Integration
**Direction**: Outbound  
**Purpose**: Multilingual embeddings

**Endpoints**:
- Primary API: `https://api.cohere.com`
- Models endpoint: `https://api.cohere.com/v1/models`

**Configuration Fields**:
```json
{
  "cohereApiKey": ""
}
```

**Models Supported**:
- embed-multilingual-light-v3.0

**Code Reference**: `.obsidian/plugins/copilot/main.js`

---

### 1.7 Hugging Face Integration
**Direction**: Outbound  
**Purpose**: Access to Hugging Face hosted models

**Configuration Fields**:
```json
{
  "huggingfaceApiKey": ""
}
```

**Code Reference**: `.obsidian/plugins/copilot/data.json`

---

### 1.8 OpenRouter AI Integration
**Direction**: Outbound  
**Purpose**: Multi-provider model access through OpenRouter

**Configuration Fields**:
```json
{
  "openRouterAiApiKey": ""
}
```

**Models Supported via OpenRouter**:
- google/gemini-2.5-flash-lite
- google/gemini-2.5-flash
- google/gemini-2.5-pro
- openai/gpt-4.1
- openai/gpt-4.1-mini
- x-ai/grok-4-fast

**Code Reference**: `.obsidian/plugins/copilot/data.json`

---

### 1.9 X.AI Integration
**Direction**: Outbound  
**Purpose**: Grok model access

**Endpoints**:
- Primary API: `https://api.x.ai/v1`
- Models endpoint: `https://api.x.ai/v1/models`

**Configuration Fields**:
```json
{
  "xaiApiKey": ""
}
```

**Models Supported**:
- grok-4-fast (with vision capabilities)

**Code Reference**: `.obsidian/plugins/copilot/main.js`

---

### 1.10 DeepSeek Integration
**Direction**: Outbound  
**Purpose**: DeepSeek models for chat and reasoning

**Endpoints**:
- Primary API: `https://api.deepseek.com/`
- Models endpoint: `https://api.deepseek.com/models`

**Configuration Fields**:
```json
{
  "deepseekApiKey": ""
}
```

**Models Supported**:
- deepseek-chat
- deepseek-reasoner (with reasoning capability)

**Code Reference**: `.obsidian/plugins/copilot/main.js`

---

### 1.11 Amazon Bedrock Integration
**Direction**: Outbound  
**Purpose**: AWS-hosted AI models

**Endpoints**:
- AWS API: `https://api.aws`
- Regional variations: `https://api.amazonwebservices.com.cn`

**Configuration Fields**:
```json
{
  "amazonBedrockApiKey": "",
  "amazonBedrockRegion": ""
}
```

**Code Reference**: `.obsidian/plugins/copilot/main.js`

---

### 1.12 SiliconFlow Integration
**Direction**: Outbound  
**Purpose**: Access to various models through SiliconFlow platform

**Endpoints**:
- Primary API: `https://api.siliconflow.com/v1`
- Models endpoint: `https://api.siliconflow.com/v1/models`

**Configuration Fields**:
```json
{
  "siliconflowApiKey": ""
}
```

**Models Supported**:
- deepseek-ai/DeepSeek-V3
- deepseek-ai/DeepSeek-R1 (with reasoning)
- Qwen/Qwen3-Embedding-0.6B (embedding model)

**Code Reference**: `.obsidian/plugins/copilot/data.json`, `.obsidian/plugins/copilot/main.js`

---

### 1.13 Groq Integration
**Direction**: Outbound  
**Purpose**: Fast inference access to various models

**Endpoints**:
- Primary API: `https://api.groq.com`
- OpenAI-compatible: `https://api.groq.com/openai`
- Models endpoint: `https://api.groq.com/openai/v1/models`

**Configuration Fields**:
```json
{
  "groqApiKey": ""
}
```

**Code Reference**: `.obsidian/plugins/copilot/main.js`

---

### 1.14 Copilot Plus Service
**Direction**: Outbound  
**Purpose**: Premium Copilot features and models

**Configuration Fields**:
```json
{
  "isPlusUser": false,
  "plusLicenseKey": ""
}
```

**Models Supported**:
- copilot-plus-flash (chat with vision, Plus exclusive)
- copilot-plus-small (embedding, Plus exclusive)
- copilot-plus-large (embedding via Jina, Plus exclusive, Believer exclusive)
- copilot-plus-multilingual (embedding via Jina, Plus exclusive)

**Code Reference**: `.obsidian/plugins/copilot/data.json`

---

### 1.15 Jina AI Integration
**Direction**: Outbound  
**Purpose**: Embedding services for Copilot Plus

**Endpoints**:
- Embeddings API: `https://api.jina.ai/v1/embeddings`

**Models Supported**:
- copilot-plus-large (via provider: copilot-plus-jina)
- copilot-plus-multilingual (via provider: copilot-plus-jina)

**Code Reference**: `.obsidian/plugins/copilot/main.js`

---

### 1.16 LangChain Smith Integration
**Direction**: Outbound  
**Purpose**: LangChain tracing and monitoring

**Endpoints**:
- API: `https://api.smith.langchain.com`

**Code Reference**: `.obsidian/plugins/copilot/main.js`

---

### 1.17 Brevi Labs Integration
**Direction**: Outbound  
**Purpose**: Additional AI model access

**Endpoints**:
- API: `https://api.brevilabs.com/v1`

**Code Reference**: `.obsidian/plugins/copilot/main.js`

---

## 2. GitHub Integration (Outbound)

### 2.1 Plugin Update Check
**Direction**: Outbound  
**Purpose**: Check for Copilot plugin updates

**Endpoints**:
- Releases API: `https://api.github.com/repos/logancyang/obsidian-copilot/releases/latest`

**Code Reference**: `.obsidian/plugins/copilot/main.js`

---

## 3. Local System Integration

### 3.1 Ollama Local Server
**Direction**: Outbound (Local)  
**Purpose**: Local LLM inference

**Endpoints**:
- Default: `http://localhost:11434`
- OpenAI-compatible: `http://localhost:11434/v1/`
- Alternative port: `http://localhost:1234/v1`

**Code Reference**: `.obsidian/plugins/copilot/main.js`

---

### 3.2 Local Development Servers
**Direction**: Outbound (Local)  
**Purpose**: Development and testing

**Endpoints**:
- `http://localhost:1984`
- `http://localhost:3000`
- `http://127.0.0.1` (dynamic port)

**Code Reference**: `.obsidian/plugins/copilot/main.js`

---

## 4. Obsidian Vault Integration (Internal)

### 4.1 File System Access
**Direction**: Bidirectional  
**Purpose**: Read/write vault notes and attachments

**Paths**:
- Conversation saves: `copilot/copilot-conversations/`
- Custom prompts: `copilot/copilot-custom-prompts/`
- Memory storage: `copilot/memory/`
- User-configurable via `defaultSaveFolder`, `customPromptsFolder`, `memoryFolderName`

**Operations**:
- Read: Active note content, vault files for context
- Write: Conversation logs, custom prompts, memory files
- Search: Semantic and lexical search across vault

**Configuration**:
```json
{
  "defaultSaveFolder": "copilot/copilot-conversations",
  "defaultConversationTag": "copilot-conversation",
  "customPromptsFolder": "copilot/copilot-custom-prompts",
  "memoryFolderName": "copilot/memory",
  "qaExclusions": "copilot",
  "qaInclusions": "",
  "chatNoteContextPath": "",
  "chatNoteContextTags": []
}
```

**Code Reference**: `.obsidian/plugins/copilot/data.json`

---

### 4.2 Vector Store Integration
**Direction**: Bidirectional  
**Purpose**: Semantic search and RAG (Retrieval Augmented Generation)

**Configuration**:
```json
{
  "indexVaultToVectorStore": "ON MODE SWITCH",
  "enableIndexSync": true,
  "embeddingRequestsPerMin": 60,
  "embeddingBatchSize": 16,
  "maxSourceChunks": 15,
  "enableSemanticSearchV3": false,
  "enableLexicalBoosts": true,
  "lexicalSearchRamLimit": 100,
  "numPartitions": 1
}
```

**Operations**:
- Build: Create embeddings for vault notes
- Update: Sync changes to vector store
- Query: Search for relevant context

**Code Reference**: `.obsidian/plugins/copilot/data.json`

---

### 4.3 Active Note Context
**Direction**: Inbound  
**Purpose**: Include current note content in chat context

**Configuration**:
```json
{
  "includeActiveNoteAsContext": true,
  "contextTurns": 15,
  "allowAdditionalContext": true,
  "autoIncludeTextSelection": true
}
```

**Code Reference**: `.obsidian/plugins/copilot/data.json`

---

## 5. Autonomous Agent Tools

### 5.1 Tool Integration
**Direction**: Bidirectional  
**Purpose**: Enable autonomous agent actions within vault

**Enabled Tools**:
```json
{
  "enableAutonomousAgent": true,
  "autonomousAgentMaxIterations": 4,
  "autonomousAgentEnabledToolIds": [
    "localSearch",
    "readNote",
    "webSearch",
    "pomodoro",
    "youtubeTranscription",
    "writeToFile",
    "replaceInFile",
    "updateMemory"
  ]
}
```

**Tool Descriptions**:
- `localSearch`: Search within vault files
- `readNote`: Read specific note content
- `webSearch`: External web search capability
- `pomodoro`: Timer integration
- `youtubeTranscription`: Fetch YouTube transcripts
- `writeToFile`: Create/append to notes
- `replaceInFile`: Edit existing notes
- `updateMemory`: Manage long-term memory

**Code Reference**: `.obsidian/plugins/copilot/data.json`

---

## 6. User Interface Integration

### 6.1 Obsidian UI Messages
**Direction**: Inbound/Outbound  
**Purpose**: User interaction and feedback

**Features**:
- Chat interface in Obsidian sidebar/tab
- Inline edit commands
- Quick command palette integration
- Autocomplete suggestions
- Prompt suggestion display
- Recent conversations list

**Configuration**:
```json
{
  "defaultOpenArea": "view",
  "defaultSendShortcut": "enter",
  "showSuggestedPrompts": true,
  "showRelevantNotes": true,
  "enableRecentConversations": true,
  "maxRecentConversations": 30,
  "enableAutocomplete": false,
  "autocompleteAcceptKey": "Tab",
  "suggestedDefaultCommands": true,
  "quickCommandIncludeNoteContext": true
}
```

**Code Reference**: `.obsidian/plugins/copilot/data.json`

---

## 7. Security and Privacy Features

### 7.1 Encryption Support
**Direction**: Internal  
**Purpose**: Secure storage of sensitive data

**Configuration**:
```json
{
  "enableEncryption": false
}
```

**Code Reference**: `.obsidian/plugins/copilot/data.json`

---

### 7.2 Mobile Optimization
**Direction**: Internal  
**Purpose**: Performance optimization on mobile devices

**Configuration**:
```json
{
  "disableIndexOnMobile": true
}
```

**Code Reference**: `.obsidian/plugins/copilot/data.json`

---

## 8. Project Management Integration

### 8.1 Project Support
**Direction**: Internal  
**Purpose**: Project-specific model configurations

**Configuration**:
```json
{
  "projectList": []
}
```

**Note**: Models can have `projectEnabled: true` flag for project-specific availability.

**Code Reference**: `.obsidian/plugins/copilot/data.json`

---

## 9. Custom Prompt Templating

### 9.1 Template System
**Direction**: Internal  
**Purpose**: Enable custom prompt templates

**Configuration**:
```json
{
  "enableCustomPromptTemplating": true
}
```

**Templates Location**: `copilot/copilot-custom-prompts/`

**Available Templates**:
- Fix grammar and spelling
- Generate table of contents
- Simplify
- Remove URLs
- Translate to Chinese
- Summarize
- Make longer
- Make shorter
- Rewrite as tweet thread
- Generate glossary
- Rewrite as tweet
- Explain like I am 5
- Emojify

**Code Reference**: `./copilot/copilot-custom-prompts/*.md`

---

## 10. Memory System

### 10.1 Saved Memory
**Direction**: Bidirectional  
**Purpose**: Long-term context retention

**Configuration**:
```json
{
  "enableSavedMemory": true,
  "memoryFolderName": "copilot/memory"
}
```

**Operations**:
- Store: Save important context from conversations
- Retrieve: Include saved memory in prompts
- Update: Modify existing memory entries

**Code Reference**: `.obsidian/plugins/copilot/data.json`

---

## 11. Debug and Development

### 11.1 Debug Mode
**Direction**: Internal  
**Purpose**: Development and troubleshooting

**Configuration**:
```json
{
  "debug": false
}
```

**Code Reference**: `.obsidian/plugins/copilot/data.json`

---

## Summary Table

| Contact Type | Direction | Count | Purpose |
|--------------|-----------|-------|---------|
| External AI APIs | Outbound | 17 | Model inference, embeddings |
| GitHub API | Outbound | 1 | Update checks |
| Local Servers | Outbound (Local) | 3+ | Local LLM inference |
| Vault File System | Bidirectional | 1 | Note storage/retrieval |
| Vector Store | Bidirectional | 1 | Semantic search |
| UI Integration | Bidirectional | 1 | User interaction |
| Autonomous Tools | Bidirectional | 8 | Agent actions |
| Memory System | Bidirectional | 1 | Context retention |

**Total External API Endpoints**: 40+  
**Total Integration Points**: 60+

---

## Connection Map

```
┌─────────────────────────────────────────────┐
│         Obsidian Copilot Plugin             │
│              (v3.1.3)                       │
└─────────────────────────────────────────────┘
                    │
        ┌───────────┼───────────┐
        │           │           │
        ▼           ▼           ▼
   ┌────────┐  ┌────────┐  ┌────────┐
   │External│  │ Local  │  │Internal│
   │  APIs  │  │Servers │  │ Vault  │
   └────────┘  └────────┘  └────────┘
        │           │           │
        │           │           │
   ┌────┴────────┐  │      ┌────┴─────┐
   │             │  │      │          │
   ▼             ▼  ▼      ▼          ▼
OpenAI      Anthropic  Ollama   Files   Vector
Google AI   Mistral AI         Context  Store
Azure       Cohere AI          Memory   Search
X.AI        HuggingFace        Prompts  Index
DeepSeek    OpenRouter
SiliconFlow Groq
AWS Bedrock Jina AI
```

---

## Notes and Observations

1. **API Key Security**: Multiple API keys are stored in `data.json`. The `mistralApiKey` field currently contains a real API key that should be rotated immediately.

2. **Proxy Support**: The plugin supports proxy configuration for OpenAI endpoints, useful for network restrictions or rate limiting.

3. **Model Flexibility**: The plugin supports multiple AI providers, allowing users to switch between models based on:
   - Cost
   - Performance
   - Capabilities (vision, reasoning, etc.)
   - Availability

4. **Local-First Option**: Ollama integration allows fully offline operation for privacy-conscious users.

5. **RAG Implementation**: The vector store integration enables Retrieval Augmented Generation, improving answer quality with vault context.

6. **Autonomous Capabilities**: The agent system can perform actions beyond simple chat, including file operations and web searches.

7. **Extensibility**: The custom prompt system and tool integration make the plugin highly extensible.

---

## Recommendations for Export/Linking (kilitary/named#47)

1. **API Credentials**: 
   - Export: API keys should be exported separately or replaced with placeholders
   - Relink: Environment variable or secure credential management should be used

2. **Local Paths**:
   - Export: Relative paths (`copilot/`, `copilot-conversations/`) should work across systems
   - Relink: Verify folder structure is maintained

3. **Vector Store**:
   - Export: Vector embeddings should be exported or flagged for rebuild
   - Relink: May need full re-indexing in new environment

4. **Model Configurations**:
   - Export: Model settings are portable
   - Relink: Verify API availability in new environment

5. **Custom Prompts**:
   - Export: Markdown files are portable
   - Relink: Verify folder path configuration

6. **Memory System**:
   - Export: Memory files should be included
   - Relink: Verify memory folder path

---

## References

- Copilot Plugin: `.obsidian/plugins/copilot/`
- Configuration: `.obsidian/plugins/copilot/data.json`
- Main Code: `.obsidian/plugins/copilot/main.js`
- Manifest: `.obsidian/plugins/copilot/manifest.json`
- Custom Prompts: `./copilot/copilot-custom-prompts/`
- Conversations: `./copilot/copilot-conversations/`
- Author: https://twitter.com/logancyang
- Funding: https://www.buymeacoffee.com/logancyang
- GitHub: https://github.com/sponsors/logancyang

---

**Document Version**: 1.0  
**Last Updated**: 2025-11-18  
**Status**: Complete
