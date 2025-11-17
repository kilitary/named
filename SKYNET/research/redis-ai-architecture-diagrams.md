---
title: "Redis AI Architecture Diagrams"
tags:
  - redis
  - ai
  - architecture
  - diagrams
  - visualization
state: Documentation
type: visual-documentation
---

# Redis AI Architecture Diagrams

Visual representations of Redis AI integration patterns with AI/LLM/Agent systems.

## System Integration Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                     AI/LLM/Agent Ecosystem                          │
│                                                                     │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐          │
│  │   LLM    │  │  Vector  │  │  Agent   │  │  ML/DL   │          │
│  │   APIs   │  │Databases │  │Framework │  │  Models  │          │
│  └─────┬────┘  └─────┬────┘  └─────┬────┘  └─────┬────┘          │
│        │             │             │             │                │
└────────┼─────────────┼─────────────┼─────────────┼────────────────┘
         │             │             │             │
         └─────────────┴─────────────┴─────────────┘
                       │
         ┌─────────────▼─────────────┐
         │                           │
         │      REDIS AI HUB         │
         │                           │
         │  ┌─────────────────────┐  │
         │  │   RedisAI Module    │  │
         │  │  - Model Serving    │  │
         │  │  - Tensor Ops       │  │
         │  └─────────────────────┘  │
         │                           │
         │  ┌─────────────────────┐  │
         │  │   RediSearch        │  │
         │  │  - Vector Index     │  │
         │  │  - Similarity       │  │
         │  └─────────────────────┘  │
         │                           │
         │  ┌─────────────────────┐  │
         │  │   Core Redis        │  │
         │  │  - Cache            │  │
         │  │  - State            │  │
         │  │  - Pub/Sub          │  │
         │  │  - Streams          │  │
         │  └─────────────────────┘  │
         │                           │
         └───────────┬───────────────┘
                     │
         ┌───────────▼───────────┐
         │                       │
         │   Application Layer   │
         │  - Web Apps           │
         │  - Microservices      │
         │  - Mobile Apps        │
         │  - IoT Devices        │
         │                       │
         └───────────────────────┘
```

## Connection Types Matrix

```
┌────────────────────────────────────────────────────────────────┐
│             What Connects to Redis AI & How                    │
└────────────────────────────────────────────────────────────────┘

LLM APIs (OpenAI, Anthropic, Cohere)
├─► Response Caching          [Redis String/Hash]
├─► Rate Limiting             [Redis Counter + TTL]
├─► Token Usage Tracking      [Redis Sorted Set]
└─► Prompt Template Storage   [Redis String/Hash]

Embedding Models (sentence-transformers, OpenAI ada)
├─► Embedding Storage         [Redis + RediSearch Vector]
├─► Batch Processing          [Redis Streams]
└─► Model Inference           [RedisAI]

Agent Frameworks (LangChain, AutoGPT, CrewAI)
├─► Agent State               [Redis Hash/JSON]
├─► Memory Storage            [Redis List/Stream]
├─► Tool Results Cache        [Redis String]
└─► Multi-Agent Messaging     [Redis Pub/Sub]

Vector Databases (Pinecone, Weaviate integration)
├─► Primary Vector Store      [RediSearch native]
├─► Metadata Filtering        [RediSearch filters]
└─► Hybrid Search             [RediSearch + full-text]

Stream Processors (Kafka, Flink, Spark)
├─► Event Ingestion           [Redis Streams]
├─► Processing Queue          [Redis List/Stream]
└─► Result Storage            [Redis Any Type]

ML Frameworks (TensorFlow, PyTorch, ONNX)
├─► Model Serving             [RedisAI]
├─► Feature Store             [Redis Hash/JSON]
└─► Training Data Cache       [Redis Any Type]

Microservices Architecture
├─► Service Discovery         [Redis Hash]
├─► Configuration             [Redis Hash/JSON]
├─► Circuit Breaker State     [Redis String]
└─► Distributed Locks         [Redis String + Lua]

API Gateways (Kong, nginx, Envoy)
├─► Request Routing Rules     [Redis Hash]
├─► Rate Limiting             [Redis Counter]
└─► Response Caching          [Redis String]

Web/Mobile Applications
├─► Session Management        [Redis String/Hash]
├─► User Preferences          [Redis Hash/JSON]
└─► Real-time Updates         [Redis Pub/Sub]
```

## LLM Caching Architecture (Detailed)

```
┌──────────────────────────────────────────────────────────────────┐
│                         Request Flow                              │
└──────────────────────────────────────────────────────────────────┘

┌─────────┐
│ Client  │
│ Request │
└────┬────┘
     │
     │ 1. Incoming Request
     ▼
