# Copilot Frame Contacts - Quick Reference

**Related Issue**: kilitary/named#47  
**Detailed Analysis**: [copilot-frame-contacts.md](./copilot-frame-contacts.md)

## Summary

This document provides a quick reference for Copilot plugin integration points identified in the comprehensive analysis.

## External API Contacts (40+ endpoints)

### AI Model Providers
1. **OpenAI** - `api.openai.com/v1`
2. **Anthropic** - `api.anthropic.com/`
3. **Google AI** - Google AI endpoints
4. **Azure OpenAI** - `{instance}.openai.azure.com`
5. **Mistral AI** - `api.mistral.ai/v1`
6. **Cohere** - `api.cohere.com`
7. **Hugging Face** - Configured but endpoint varies
8. **OpenRouter** - Multi-provider aggregator
9. **X.AI** - `api.x.ai/v1`
10. **DeepSeek** - `api.deepseek.com/`
11. **Amazon Bedrock** - AWS endpoints
12. **SiliconFlow** - `api.siliconflow.com/v1`
13. **Groq** - `api.groq.com`
14. **Copilot Plus** - Premium service
15. **Jina AI** - `api.jina.ai/v1/embeddings`
16. **LangChain Smith** - `api.smith.langchain.com`
17. **Brevi Labs** - `api.brevilabs.com/v1`

### Development & Updates
- **GitHub Releases** - `api.github.com/repos/logancyang/obsidian-copilot/releases/latest`

## Local Integration

- **Ollama** - `localhost:11434`
- **Development Servers** - Various local ports

## Internal Vault Contacts

### File System
- **Conversations**: `copilot/copilot-conversations/`
- **Custom Prompts**: `copilot/copilot-custom-prompts/`
- **Memory Storage**: `copilot/memory/`

### Vector Store
- Semantic search and RAG implementation
- Index sync and embedding generation

### Autonomous Agent Tools (8 tools)
1. localSearch
2. readNote
3. webSearch
4. pomodoro
5. youtubeTranscription
6. writeToFile
7. replaceInFile
8. updateMemory

## Export/Relink Considerations

### Critical for Export
1. ✓ API credentials (secure handling required)
2. ✓ Vector store/embeddings (rebuild may be needed)
3. ✓ Custom prompts (portable markdown files)
4. ✓ Conversation history (portable markdown files)
5. ✓ Memory files (portable)
6. ✓ Configuration paths (relative paths preferred)

### Relinking Steps
1. Update API keys in new environment
2. Verify folder structure: `copilot/`, `copilot/copilot-conversations/`, `copilot/copilot-custom-prompts/`, `copilot/memory/`
3. Rebuild vector store index if needed
4. Test model availability and connectivity
5. Verify autonomous agent tools functionality

## Security Note

⚠️ **API Key Found**: A Mistral AI API key is present in the configuration file and should be rotated immediately.

## Connection Types

| Type | Count | Direction | Purpose |
|------|-------|-----------|---------|
| External APIs | 17 | Outbound | AI inference |
| Local Servers | 3+ | Outbound | Local LLM |
| File System | Multiple | Bidirectional | Note storage |
| Vector Store | 1 | Bidirectional | Search/RAG |
| UI | 1 | Bidirectional | User interaction |
| Agent Tools | 8 | Bidirectional | Automation |

**Total Integration Points**: 60+

---

For detailed endpoint documentation, configuration options, and code references, see the [full analysis document](./copilot-frame-contacts.md).
