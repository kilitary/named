# Copilot Frame Contacts Documentation Index

**Issue Reference**: Sub-issue of [kilitary/named#47](https://github.com/kilitary/named/issues/47)  
**Status**: ✅ Complete  
**Date**: 2025-11-18

---

## Overview

This documentation set provides a comprehensive analysis of all contact points (endpoints, APIs, and integration touchpoints) where the Copilot frame (Obsidian Copilot plugin v3.1.3) interacts with other components and external systems.

## Documentation Files

### 1. Main Technical Analysis
📄 **[copilot-frame-contacts.md](./copilot-frame-contacts.md)**
- **Size**: 810 lines, 19KB
- **Purpose**: Complete technical documentation of all integration points
- **Contents**:
  - 17 External AI Provider APIs with endpoints, configurations, and models
  - Local server integrations (Ollama, development servers)
  - Internal Obsidian vault file system integration
  - Vector store and semantic search architecture
  - 8 Autonomous agent tools
  - UI integration points
  - Security and encryption features
  - Memory system
  - Custom prompt templating
  - Export/relink recommendations for issue #47
  - Code references

### 2. Quick Reference Guide
📄 **[copilot-frame-contacts-summary.md](./copilot-frame-contacts-summary.md)**
- **Size**: 96 lines, 3.1KB
- **Purpose**: Condensed quick-reference for developers and operators
- **Contents**:
  - Summary list of all 17 AI providers
  - Export/relink checklist
  - Security alerts
  - Integration point counts
  - Connection type summary table

### 3. Visual Architecture Diagrams
📄 **[copilot-frame-contacts-diagrams.md](./copilot-frame-contacts-diagrams.md)**
- **Size**: 398 lines, 13KB
- **Purpose**: Visual representations of the plugin architecture
- **Contents**:
  - Architecture overview diagram
  - External AI provider connections map
  - Data flow diagram
  - Autonomous agent tool flow
  - Vector store architecture
  - Configuration hierarchy
  - Security & privacy flow
  - Export/relink flow (for issue #47)
  - Integration summary table

## Quick Stats

- **Total Integration Points**: 60+
- **External API Endpoints**: 40+
- **AI Provider Services**: 17
- **Local Server Integrations**: 3+
- **Autonomous Agent Tools**: 8
- **File System Locations**: 3 (conversations, prompts, memory)
- **Total Documentation Lines**: 1,304

## Key Integration Categories

### External APIs (Outbound)
1. OpenAI - `api.openai.com/v1`
2. Anthropic - `api.anthropic.com/`
3. Google AI - Google API endpoints
4. Azure OpenAI - Dynamic instance URLs
5. Mistral AI - `api.mistral.ai/v1`
6. X.AI (Grok) - `api.x.ai/v1`
7. DeepSeek - `api.deepseek.com/`
8. SiliconFlow - `api.siliconflow.com/v1`
9. Groq - `api.groq.com`
10. Cohere - `api.cohere.com`
11. Jina AI - `api.jina.ai/v1/embeddings`
12. OpenRouter - Multi-provider
13. Amazon Bedrock - AWS endpoints
14. Hugging Face - Model hub
15. Brevi Labs - `api.brevilabs.com/v1`
16. LangChain Smith - `api.smith.langchain.com`
17. Copilot Plus - Premium service

### Local Integration
- **Ollama**: `localhost:11434` (local LLM)
- **Dev Servers**: Various local ports

### Internal Vault Integration (Bidirectional)
- **File System**: Read/write access to vault
- **Vector Store**: Semantic search and RAG
- **Active Context**: Current note content

### Tools (Bidirectional)
- localSearch
- readNote
- webSearch
- pomodoro
- youtubeTranscription
- writeToFile
- replaceInFile
- updateMemory

## For Issue #47: Export/Relink

### Export Considerations
✅ API credentials (secure handling)  
✅ Vector store (rebuild may be needed)  
✅ Custom prompts (portable)  
✅ Conversation history (portable)  
✅ Memory files (portable)  
✅ Configuration paths (relative)

### Relink Steps
1. Update API keys in new environment
2. Verify folder structure
3. Rebuild vector store if needed
4. Test connectivity to AI providers
5. Verify autonomous agent tools
6. Test custom prompts
7. Validate memory system

## Security Alert

⚠️ **Critical**: Active Mistral AI API key found in configuration:
```
File: .obsidian/plugins/copilot/data.json
Field: mistralApiKey
Action Required: Rotate key immediately
```

## Source Code References

- **Plugin Directory**: `.obsidian/plugins/copilot/`
- **Main Code**: `.obsidian/plugins/copilot/main.js`
- **Configuration**: `.obsidian/plugins/copilot/data.json`
- **Manifest**: `.obsidian/plugins/copilot/manifest.json`
- **Custom Prompts**: `./copilot/copilot-custom-prompts/*.md`
- **Conversations**: `./copilot/copilot-conversations/*.md`
- **Memory**: `./copilot/memory/`

## How to Use This Documentation

### For Developers
Start with the [main technical analysis](./copilot-frame-contacts.md) to understand all integration points and their implementation details.

### For Operations/DevOps
Use the [quick reference guide](./copilot-frame-contacts-summary.md) for a condensed view of all connections and export/relink procedures.

### For Architects
Review the [visual diagrams](./copilot-frame-contacts-diagrams.md) to understand the overall architecture and data flows.

### For Issue #47 Implementation
All three documents contain relevant information for export/linking/relinking:
1. Technical details in main document
2. Checklists in summary
3. Flow diagrams for the process

## Metadata

- **Plugin**: Obsidian Copilot v3.1.3
- **Plugin Author**: Logan Yang
- **Plugin URL**: https://github.com/logancyang/obsidian-copilot
- **Analysis Date**: 2025-11-18
- **Analysis Author**: GitHub Copilot Agent
- **Repository**: kilitary/named
- **Branch**: copilot/identify-copilot-frame-contacts

## Related Issues

- **Parent Issue**: [kilitary/named#47](https://github.com/kilitary/named/issues/47) - Export, link, and relink processes
- **This Issue**: Identify Copilot frame contacts (sub-issue)

## Document Status

✅ **COMPLETE** - All contact points identified, documented, and visualized with code references and export/relink recommendations.

---

*Last updated: 2025-11-18*