┌─────────────────┐
│   API Gateway   │
│  - Validation   │
│  - Auth         │
└────┬────────────┘
     │
     │ 2. Generate Cache Key
     │    hash(prompt + model + params)
     ▼
┌─────────────────────────────────┐
│      Redis Cache Layer          │
│                                 │
│  Key Format:                    │
│  llm:cache:{hash}               │
│                                 │
│  Value Structure:               │
│  {                              │
│    "response": "...",           │
│    "model": "gpt-4",            │
│    "timestamp": 1234567890,     │
│    "tokens": 150                │
│  }                              │
└────┬──────────────┬─────────────┘
     │              │
     │ Cache HIT?   │
     │              │
  ┌──▼──────┐  ┌───▼────────┐
  │  YES    │  │    NO      │
  │         │  │            │
  │ Return  │  │ 3. Call    │
  │ Cached  │  │    LLM API │
  │ Response│  │            │
  └──┬──────┘  └───┬────────┘
     │             │
     │             ▼
     │        ┌────────────────┐
     │        │   LLM Service  │
     │        │  (OpenAI, etc) │
     │        └────┬───────────┘
     │             │
     │             │ 4. Get Response
     │             ▼
     │        ┌────────────────┐
     │        │ Store in Cache │
     │        │   TTL: 1 hour  │
     │        └────┬───────────┘
     │             │
     └─────────────┘
                   │
                   ▼
            ┌──────────────┐
            │   Response   │
            │   to Client  │
            └──────────────┘

Performance Metrics:
├─► Cache HIT:  <1ms response time, $0.00 cost
└─► Cache MISS: 500-2000ms, $0.002-0.10 cost per request
```

## Multi-Agent System Architecture

```
┌──────────────────────────────────────────────────────────────────┐
│                    Multi-Agent Redis Architecture                 │
└──────────────────────────────────────────────────────────────────┘

                    ┌─────────────────────┐
                    │   Redis Cluster     │
                    │                     │
                    │  ┌───────────────┐  │
                    │  │ Pub/Sub       │  │
                    │  │ Channels:     │  │
                    │  │ - agent:tasks │  │
                    │  │ - agent:events│  │
                    │  │ - agent:logs  │  │
                    │  └───────────────┘  │
                    │                     │
                    │  ┌───────────────┐  │
                    │  │ State Store   │  │
                    │  │ agent:{id}    │  │
                    │  └───────────────┘  │
                    │                     │
                    │  ┌───────────────┐  │
                    │  │ Shared KB     │  │
                    │  │ knowledge:*   │  │
                    │  └───────────────┘  │
                    │                     │
                    └──────────┬──────────┘
                               │
        ┌──────────────────────┼──────────────────────┐
        │                      │                      │
        ▼                      ▼                      ▼
┌───────────────┐      ┌───────────────┐     ┌───────────────┐
│  Agent Type 1 │      │  Agent Type 2 │     │  Agent Type N │
│  (Planner)    │      │  (Executor)   │     │  (Custom)     │
│               │      │               │     │               │
│ Responsibilities:    │ Responsibilities:   │ Responsibilities:
│ - Task planning      │ - Task execution    │ - Domain specific
│ - Work delegation    │ - Result reporting  │ - Specialized ops
│ - Coordination       │ - Error handling    │ - Integration    │
│                      │                     │                  │
│ Redis Operations:    │ Redis Operations:   │ Redis Operations:
│ • PUBLISH tasks      │ • SUBSCRIBE tasks   │ • Custom logic   │
│ • SET agent state    │ • GET agent state   │ • Data processing│
│ • HSET knowledge     │ • LPUSH results     │ • API calls      │
└───────────────┘      └───────────────┘     └───────────────┘

Communication Flow:
1. Planner → PUBLISH agent:tasks → Executor receives
2. Executor → SET agent:state → Updates progress
3. Executor → PUBLISH agent:events → Planner notified
4. All → HSET knowledge:* → Shared learning
```

## RAG (Retrieval-Augmented Generation) Pipeline

```
┌──────────────────────────────────────────────────────────────────┐
│         RAG Pipeline with Redis Vector Search                     │
└──────────────────────────────────────────────────────────────────┘

User Query: "What is Redis AI?"
      │
      ▼
┌─────────────────────┐
│  1. Embed Query     │
│  Using embedding    │
│  model (e.g., ada)  │
└──────┬──────────────┘
       │
       │ Query Vector: [0.1, 0.3, ...]
       ▼
