---
title: "Redis AI Integration with AI/LLM/Agent Systems"
tags:
  - redis
  - ai
  - llm
  - agent
  - integration
  - architecture
  - machine-learning
state: Research
type: technical-documentation
category: AI-Infrastructure
---

# Redis AI Integration with AI/LLM/Agent Systems

## Overview

Redis AI (now part of RedisAI) is a Redis module that enables AI model serving and execution directly within Redis. This document explores what can be connected to AI/LLM/agent systems from Redis AI, providing a comprehensive guide to integration patterns, architectures, and use cases.

## Table of Contents

1. [What Can Be Connected](#what-can-be-connected)
2. [Core Integration Components](#core-integration-components)
3. [Architecture Patterns](#architecture-patterns)
4. [Implementation Examples](#implementation-examples)
5. [Best Practices](#best-practices)
6. [Use Cases](#use-cases)

## What Can Be Connected

Redis AI serves as a powerful integration hub that can connect various AI/LLM/agent components:

### 1. Machine Learning Models

#### Deep Learning Frameworks
- **TensorFlow** models (.pb format)
- **PyTorch** models (.pt format)
- **ONNX** (Open Neural Network Exchange) models
- **TensorFlow Lite** models for edge deployment

#### Model Types
- Neural networks (CNN, RNN, LSTM, Transformers)
- Computer vision models
- Natural language processing models
- Time-series prediction models
- Reinforcement learning models

### 2. Large Language Models (LLMs)

#### LLM Integration Points
- **Embedding Models**: Store and retrieve vector embeddings
  - OpenAI embeddings
  - Sentence transformers
  - Custom embedding models
  
- **Token Management**: Cache tokenized inputs/outputs
  - Token counting and tracking
  - Context window management
  - Token-based rate limiting

- **Prompt Templates**: Store and manage prompts
  - Template versioning
  - A/B testing of prompts
  - Dynamic prompt generation

- **Response Caching**: Cache LLM responses
  - Semantic caching
  - Exact match caching
  - TTL-based cache invalidation

### 3. AI Agent Systems

#### Agent Components
- **Agent State Management**
  - Session state persistence
  - Agent memory (short-term and long-term)
  - Conversation history
  - Context preservation

- **Multi-Agent Communication**
  - Inter-agent messaging via Redis Pub/Sub
  - Shared knowledge bases
  - Coordination and orchestration
  - Task queues and job distribution

- **Agent Tools and Functions**
  - Tool result caching
  - Function call history
  - API response caching
  - Rate limiting and throttling

### 4. Vector Databases and Semantic Search

#### Vector Operations
- **Vector Storage**: Store embeddings in Redis
  - Dense vectors from LLMs
  - Sparse vectors for hybrid search
  - Multi-modal embeddings

- **Similarity Search**
  - K-nearest neighbors (KNN)
  - Approximate nearest neighbors (ANN)
  - Semantic search capabilities
  - Vector indexing with RediSearch

- **RAG (Retrieval-Augmented Generation)**
  - Document embedding storage
  - Context retrieval for LLMs
  - Hybrid search (vector + full-text)
  - Metadata filtering

### 5. Real-Time Data Streams

#### Stream Processing
- **Redis Streams** for data ingestion
  - Real-time event processing
  - Time-series data for AI models
  - Feature streams for online learning
  - Model input/output logging

- **Pub/Sub Integration**
  - Model inference triggers
  - Result broadcasting
  - Multi-consumer patterns
  - Event-driven AI pipelines

### 6. Application Backends

#### Backend Integration
- **API Gateways**
  - Request/response caching
  - Rate limiting
  - Load balancing
  - Authentication tokens

- **Microservices**
  - Service discovery
  - Configuration management
  - Inter-service communication
  - Distributed tracing

- **Web Applications**
  - Session management
  - User preferences
  - Personalization data
  - A/B testing configurations

### 7. Data Processing Pipelines

#### Pipeline Components
- **ETL (Extract, Transform, Load)**
  - Data preprocessing caching
  - Feature engineering results
  - Transformation rules
  - Data validation states

- **Model Training Infrastructure**
  - Training data sampling
  - Hyperparameter storage
  - Experiment tracking
  - Model versioning

- **Inference Pipelines**
  - Pre-processing cache
  - Post-processing cache
  - Batch inference queues
  - Result aggregation

### 8. Monitoring and Observability

#### Monitoring Systems
- **Metrics Collection**
  - Model performance metrics
  - Inference latency tracking
  - Resource utilization
  - Error rates and logging

- **Alerting Systems**
  - Threshold-based alerts
  - Anomaly detection triggers
  - Model drift detection
  - Performance degradation alerts

## Core Integration Components

### RedisAI Capabilities

```python
# Core RedisAI operations that enable integrations

# 1. Model Management
# Store a machine learning model in Redis for later inference
AI.MODELSTORE <key> <backend> <device> <tag> <model_blob>
# Parameters:
#   - key: Unique identifier for the model (e.g., "sentiment_model")
#   - backend: Framework type (TORCH, TF, TFLITE, ONNX)
#   - device: Execution device (CPU, GPU, GPU:0, GPU:1)
#   - tag: Version tag for model tracking
#   - model_blob: Binary model data

# Retrieve model metadata or binary blob
AI.MODELGET <key> [META | BLOB]
# Returns model configuration or full binary data

# Remove a model from Redis
AI.MODELDEL <key>

# Execute inference on a stored model
AI.MODELEXECUTE <key> INPUTS <input_keys...> OUTPUTS <output_keys...>
# This is the core inference operation that enables AI/LLM/agent integrations
# Parameters:
#   - key: The model identifier stored in Redis
#   - INPUTS: One or more tensor keys containing input data
#   - OUTPUTS: One or more keys where results will be stored
# Example: AI.MODELEXECUTE my_model INPUTS input_tensor OUTPUTS prediction
# 
# This command executes the model inference operation and is fundamental to:
#   - Real-time AI/ML predictions in applications
#   - Low-latency model serving without external dependencies
#   - Integration with LLM preprocessing/postprocessing pipelines
#   - Agent decision-making based on ML model outputs
#   - Multi-step inference pipelines using DAG operations
#
# Performance characteristics:
#   - Latency: 1-100ms depending on model complexity
#   - Throughput: Can handle 10,000+ inferences/second
#   - Memory: Models stay in memory for fast execution
#   - Scalability: Horizontal scaling with Redis Cluster

# 2. Tensor Operations
AI.TENSORSET <key> <type> <shape...> [BLOB <data> | VALUES <val...>]
AI.TENSORGET <key> [META | VALUES | BLOB]

# 3. Script Execution (TorchScript)
AI.SCRIPTSTORE <key> <device> <script>
AI.SCRIPTEXECUTE <key> <function> INPUTS <input_keys...> OUTPUTS <output_keys...>

# 4. DAG (Directed Acyclic Graph) for complex pipelines
AI.DAGRUN [LOAD <n> <key...>] [PERSIST <n> <key...>] |> <command> |> ...
```

### Redis Data Structures for AI

```python
# Data structures commonly used in AI integrations

# 1. Strings - Simple key-value storage
# Use: Model predictions, cached responses, configuration
SET model:prediction:user123 "positive"
GET model:prediction:user123

# 2. Hashes - Structured data
# Use: Agent state, user profiles, model metadata
HSET agent:state:session1 "context" "shopping" "turn" "5"
HGETALL agent:state:session1

# 3. Lists - Ordered collections
# Use: Conversation history, task queues
LPUSH conversation:user123 "User: Hello"
LPUSH conversation:user123 "Agent: Hi, how can I help?"
LRANGE conversation:user123 0 -1

# 4. Sets - Unique collections
# Use: Tags, categories, user segments
SADD user:segments:123 "premium" "active" "tech-savvy"
SMEMBERS user:segments:123

# 5. Sorted Sets - Ranked data
# Use: Recommendation scores, priority queues
ZADD recommendations:user123 0.95 "item1" 0.87 "item2"
ZRANGE recommendations:user123 0 -1 WITHSCORES

# 6. Streams - Event logs
# Use: Model input/output logging, audit trails
XADD inference:log * model "gpt-4" input "hello" output "Hi there"
XREAD STREAMS inference:log 0

# 7. JSON - Complex nested data (RedisJSON)
# Use: Agent memory, complex configurations
JSON.SET agent:memory:session1 $ '{"facts": [], "preferences": {}}'
JSON.GET agent:memory:session1
```

## Architecture Patterns

### Pattern 1: LLM Response Caching Architecture

```
┌─────────────┐
│   Client    │
└──────┬──────┘
       │
       ▼
┌─────────────────────────────────────┐
│     API Gateway / Load Balancer     │
└──────────────┬──────────────────────┘
               │
               ▼
       ┌───────────────┐
       │  Check Cache  │◄─────┐
       │  (Redis)      │      │
       └───────┬───────┘      │
               │              │
        ┌──────▼──────┐       │
        │Cache Hit?   │       │
        └──┬───────┬──┘       │
           │Yes    │No        │
           │       │          │
           │       ▼          │
           │   ┌─────────┐   │
           │   │   LLM   │   │
           │   │ Service │   │
           │   └────┬────┘   │
           │        │        │
           │        ├────────┘
           │        │Store Result
           │        │
           ▼        ▼
       ┌──────────────┐
       │   Response   │
       └──────────────┘
```

### Pattern 2: Multi-Agent System with Redis

```
┌──────────────────────────────────────────────────────┐
│                    Redis Cluster                      │
│                                                        │
│  ┌──────────────┐  ┌──────────────┐  ┌────────────┐ │
│  │ Agent States │  │ Message Queue│  │ Shared KB  │ │
│  └──────────────┘  └──────────────┘  └────────────┘ │
└───────────┬──────────────┬──────────────┬────────────┘
            │              │              │
    ┌───────┴───────┬──────┴──────┬───────┴────────┐
    │               │             │                │
┌───▼────┐     ┌────▼───┐    ┌────▼───┐      ┌────▼───┐
│Agent 1 │     │Agent 2 │    │Agent 3 │      │Agent N │
│(Planner)│     │(Executor)   │(Critic)│      │(Custom)│
└────────┘     └────────┘    └────────┘      └────────┘
```

### Pattern 3: RAG (Retrieval-Augmented Generation) Pipeline

```
┌─────────────┐
│   Query     │
└──────┬──────┘
       │
       ▼
┌──────────────────┐
│ Embedding Model  │
│   (via Redis)    │
└──────┬───────────┘
       │
       ▼
┌────────────────────────────┐
│ Vector Search (RediSearch) │
│   - Find similar docs      │
│   - Retrieve context       │
└──────┬─────────────────────┘
       │
       ▼
┌──────────────────┐
│  Build Prompt    │
│  Query + Context │
└──────┬───────────┘
       │
       ▼
┌──────────────────┐
│   LLM Service    │
│  (e.g., GPT-4)   │
└──────┬───────────┘
       │
       ▼
┌──────────────────┐
│   Response       │
│   (cached)       │
└──────────────────┘
```

### Pattern 4: Real-Time Model Inference Pipeline

```
┌─────────────────┐
│  Data Source    │
│ (Streams/Pub/Sub)│
└────────┬────────┘
         │
         ▼
┌─────────────────────┐
│  Feature Engineering│
│   (Redis + Script)  │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│   Model Inference   │
│    (RedisAI)        │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  Post-Processing    │
│  & Result Storage   │
└────────┬────────────┘
         │
         ▼
┌─────────────────────┐
│  Consumer Services  │
│ (Dashboards/APIs)   │
└─────────────────────┘
```

## Implementation Examples

### Example 1: LLM Response Caching with Semantic Search

```python
import redis
import hashlib
import json
from typing import Optional

class LLMCache:
    def __init__(self, redis_client: redis.Redis):
        self.redis = redis_client
        self.ttl = 3600  # 1 hour
    
    def _generate_cache_key(self, prompt: str, model: str, params: dict) -> str:
        """Generate a unique cache key based on prompt and parameters"""
        cache_input = f"{model}:{prompt}:{json.dumps(params, sort_keys=True)}"
        return f"llm:cache:{hashlib.sha256(cache_input.encode()).hexdigest()}"
    
    def get(self, prompt: str, model: str, params: dict) -> Optional[str]:
        """Retrieve cached response"""
        key = self._generate_cache_key(prompt, model, params)
        cached = self.redis.get(key)
        if cached:
            return cached.decode('utf-8')
        return None
    
    def set(self, prompt: str, model: str, params: dict, response: str):
        """Store response in cache"""
        key = self._generate_cache_key(prompt, model, params)
        self.redis.setex(key, self.ttl, response)
    
    def get_stats(self) -> dict:
        """Get cache statistics"""
        total_keys = len(self.redis.keys("llm:cache:*"))
        return {
            "total_cached_responses": total_keys,
            "ttl": self.ttl
        }


# Usage
r = redis.Redis(host='localhost', port=6379, decode_responses=False)
cache = LLMCache(r)

# Check cache before calling LLM
prompt = "Explain quantum computing"
model = "gpt-4"
params = {"temperature": 0.7, "max_tokens": 500}

cached_response = cache.get(prompt, model, params)
if cached_response:
    print(f"Cache hit! Response: {cached_response}")
else:
    # Call actual LLM (pseudo-code)
    response = call_llm(prompt, model, params)
    cache.set(prompt, model, params, response)
    print(f"Cache miss. Stored new response: {response}")
```

### Example 2: Agent State Management

```python
import redis
import json
from typing import Dict, Any, List

class AgentStateManager:
    def __init__(self, redis_client: redis.Redis):
        self.redis = redis_client
    
    def save_state(self, agent_id: str, session_id: str, state: Dict[str, Any]):
        """Save agent state to Redis"""
        key = f"agent:{agent_id}:session:{session_id}:state"
        self.redis.hset(key, mapping={
            "context": json.dumps(state.get("context", {})),
            "memory": json.dumps(state.get("memory", [])),
            "turn_count": state.get("turn_count", 0),
            "last_action": state.get("last_action", ""),
            "timestamp": state.get("timestamp", "")
        })
        self.redis.expire(key, 86400)  # 24 hours
    
    def load_state(self, agent_id: str, session_id: str) -> Dict[str, Any]:
        """Load agent state from Redis"""
        key = f"agent:{agent_id}:session:{session_id}:state"
        state_data = self.redis.hgetall(key)
        
        if not state_data:
            return {}
        
        return {
            "context": json.loads(state_data.get(b"context", b"{}")),
            "memory": json.loads(state_data.get(b"memory", b"[]")),
            "turn_count": int(state_data.get(b"turn_count", 0)),
            "last_action": state_data.get(b"last_action", b"").decode(),
            "timestamp": state_data.get(b"timestamp", b"").decode()
        }
    
    def add_to_memory(self, agent_id: str, session_id: str, memory_item: str):
        """Add item to agent's conversation memory"""
        key = f"agent:{agent_id}:session:{session_id}:conversation"
        self.redis.lpush(key, memory_item)
        self.redis.ltrim(key, 0, 99)  # Keep last 100 items
        self.redis.expire(key, 86400)
    
    def get_conversation_history(self, agent_id: str, session_id: str, limit: int = 10) -> List[str]:
        """Retrieve conversation history"""
        key = f"agent:{agent_id}:session:{session_id}:conversation"
        history = self.redis.lrange(key, 0, limit - 1)
        return [item.decode() for item in history]


# Usage
r = redis.Redis(host='localhost', port=6379)
agent_manager = AgentStateManager(r)

# Save agent state
agent_manager.save_state(
    agent_id="assistant-001",
    session_id="user-session-123",
    state={
        "context": {"topic": "technology", "mood": "helpful"},
        "memory": ["Previous discussion about AI"],
        "turn_count": 5,
        "last_action": "provided_information",
        "timestamp": "2025-11-17T13:00:00Z"
    }
)

# Load agent state
state = agent_manager.load_state("assistant-001", "user-session-123")
print(f"Loaded state: {state}")

# Add to conversation memory
agent_manager.add_to_memory("assistant-001", "user-session-123", "User: Tell me about Redis")
agent_manager.add_to_memory("assistant-001", "user-session-123", "Agent: Redis is an in-memory database...")

# Get conversation history
history = agent_manager.get_conversation_history("assistant-001", "user-session-123", limit=5)
print(f"Conversation history: {history}")
```

### Example 3: Vector Similarity Search for RAG

```python
import redis
import numpy as np
from redis.commands.search.field import VectorField, TextField, NumericField
from redis.commands.search.indexDefinition import IndexDefinition, IndexType
from redis.commands.search.query import Query

class VectorRAG:
    def __init__(self, redis_client: redis.Redis):
        self.redis = redis_client
        self.index_name = "doc_embeddings_idx"
        self._create_index()
    
    def _create_index(self):
        """Create a vector search index"""
        try:
            self.redis.ft(self.index_name).info()
            print(f"Index {self.index_name} already exists")
        except:
            schema = (
                TextField("$.content", as_name="content"),
                TextField("$.metadata", as_name="metadata"),
                VectorField(
                    "$.embedding",
                    "FLAT",
                    {
                        "TYPE": "FLOAT32",
                        "DIM": 1536,  # OpenAI ada-002 dimension
                        "DISTANCE_METRIC": "COSINE"
                    },
                    as_name="embedding"
                )
            )
            
            definition = IndexDefinition(prefix=["doc:"], index_type=IndexType.JSON)
            self.redis.ft(self.index_name).create_index(
                fields=schema,
                definition=definition
            )
            print(f"Created index {self.index_name}")
    
    def add_document(self, doc_id: str, content: str, embedding: List[float], metadata: dict = None):
        """Add a document with its embedding"""
        doc_key = f"doc:{doc_id}"
        doc_data = {
            "content": content,
            "embedding": embedding,
            "metadata": metadata or {}
        }
        self.redis.json().set(doc_key, "$", doc_data)
    
    def search_similar(self, query_embedding: List[float], top_k: int = 5) -> List[Dict]:
        """Search for similar documents using vector similarity"""
        query_vector = np.array(query_embedding, dtype=np.float32).tobytes()
        
        q = (
            Query(f"*=>[KNN {top_k} @embedding $vec AS score]")
            .sort_by("score")
            .return_fields("content", "metadata", "score")
            .dialect(2)
        )
        
        results = self.redis.ft(self.index_name).search(
            q,
            query_params={"vec": query_vector}
        )
        
        documents = []
        for doc in results.docs:
            documents.append({
                "content": doc.content,
                "metadata": doc.metadata,
                "score": float(doc.score)
            })
        
        return documents
    
    def rag_query(self, query: str, query_embedding: List[float], 
                  llm_function, top_k: int = 3) -> str:
        """Perform RAG: retrieve context and generate response"""
        # 1. Retrieve relevant documents
        relevant_docs = self.search_similar(query_embedding, top_k)
        
        # 2. Build context from retrieved documents
        context = "\n\n".join([doc["content"] for doc in relevant_docs])
        
        # 3. Build prompt with context
        prompt = f"""Context information:
{context}

Question: {query}

Answer based on the context provided:"""
        
        # 4. Generate response using LLM
        response = llm_function(prompt)
        
        return response


# Usage example (pseudo-code)
r = redis.Redis(host='localhost', port=6379, decode_responses=True)
rag = VectorRAG(r)

# Add documents (you would get embeddings from an embedding model)
def get_embedding(text):
    # Call embedding model (e.g., OpenAI ada-002)
    # This is pseudo-code
    return [0.1] * 1536  # Replace with actual embedding

doc1_embedding = get_embedding("Redis is an in-memory database")
rag.add_document(
    doc_id="1",
    content="Redis is an in-memory database that supports various data structures",
    embedding=doc1_embedding,
    metadata={"source": "redis_docs", "category": "database"}
)

# Query with RAG
query = "What is Redis?"
query_embedding = get_embedding(query)

def mock_llm(prompt):
    return "Redis is an in-memory database..." # Replace with actual LLM call

response = rag.rag_query(query, query_embedding, mock_llm, top_k=3)
print(f"RAG Response: {response}")
```

### Example 4: Multi-Agent Coordination with Pub/Sub

```python
import redis
import json
import threading
from typing import Callable, Dict

class AgentCoordinator:
    def __init__(self, redis_client: redis.Redis, agent_id: str):
        self.redis = redis_client
        self.agent_id = agent_id
        self.pubsub = self.redis.pubsub()
        self.message_handlers: Dict[str, Callable] = {}
    
    def subscribe_to_channel(self, channel: str, handler: Callable):
        """Subscribe to a communication channel"""
        self.pubsub.subscribe(channel)
        self.message_handlers[channel] = handler
    
    def send_message(self, channel: str, message: dict):
        """Send a message to a channel"""
        message_data = {
            "from": self.agent_id,
            "timestamp": "2025-11-17T13:00:00Z",  # Use actual timestamp
            "payload": message
        }
        self.redis.publish(channel, json.dumps(message_data))
    
    def listen(self):
        """Listen for messages (blocking)"""
        for message in self.pubsub.listen():
            if message['type'] == 'message':
                channel = message['channel'].decode()
                data = json.loads(message['data'].decode())
                
                # Don't process own messages
                if data.get('from') == self.agent_id:
                    continue
                
                # Call the appropriate handler
                if channel in self.message_handlers:
                    self.message_handlers[channel](data)
    
    def start_listening(self):
        """Start listening in a separate thread"""
        listener_thread = threading.Thread(target=self.listen, daemon=True)
        listener_thread.start()
    
    def broadcast_task(self, task_type: str, task_data: dict):
        """Broadcast a task to all agents"""
        self.send_message("agent:tasks", {
            "task_type": task_type,
            "task_data": task_data
        })
    
    def request_assistance(self, problem: str, context: dict):
        """Request help from other agents"""
        self.send_message("agent:assistance", {
            "problem": problem,
            "context": context,
            "requesting_agent": self.agent_id
        })
    
    def share_knowledge(self, knowledge_type: str, knowledge: dict):
        """Share knowledge with other agents"""
        knowledge_key = f"knowledge:{knowledge_type}:{self.agent_id}"
        self.redis.setex(knowledge_key, 3600, json.dumps(knowledge))
        
        # Notify other agents
        self.send_message("agent:knowledge", {
            "knowledge_type": knowledge_type,
            "knowledge_key": knowledge_key
        })


# Usage example
r = redis.Redis(host='localhost', port=6379)

# Agent 1: Planning Agent
planner_agent = AgentCoordinator(r, "planner-001")

def handle_task_completion(message):
    print(f"Planner received task completion: {message}")

planner_agent.subscribe_to_channel("agent:task_completion", handle_task_completion)
planner_agent.start_listening()

# Broadcast a new task
planner_agent.broadcast_task("analyze_data", {
    "dataset": "user_behavior_2025",
    "priority": "high"
})

# Agent 2: Executor Agent
executor_agent = AgentCoordinator(r, "executor-001")

def handle_new_task(message):
    print(f"Executor received task: {message}")
    # Process the task...
    # When done, notify completion
    executor_agent.send_message("agent:task_completion", {
        "task_type": message['payload']['task_type'],
        "status": "completed",
        "result": {"analyzed": True}
    })

executor_agent.subscribe_to_channel("agent:tasks", handle_new_task)
executor_agent.start_listening()

# Agent 3: Knowledge Agent
knowledge_agent = AgentCoordinator(r, "knowledge-001")
knowledge_agent.share_knowledge("best_practices", {
    "domain": "data_analysis",
    "tips": ["validate data", "check for outliers"]
})
```

### Example 5: Model Inference with RedisAI

```python
import redis
import numpy as np
from redisai import Client as RedisAI

class ModelInferenceService:
    def __init__(self, redis_host='localhost', redis_port=6379):
        self.client = RedisAI(host=redis_host, port=redis_port)
    
    def load_model(self, model_key: str, model_path: str, backend='TORCH', device='CPU'):
        """Load a model into RedisAI"""
        with open(model_path, 'rb') as f:
            model_blob = f.read()
        
        self.client.modelstore(
            model_key,
            backend,
            device,
            model_blob,
            tag='v1.0'
        )
        print(f"Model {model_key} loaded successfully")
    
    def set_tensor(self, tensor_key: str, data: np.ndarray):
        """Store a tensor in Redis"""
        self.client.tensorset(
            tensor_key,
            data,
            dtype=str(data.dtype)
        )
    
    def run_inference(self, model_key: str, input_tensor_key: str, output_tensor_key: str):
        """Run model inference"""
        self.client.modelexecute(
            model_key,
            inputs=[input_tensor_key],
            outputs=[output_tensor_key]
        )
    
    def get_tensor(self, tensor_key: str) -> np.ndarray:
        """Retrieve a tensor from Redis"""
        return self.client.tensorget(tensor_key)
    
    def run_inference_pipeline(self, model_key: str, input_data: np.ndarray) -> np.ndarray:
        """Complete inference pipeline"""
        # Generate unique keys for this inference
        import uuid
        request_id = str(uuid.uuid4())
        input_key = f"input:{request_id}"
        output_key = f"output:{request_id}"
        
        try:
            # 1. Store input tensor
            self.set_tensor(input_key, input_data)
            
            # 2. Run inference
            self.run_inference(model_key, input_key, output_key)
            
            # 3. Retrieve output
            result = self.get_tensor(output_key)
            
            return result
        finally:
            # Cleanup temporary tensors
            self.client.delete(input_key)
            self.client.delete(output_key)


# Usage example
service = ModelInferenceService()

# Load a model (e.g., PyTorch model)
# service.load_model('sentiment_model', 'path/to/model.pt', backend='TORCH')

# Run inference
input_data = np.array([[0.5, 0.3, 0.2]], dtype=np.float32)
result = service.run_inference_pipeline('sentiment_model', input_data)
print(f"Model output: {result}")
```

## Best Practices

### 1. Caching Strategy

#### When to Cache
- **High-frequency queries**: Cache responses for common questions
- **Expensive operations**: Cache results of costly LLM calls
- **Static content**: Cache rarely-changing information
- **Rate-limited APIs**: Reduce API calls to stay within limits

#### Cache Invalidation
```python
# Time-based expiration
redis.setex("cache:key", ttl=3600, value="data")

# Manual invalidation on data updates
def update_data(key, new_value):
    redis.set(f"data:{key}", new_value)
    redis.delete(f"cache:{key}")  # Invalidate cache

# Version-based caching
def get_cached_with_version(key, version):
    versioned_key = f"cache:{key}:v{version}"
    return redis.get(versioned_key)
```

### 2. Connection Management

```python
import redis
from redis.connection import ConnectionPool

# Use connection pooling for better performance
pool = ConnectionPool(
    host='localhost',
    port=6379,
    max_connections=50,
    decode_responses=True
)

redis_client = redis.Redis(connection_pool=pool)

# Use Redis cluster for high availability
from redis.cluster import RedisCluster

cluster_nodes = [
    {"host": "node1", "port": 6379},
    {"host": "node2", "port": 6379},
    {"host": "node3", "port": 6379}
]

redis_cluster = RedisCluster(startup_nodes=cluster_nodes)
```

### 3. Error Handling and Resilience

```python
import redis
from redis.exceptions import RedisError, ConnectionError
import time

def resilient_redis_operation(func, max_retries=3, backoff=1):
    """Wrapper for resilient Redis operations"""
    for attempt in range(max_retries):
        try:
            return func()
        except ConnectionError as e:
            if attempt == max_retries - 1:
                raise
            time.sleep(backoff * (2 ** attempt))
        except RedisError as e:
            # Log error and handle appropriately
            print(f"Redis error: {e}")
            raise

# Usage
def get_data():
    return redis_client.get("some:key")

result = resilient_redis_operation(get_data)
```

### 4. Security Considerations

```python
# 1. Use ACL (Access Control Lists)
# Configure in redis.conf or via command:
"""
ACL SETUSER llm_service on >secure_password ~llm:* +get +set +del
"""

# 2. Enable TLS/SSL
import redis

redis_client = redis.Redis(
    host='redis.example.com',
    port=6380,
    ssl=True,
    ssl_cert_reqs='required',
    ssl_ca_certs='/path/to/ca.crt'
)

# 3. Sensitive data handling
from cryptography.fernet import Fernet

class SecureCache:
    def __init__(self, redis_client, encryption_key):
        self.redis = redis_client
        self.cipher = Fernet(encryption_key)
    
    def set_secure(self, key, value):
        encrypted = self.cipher.encrypt(value.encode())
        self.redis.set(key, encrypted)
    
    def get_secure(self, key):
        encrypted = self.redis.get(key)
        if encrypted:
            return self.cipher.decrypt(encrypted).decode()
        return None
```

### 5. Performance Optimization

```python
# 1. Use pipelining for batch operations
pipe = redis_client.pipeline()
for i in range(1000):
    pipe.set(f"key:{i}", f"value:{i}")
pipe.execute()

# 2. Use Lua scripts for atomic operations
lua_script = """
local key = KEYS[1]
local value = redis.call('GET', key)
if value then
    redis.call('SET', key, tonumber(value) + 1)
    return tonumber(value) + 1
else
    redis.call('SET', key, 1)
    return 1
end
"""

increment_script = redis_client.register_script(lua_script)
result = increment_script(keys=['counter:requests'])

# 3. Memory optimization
redis_client.config_set('maxmemory-policy', 'allkeys-lru')
redis_client.config_set('maxmemory', '2gb')
```

## Use Cases

### Use Case 1: Conversational AI with Memory

**Scenario**: Building a chatbot that remembers conversation context across sessions.

**Components**:
- Redis for conversation history storage
- LLM for response generation
- Vector search for semantic memory retrieval

**Benefits**:
- Fast context retrieval (< 1ms)
- Persistent memory across sessions
- Scalable to millions of users

### Use Case 2: Real-Time Recommendation System

**Scenario**: E-commerce platform providing personalized product recommendations.

**Components**:
- RedisAI for model inference
- Sorted sets for ranking
- Vectors for similarity matching

**Benefits**:
- Sub-millisecond inference latency
- Real-time personalization
- A/B testing capabilities

### Use Case 3: Multi-Agent Customer Service

**Scenario**: Distributed agent system handling customer inquiries.

**Components**:
- Redis Pub/Sub for agent communication
- Shared knowledge base in Redis
- Task queue for work distribution

**Benefits**:
- Scalable agent architecture
- Load balancing across agents
- Consistent knowledge sharing

### Use Case 4: Intelligent Content Moderation

**Scenario**: Automated content moderation using ML models.

**Components**:
- RedisAI for model serving
- Streams for processing pipeline
- Caching for repeated content

**Benefits**:
- High-throughput processing
- Low latency decisions
- Cost-effective at scale

### Use Case 5: Semantic Search Engine

**Scenario**: Document search using natural language queries.

**Components**:
- Vector embeddings in Redis
- RediSearch for indexing
- RAG for enhanced results

**Benefits**:
- Semantic understanding
- Fast vector search
- Hybrid search capabilities

## Monitoring and Metrics

### Key Metrics to Track

```python
class RedisAIMetrics:
    def __init__(self, redis_client):
        self.redis = redis_client
    
    def track_inference(self, model_name, latency_ms, success=True):
        """Track model inference metrics"""
        timestamp = int(time.time())
        
        # Increment counters
        self.redis.incr(f"metrics:{model_name}:total_requests")
        if success:
            self.redis.incr(f"metrics:{model_name}:successful_requests")
        else:
            self.redis.incr(f"metrics:{model_name}:failed_requests")
        
        # Track latency (using sorted set for percentile calculations)
        self.redis.zadd(
            f"metrics:{model_name}:latencies",
            {str(timestamp): latency_ms}
        )
        
        # Trim old data (keep last 1000 entries)
        self.redis.zremrangebyrank(f"metrics:{model_name}:latencies", 0, -1001)
    
    def get_metrics(self, model_name):
        """Retrieve metrics for a model"""
        total = int(self.redis.get(f"metrics:{model_name}:total_requests") or 0)
        successful = int(self.redis.get(f"metrics:{model_name}:successful_requests") or 0)
        failed = int(self.redis.get(f"metrics:{model_name}:failed_requests") or 0)
        
        # Calculate percentiles
        latencies = self.redis.zrange(
            f"metrics:{model_name}:latencies",
            0, -1,
            withscores=True
        )
        
        if latencies:
            latency_values = sorted([score for _, score in latencies])
            p50 = latency_values[len(latency_values) // 2]
            p95 = latency_values[int(len(latency_values) * 0.95)]
            p99 = latency_values[int(len(latency_values) * 0.99)]
        else:
            p50 = p95 = p99 = 0
        
        return {
            "total_requests": total,
            "successful_requests": successful,
            "failed_requests": failed,
            "success_rate": (successful / total * 100) if total > 0 else 0,
            "latency_p50": p50,
            "latency_p95": p95,
            "latency_p99": p99
        }
```

## Conclusion

Redis AI integration provides a powerful foundation for building scalable, low-latency AI/LLM/agent systems. The key integration points include:

1. **Model Serving**: Direct model inference with RedisAI
2. **Caching**: Response and computation caching for cost reduction
3. **State Management**: Agent and session state persistence
4. **Vector Operations**: Semantic search and RAG implementations
5. **Communication**: Multi-agent coordination via Pub/Sub
6. **Real-time Processing**: Stream-based AI pipelines
7. **Monitoring**: Comprehensive metrics and observability

By leveraging Redis's performance characteristics and RedisAI's capabilities, you can build production-ready AI systems that scale to millions of users while maintaining sub-millisecond response times.

## References

- [RedisAI Documentation](https://redis.io/docs/stack/ai/)
- [RediSearch Vector Similarity](https://redis.io/docs/stack/search/reference/vectors/)
- [Redis Pub/Sub](https://redis.io/docs/manual/pubsub/)
- [Redis Streams](https://redis.io/docs/data-types/streams/)
- [RedisJSON](https://redis.io/docs/stack/json/)

## Related Documentation

- [[SKYNET.md]] - Technology & Systems Research
- [[ai scenarios simulator]] - AI Scenarios and Simulations
- [[textgenerator]] - AI Text Generation Tools

---

*Last Updated: 2025-11-17*
*Category: AI Infrastructure*
*Status: Research Documentation*

<!-- 8A4F2E91 -->
