# Copilot Frame Contact Visualization

This document provides visual representations of the Copilot frame contact architecture.

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    OBSIDIAN VAULT                               │
│  ┌───────────────────────────────────────────────────────────┐  │
│  │              COPILOT PLUGIN (v3.1.3)                      │  │
│  │                                                           │  │
│  │  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │  │
│  │  │ Chat         │  │ Vector       │  │ Autonomous   │  │  │
│  │  │ Interface    │  │ Store        │  │ Agent        │  │  │
│  │  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘  │  │
│  └─────────┼─────────────────┼─────────────────┼───────────┘  │
│            │                 │                 │               │
│  ┌─────────▼─────────────────▼─────────────────▼──────────┐   │
│  │               File System Integration                   │   │
│  │  • copilot/copilot-conversations/                      │   │
│  │  • copilot/copilot-custom-prompts/                     │   │
│  │  • copilot/memory/                                     │   │
│  │  • Active note context                                 │   │
│  └─────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
        ▼                   ▼                   ▼
┌───────────────┐  ┌────────────────┐  ┌────────────────┐
│  EXTERNAL     │  │  LOCAL         │  │  SERVICES      │
│  AI APIs      │  │  SERVERS       │  │  & TOOLS       │
└───────────────┘  └────────────────┘  └────────────────┘
```

## External AI Provider Connections

```
COPILOT PLUGIN
      │
      ├─► OpenAI ──────────► api.openai.com/v1
      │                      • Chat Models (GPT-5, GPT-4.1)
      │                      • Embeddings (text-embedding-3)
      │
      ├─► Anthropic ────────► api.anthropic.com/
      │                      • Claude Sonnet 4
      │                      • Reasoning capability
      │
      ├─► Google AI ────────► Google API
      │                      • Gemini 2.5 (Flash, Pro)
      │                      • Embeddings
      │
      ├─► Azure OpenAI ─────► {instance}.openai.azure.com
      │                      • Enterprise OpenAI
      │
      ├─► Mistral AI ───────► api.mistral.ai/v1
      │                      • Pixtral Large
      │                      • Codestral, Devstral
      │
      ├─► X.AI (Grok) ──────► api.x.ai/v1
      │                      • Grok-4-fast
      │
      ├─► DeepSeek ─────────► api.deepseek.com/
      │                      • DeepSeek Chat & Reasoner
      │
      ├─► SiliconFlow ──────► api.siliconflow.com/v1
      │                      • DeepSeek V3/R1
      │                      • Qwen Embeddings
      │
      ├─► Groq ─────────────► api.groq.com
      │                      • Fast inference
      │
      ├─► Cohere ───────────► api.cohere.com
      │                      • Multilingual embeddings
      │
      ├─► Jina AI ──────────► api.jina.ai/v1/embeddings
      │                      • Copilot Plus embeddings
      │
      ├─► OpenRouter ───────► Multi-provider aggregator
      │                      • Various models
      │
      ├─► Amazon Bedrock ───► AWS API
      │                      • AWS-hosted models
      │
      ├─► Hugging Face ─────► Configured endpoint
      │                      • HF models
      │
      ├─► Brevi Labs ───────► api.brevilabs.com/v1
      │                      • Additional models
      │
      ├─► LangChain ────────► api.smith.langchain.com
      │                      • Tracing & monitoring
      │
      └─► Copilot Plus ─────► Premium service endpoint
                             • Exclusive models
```

## Data Flow Diagram

```
┌─────────────┐
│    USER     │
└──────┬──────┘
       │ Input/Commands
       ▼
┌─────────────────────────────────────┐
│     COPILOT UI                      │
│  • Chat Interface                   │
│  • Command Palette                  │
│  • Quick Commands                   │
└──────┬──────────────────────────────┘
       │
       ▼