┌─────────────────────────────────────┐
│  2. Vector Similarity Search        │
│                                     │
│  Redis Command:                     │
│  FT.SEARCH idx                      │
│    "*=>[KNN 5 @embedding $vec]"     │
│    PARAMS 2 vec {query_vector}      │
│    RETURN 3 content score           │
│                                     │
│  Index Structure:                   │
│  doc:{id} → {                       │
│    content: "...",                  │
│    embedding: [float32],            │
│    metadata: {...}                  │
│  }                                  │
└──────┬──────────────────────────────┘
       │
       │ Top 5 Similar Documents
       ▼
┌─────────────────────┐
│  3. Build Context   │
│                     │
│  Context = concat(  │
│    doc1.content,    │
│    doc2.content,    │
│    ...              │
│  )                  │
└──────┬──────────────┘
       │
       │ Enriched Context
       ▼
┌─────────────────────────────┐
│  4. Build Augmented Prompt  │
│                             │
│  Prompt = f"""              │
│  Context: {context}         │
│                             │
│  Question: {user_query}     │
│                             │
│  Answer:                    │
│  """                        │
└──────┬──────────────────────┘
       │
       │ Augmented Prompt
       ▼
┌─────────────────────┐
│  5. LLM Generation  │
│                     │
│  Check cache first: │
│  llm:cache:{hash}   │
│                     │
│  If miss, call LLM  │
│  and cache result   │
└──────┬──────────────┘
       │
       │ Final Response
       ▼
┌─────────────────────┐
│  6. Return Result   │
│  with citations     │
└─────────────────────┘

Performance:
├─► Vector Search: 1-5ms for millions of docs
├─► Context Building: <1ms
├─► LLM Call (cached): <1ms
└─► LLM Call (uncached): 500-2000ms
```

## Real-Time Inference Pipeline

```
┌──────────────────────────────────────────────────────────────────┐
│           Real-Time ML Model Inference with RedisAI               │
└──────────────────────────────────────────────────────────────────┘

Data Sources                   Redis Streams              Processing
┌──────────┐                                             
│  IoT     │─┐                                           
│ Devices  │ │              ┌─────────────────┐          
└──────────┘ │              │ Redis Stream    │          
             ├─────────────►│ "events:sensor" │          
┌──────────┐ │              │                 │          
│  Web     │ │              │ Entry Format:   │          
│  APIs    │─┤              │ {               │          
└──────────┘ │              │   id: "123-0",  │          
             │              │   data: {...}   │          
┌──────────┐ │              │ }               │          
│  Mobile  │ │              └────────┬────────┘          
│  Apps    │─┘                       │                   
└──────────┘                         │                   
                                     │ XREAD              
                                     ▼                    
                            ┌─────────────────┐           
                            │  Consumer App   │           
                            │  (Python/Node)  │           
                            └────────┬────────┘           
                                     │                    
                                     │ 1. Read Stream     
                                     │ 2. Preprocess      
                                     ▼                    
                            ┌─────────────────────┐       
                            │  RedisAI Pipeline   │       
                            │                     │       
                            │  AI.DAGRUN          │       
                            │    |> TENSORSET     │       
                            │    |> MODELEXECUTE  │       
                            │    |> TENSORGET     │       
                            └────────┬────────────┘       
                                     │                    
                                     │ Inference Result   
                                     ▼                    
                            ┌─────────────────┐           
                            │  Post-Process   │           
                            │  & Store        │           
                            │                 │           
                            │  SET result:123 │           
                            │  PUBLISH alerts │           
                            └────────┬────────┘           
                                     │                    
                   ┌─────────────────┼─────────────────┐  
                   ▼                 ▼                 ▼  
           ┌──────────┐      ┌──────────┐     ┌──────────┐
           │Dashboard │      │  Alerts  │     │  Storage │
           │   UI     │      │  System  │     │   Layer  │
           └──────────┘      └──────────┘     └──────────┘

Throughput: 10,000+ inferences/second
Latency: Single-digit milliseconds (p99)
```

## Data Flow Patterns

### Pattern: Request-Response with Caching

```
Request → Cache Check → [HIT] → Immediate Response
                      ↓
                    [MISS]
                      ↓
                 Compute/Fetch
                      ↓
                 Store in Cache ──→ Response
                      ↑
                  Set TTL
```

### Pattern: Pub/Sub Event Distribution

```
Event Source
     │
     ▼
PUBLISH channel
     │
     └─────┬─────┬─────┬─────
           ▼     ▼     ▼     ▼
        Sub1  Sub2  Sub3  Sub4
         │     │     │     │
         ▼     ▼     ▼     ▼
      Action Action Action Action
```

### Pattern: Stream Processing Pipeline

```
Producer → XADD stream
                │
                ▼
         [Stream Buffer]
                │
     ┌──────────┴──────────┐
     ▼                     ▼
Consumer Group 1    Consumer Group 2
     │                     │
     ▼                     ▼
  Process A            Process B
     │                     │
     └──────────┬──────────┘
                ▼
         Downstream System
```

## Integration Complexity Matrix

```
┌───────────────────────────────────────────────────────────────┐
│  Integration Complexity vs. Value Matrix                      │
└───────────────────────────────────────────────────────────────┘

High Value
    │
    │   ┌────────────────┐
    │   │  RAG Pipeline  │ ◄── Optimal
    │   │  (Vector + LLM)│
    │   └────────────────┘
    │        
    │   ┌──────────────┐     ┌─────────────────┐
    │   │ Agent State  │     │  Multi-Model    │
    │   │ Management   │     │  Orchestration  │
    │   └──────────────┘     └─────────────────┘
    │   
    │   ┌──────────────┐
    │   │ LLM Response │ ◄── Quick Win
    │   │   Caching    │
    │   └──────────────┘
    │
Low Value
    │
    └────────────────────────────────────────────►
        Low Complexity              High Complexity

Legend:
• Quick Win: High value, low complexity - implement first
• Optimal: High value, medium complexity - core features
• Advanced: High value, high complexity - after foundations
```

## Technology Stack Layers

```
┌──────────────────────────────────────────────────────────┐
│                    Application Layer                      │
│  Web Apps • Mobile Apps • APIs • Microservices          │
└────────────────────┬─────────────────────────────────────┘
                     │
┌────────────────────┴─────────────────────────────────────┐
│                  AI/ML Framework Layer                    │
│  LangChain • AutoGPT • LlamaIndex • HuggingFace         │
└────────────────────┬─────────────────────────────────────┘
                     │
┌────────────────────┴─────────────────────────────────────┐
│                    Redis Integration Layer                │
│                                                           │
│  ┌───────────┐  ┌───────────┐  ┌───────────┐           │
│  │  RedisAI  │  │RediSearch │  │Core Redis │           │
│  │           │  │           │  │           │           │
│  │ • Models  │  │ • Vectors │  │ • Cache   │           │
│  │ • Tensors │  │ • Search  │  │ • State   │           │
│  └───────────┘  └───────────┘  │ • Pub/Sub │           │
│                                 │ • Streams │           │
│                                 └───────────┘           │
└────────────────────┬─────────────────────────────────────┘
                     │
┌────────────────────┴─────────────────────────────────────┐
│                   Infrastructure Layer                    │
│  Redis Cluster • Redis Sentinel • Redis Enterprise       │
└───────────────────────────────────────────────────────────┘
```

## Deployment Topologies

### Single Instance (Development)

```
┌─────────────────────┐
│   Application       │
└──────────┬──────────┘
           │
┌──────────▼──────────┐
│   Redis Instance    │
│   - All modules     │
│   - localhost:6379  │
└─────────────────────┘
```

### High Availability (Production)

```
        Load Balancer
              │
    ┌─────────┼─────────┐
    │         │         │
    ▼         ▼         ▼
  App1      App2      App3
    │         │         │
    └─────────┼─────────┘
              │
    ┌─────────▼─────────┐
    │  Redis Sentinel   │
    │   (Monitoring)    │
    └─────────┬─────────┘
              │
    ┌─────────┼─────────┐
    ▼         ▼         ▼
 Master    Replica   Replica
 (Write)   (Read)    (Read)
```

### Cluster (Massive Scale)

```
        Application Tier
    ┌─────────┬─────────┐
    │         │         │
    ▼         ▼         ▼
 App1      App2    ...  AppN
    │         │         │
    └─────────┼─────────┘
              │
    ┌─────────▼─────────────────┐
    │    Redis Cluster          │
    │                           │
    │  ┌─────┐  ┌─────┐  ┌────┐│
    │  │Shard│  │Shard│  │... ││
    │  │  1  │  │  2  │  │  N ││
    │  └──┬──┘  └──┬──┘  └─┬──┘│
    │     │        │       │   │
    │  ┌──▼──┐  ┌─▼───┐  ┌▼──┐│
    │  │Rep 1│  │Rep 2│  │...││
    │  └─────┘  └─────┘  └───┘│
    └───────────────────────────┘
    
    Features:
    - Horizontal scaling
    - Automatic sharding
    - 1000+ nodes supported
    - Multi-region deployment
```

## Related Documentation

- [[redis-ai-integration.md]] - Detailed integration guide
- [[redis-ai-quick-reference.md]] - Quick reference guide
- [[SKYNET.md]] - Technology research overview

---

*Architecture Diagrams*
*Last Updated: 2025-11-17*
*ASCII art diagrams for terminal/markdown viewing*

<!-- 9E2A5C16 -->