┌─────────────────────────────────────┐
│   CONTEXT GATHERING                 │
│  • Active Note                      │
│  • Text Selection                   │
│  • Conversation History             │
│  • Vector Search (RAG)              │
│  • Saved Memory                     │
└──────┬──────────────────────────────┘
       │
       ├───────────────┐
       │               │
       ▼               ▼
┌─────────────┐  ┌─────────────┐
│  SEMANTIC   │  │   LEXICAL   │
│   SEARCH    │  │   SEARCH    │
│ (Embeddings)│  │  (Keywords) │
└──────┬──────┘  └──────┬──────┘
       │                │
       └────────┬───────┘
                │ Context
                ▼
       ┌─────────────────┐
       │  PROMPT BUILD   │
       │ • System Prompt │
       │ • User Context  │
       │ • Memory        │
       └────────┬────────┘
                │
                ▼
       ┌─────────────────┐
       │   AI PROVIDER   │
       │   • Model Call  │
       │   • Streaming   │
       └────────┬────────┘
                │
                ▼
       ┌─────────────────┐
       │   RESPONSE      │
       │   PROCESSING    │
       │ • Parse output  │
       │ • Tool calls    │
       └────────┬────────┘
                │
       ┌────────┴────────┐
       │                 │
       ▼                 ▼
┌─────────────┐   ┌─────────────┐
│  DISPLAY    │   │ SAVE/MEMORY │
│  • UI       │   │ • History   │
│  • Format   │   │ • Memory    │
└─────────────┘   └─────────────┘
```

## Autonomous Agent Tool Flow

```
┌──────────────────────────────┐
│   AGENT ENABLED TOOLS        │
└──────────────────────────────┘
       │
       ├─► localSearch ──────► Vault Search
       │                       └─► Returns: Notes
       │
       ├─► readNote ─────────► File Read
       │                       └─► Returns: Content
       │
       ├─► webSearch ────────► External Search
       │                       └─► Returns: Web Results
       │
       ├─► pomodoro ─────────► Timer Control
       │                       └─► Returns: Timer Status
       │
       ├─► youtubeTranscription ► YouTube API
       │                       └─► Returns: Transcript
       │
       ├─► writeToFile ──────► File Creation
       │                       └─► Returns: Success
       │
       ├─► replaceInFile ────► File Edit
       │                       └─► Returns: Updated Content
       │
       └─► updateMemory ─────► Memory Management
                               └─► Returns: Memory State
```

## Vector Store Architecture

```
┌─────────────────────────────────────┐
│        VAULT NOTES                  │
│  • Markdown Files                   │
│  • Active Notes                     │
│  • Included Paths                   │
│  • Excluded Paths (qaExclusions)    │
└────────────┬────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│     DOCUMENT CHUNKING               │
│  • Split by size                    │
│  • Preserve context                 │
└────────────┬────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│     EMBEDDING GENERATION            │
│  • Provider: OpenAI/Cohere/etc      │
│  • Model: text-embedding-3-small    │
│  • Batch Size: 16                   │
│  • Rate Limit: 60/min               │
└────────────┬────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│     VECTOR STORE                    │
│  • Store embeddings                 │
│  • Index for search                 │
│  • Partitions: 1                    │
│  • Max Source Chunks: 15            │
└────────────┬────────────────────────┘
             │
             ├─► SEMANTIC SEARCH ─────► Similarity
             │                          Matching
             │
             └─► LEXICAL BOOST ───────► Keyword
                                        Enhancement
```

## Configuration Hierarchy

```
┌─────────────────────────────────────┐
│    COPILOT CONFIGURATION            │
│    (.obsidian/plugins/copilot/      │
│     data.json)                      │
└─────────────────────────────────────┘
       │
       ├─► API Keys
       │    ├─► openAIApiKey
       │    ├─► anthropicApiKey
       │    ├─► mistralApiKey
       │    └─► ... (15+ providers)
       │
       ├─► Model Configuration
       │    ├─► activeModels (30+)
       │    ├─► activeEmbeddingModels (10+)
       │    └─► defaultModelKey
       │
       ├─► Chat Settings
       │    ├─► temperature: 0.1
       │    ├─► maxTokens: 6000
       │    ├─► contextTurns: 15
       │    └─► stream: true
       │
       ├─► Vault Integration
       │    ├─► defaultSaveFolder
       │    ├─► customPromptsFolder
       │    ├─► memoryFolderName
       │    ├─► qaExclusions
       │    └─► includeActiveNoteAsContext
       │
       ├─► Vector Store
       │    ├─► indexVaultToVectorStore
       │    ├─► enableIndexSync
       │    ├─► embeddingBatchSize: 16
       │    └─► maxSourceChunks: 15
       │
       └─► Agent Settings
            ├─► enableAutonomousAgent
            ├─► autonomousAgentMaxIterations: 4
            └─► autonomousAgentEnabledToolIds[]
```

## Security & Privacy Flow

```
┌─────────────────────────────────────┐
│         USER DATA                   │
│  • Notes                            │
│  • Conversations                    │
│  • API Keys                         │
└────────────┬────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│    OPTIONAL ENCRYPTION              │
│    enableEncryption: false          │
└────────────┬────────────────────────┘
             │
      ┌──────┴──────┐
      │             │
      ▼             ▼
┌──────────┐  ┌──────────┐
│ LOCAL    │  │ EXTERNAL │
│ STORAGE  │  │ API CALL │
│          │  │          │
│ • Files  │  │ • HTTPS  │
│ • Vector │  │ • API Key│
│ • Memory │  │ • Stream │
└──────────┘  └──────────┘
```

## Export/Relink Flow (for #47)

```
┌─────────────────────────────────────┐
│     CURRENT ENVIRONMENT             │
└────────────┬────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│         EXPORT PHASE                │
│                                     │
│  1. Extract Configuration           │
│     • data.json (API keys removed)  │
│     • Folder structure              │
│                                     │
│  2. Export Content                  │
│     • Conversations (markdown)      │
│     • Custom Prompts (markdown)     │
│     • Memory Files (markdown)       │
│                                     │
│  3. Export Metadata                 │
│     • Vector index metadata         │
│     • Model preferences             │
│     • Settings                      │
└────────────┬────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│         TRANSPORT                   │
│  • Git repository                   │
│  • File transfer                    │
│  • Cloud sync                       │
└────────────┬────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│     NEW ENVIRONMENT                 │
└────────────┬────────────────────────┘
             │
             ▼
┌─────────────────────────────────────┐
│         RELINK PHASE                │
│                                     │
│  1. Verify Structure                │
│     • copilot/ folders exist        │
│     • Path references correct       │
│                                     │
│  2. Configure API Keys              │
│     • Add new/existing API keys     │
│     • Test connectivity             │
│                                     │
│  3. Rebuild Indexes                 │
│     • Vector store rebuild          │
│     • Verify embeddings             │
│                                     │
│  4. Test Functionality              │
│     • Chat interface                │
│     • Search functionality          │
│     • Agent tools                   │
│     • Custom prompts                │
└─────────────────────────────────────┘
```

## Integration Point Summary

| Layer | Components | Count | Type |
|-------|-----------|-------|------|
| External APIs | AI Providers | 17 | Outbound |
| External APIs | Update Check | 1 | Outbound |
| Local Services | Ollama | 1 | Outbound |
| Local Services | Dev Servers | 2+ | Outbound |
| Vault | File System | 1 | Bidirectional |
| Vault | Vector Store | 1 | Bidirectional |
| Vault | Active Context | 1 | Inbound |
| Tools | Agent Actions | 8 | Bidirectional |
| UI | User Interface | 1 | Bidirectional |
| Memory | Saved Context | 1 | Bidirectional |
| **TOTAL** | | **35+** | |

---

**Note**: This visualization complements the detailed technical documentation in `copilot-frame-contacts.md`.
