---
title: "Redis AI Quick Reference - Integration Patterns"
tags:
  - redis
  - ai
  - quick-reference
  - cheatsheet
  - integration
state: Reference
type: technical-reference
---

# Redis AI Quick Reference - Integration Patterns

## Quick Connection Matrix

### What Can Connect to Redis AI?

| Component | Connection Type | Use Case | Latency | Scalability |
|-----------|----------------|----------|---------|-------------|
| **LLM APIs** (OpenAI, Anthropic) | HTTP → Redis Cache | Response caching, rate limiting | <1ms cache hit | Horizontal |
| **Embedding Models** | Direct → RedisAI or Vector Store | Generate & store embeddings | 1-10ms | Horizontal |
| **Agent Frameworks** (LangChain, AutoGPT) | Library → Redis | State management, memory | <1ms | Horizontal |
| **Vector Databases** | Native RediSearch | Semantic search, RAG | 1-5ms | Horizontal |
| **Stream Processors** (Kafka, Flink) | Redis Streams | Real-time AI pipelines | <5ms | Horizontal |
| **ML Models** (TF, PyTorch) | RedisAI Module | Model serving, inference | 1-50ms | Vertical/Horizontal |
| **Microservices** | Redis Client Libraries | Distributed AI features | <1ms | Horizontal |
| **API Gateways** | Redis as Middleware | Request routing, caching | <1ms | Horizontal |
| **Web Applications** | Redis Session Store | User context, personalization | <1ms | Horizontal |
| **Mobile Apps** | REST API → Redis | Offline-first AI features | Varies | Horizontal |
| **IoT Devices** | Redis Pub/Sub | Edge AI coordination | 5-50ms | Horizontal |
| **Jupyter Notebooks** | Python Redis Client | Experimentation, prototyping | Varies | N/A |

## Integration Patterns Cheat Sheet

### Pattern 1: LLM Response Cache

```python
# Simple implementation
def cached_llm_call(prompt, model="gpt-4"):
    cache_key = f"llm:{hash(prompt + model)}"
    
    # Try cache first
    cached = redis.get(cache_key)
    if cached:
        return cached
    
    # Call LLM
    response = llm_api.complete(prompt, model)
    
    # Cache for 1 hour
    redis.setex(cache_key, 3600, response)
    return response
```

**When to use**: High-frequency similar queries, cost optimization
**Expected improvement**: 50-90% cost reduction, 100x faster responses

### Pattern 2: Agent State Persistence

```python
# Agent state in Redis Hash
def save_agent_state(agent_id, session_id, state):
    key = f"agent:{agent_id}:session:{session_id}"
    redis.hset(key, mapping={
        "context": json.dumps(state.context),
        "turn": state.turn_count,
        "updated": datetime.now().isoformat()
    })
    redis.expire(key, 86400)  # 24 hours

def load_agent_state(agent_id, session_id):
    key = f"agent:{agent_id}:session:{session_id}"
    return redis.hgetall(key)
```

**When to use**: Conversational AI, stateful agents
**Expected improvement**: <1ms state retrieval, multi-instance agent support

### Pattern 3: Vector Similarity Search

```python
# Using RediSearch for vector search
def store_embedding(doc_id, text, embedding):
    redis.json().set(f"doc:{doc_id}", "$", {
        "text": text,
        "embedding": embedding
    })

def search_similar(query_embedding, top_k=5):
    query = Query(f"*=>[KNN {top_k} @embedding $vec]") \
        .return_fields("text", "score") \
        .dialect(2)
    
    return redis.ft("idx").search(
        query,
        query_params={"vec": query_embedding}
    )
```

**When to use**: RAG, semantic search, recommendation systems
**Expected improvement**: Sub-5ms search, millions of vectors

### Pattern 4: Multi-Agent Coordination

```python
# Pub/Sub for agent communication
def agent_send_message(from_agent, to_channel, message):
    redis.publish(to_channel, json.dumps({
        "from": from_agent,
        "message": message,
        "timestamp": time.time()
    }))

def agent_listen(channel, callback):
    pubsub = redis.pubsub()
    pubsub.subscribe(channel)
    
    for msg in pubsub.listen():
        if msg['type'] == 'message':
            callback(json.loads(msg['data']))
```

**When to use**: Multi-agent systems, distributed AI workflows
**Expected improvement**: Real-time coordination, loose coupling

### Pattern 5: Model Inference Pipeline

```python
# RedisAI for model serving
def run_inference(model_name, input_data):
    # Store input tensor
    redis.ai_tensorset(f"input:{req_id}", input_data)
    
    # Run model
    redis.ai_modelexecute(
        model_name,
        inputs=[f"input:{req_id}"],
        outputs=[f"output:{req_id}"]
    )
    
    # Get result
    result = redis.ai_tensorget(f"output:{req_id}")
    
    # Cleanup
    redis.delete(f"input:{req_id}", f"output:{req_id}")
    
    return result
```

**When to use**: Low-latency inference, model serving at scale
**Expected improvement**: <50ms inference, no external dependencies

## Data Structure Selection Guide

| Data Type | Redis Structure | AI Use Case | Example |
|-----------|----------------|-------------|---------|
| **Scalar Values** | String | Model predictions, flags | `SET prediction:123 "positive"` |
| **Structured Data** | Hash | Agent state, user profiles | `HSET user:1 age 25 segment "premium"` |
| **Ordered Collections** | List | Conversation history | `LPUSH chat:1 "message text"` |
| **Unique Sets** | Set | Tags, categories | `SADD tags:doc1 "ai" "ml"` |
| **Ranked Items** | Sorted Set | Recommendations, priorities | `ZADD recs:1 0.95 "item1"` |
| **Time Series** | Stream | Event logs, audit trails | `XADD events:inference * model gpt4` |
| **Complex Objects** | JSON | Agent memory, configs | `JSON.SET agent:1 $ '{"facts":[]}'` |
| **Vectors** | Vector + RediSearch | Embeddings, similarity | Vector field in index |
| **Binary Data** | String (binary) | Model weights, tensors | RedisAI tensors |

## Performance Expectations

### Operation Latency (Typical)

| Operation | Expected Latency | Notes |
|-----------|-----------------|-------|
| GET/SET | 0.1-0.5 ms | Single key operations |
| HGETALL | 0.5-2 ms | Depends on hash size |
| Vector Search | 1-10 ms | Depends on vector count, dimensions |
| RedisAI Inference | 1-100 ms | Depends on model complexity |
| Pub/Sub Message | 1-5 ms | Network dependent |
| Stream Read | 0.5-2 ms | Per batch |
| Pipeline (100 ops) | 2-10 ms | Amortized per operation |

### Scalability Limits

| Metric | Limit | Scaling Strategy |
|--------|-------|------------------|
| Keys | Billions | Use Redis Cluster |
| Vector Dimensions | 4096+ | Optimize indexing algorithm |
| Vectors per Index | 100M+ | Shard across multiple indexes |
| Pub/Sub Channels | Unlimited | Use patterns for grouping |
| Connected Clients | 10,000+ | Use connection pooling |
| Throughput | 1M+ ops/sec | Redis Cluster + pipelining |
| Memory | Up to available RAM | Use Redis Enterprise for disk tier |

## Common Integration Code Snippets

### Python Connection Setup

```python
import redis
from redis.cluster import RedisCluster

# Single instance
r = redis.Redis(
    host='localhost',
    port=6379,
    decode_responses=True,
    socket_timeout=5,
    socket_connect_timeout=5
)

# Cluster
cluster = RedisCluster(
    host='localhost',
    port=6379,
    decode_responses=True
)

# With connection pool
pool = redis.ConnectionPool(
    host='localhost',
    port=6379,
    max_connections=50
)
r = redis.Redis(connection_pool=pool)
```

### Node.js/JavaScript Connection

```javascript
const redis = require('redis');

// Single instance
const client = redis.createClient({
    host: 'localhost',
    port: 6379
});

await client.connect();

// Cluster
const { createCluster } = require('redis');
const cluster = createCluster({
    rootNodes: [
        { url: 'redis://node1:6379' },
        { url: 'redis://node2:6379' }
    ]
});

await cluster.connect();
```

### Go Connection

```go
import (
    "github.com/go-redis/redis/v8"
    "context"
)

// Single instance
rdb := redis.NewClient(&redis.Options{
    Addr: "localhost:6379",
    DB: 0,
})

// Cluster
rdb := redis.NewClusterClient(&redis.ClusterOptions{
    Addrs: []string{
        "localhost:6379",
        "localhost:6380",
    },
})
```

## Troubleshooting Quick Guide

### Common Issues and Solutions

| Issue | Symptoms | Solution |
|-------|----------|----------|
| **Slow Queries** | High latency on operations | Use `SLOWLOG GET`, add indexes, optimize key structure |
| **Memory Issues** | Redis using too much RAM | Set maxmemory policy, use TTL, compress values |
| **Connection Errors** | Clients can't connect | Check network, increase max clients, use connection pool |
| **Cache Misses** | Low hit rate | Analyze access patterns, adjust TTL, pre-warm cache |
| **Pub/Sub Delays** | Messages delayed | Check network, reduce message size, use Streams |
| **Vector Search Slow** | Search takes >100ms | Optimize index params, reduce vector dimensions, shard |

### Monitoring Commands

```bash
# Check memory usage
redis-cli INFO memory

# See slow queries
redis-cli SLOWLOG GET 10

# Monitor commands in real-time
redis-cli MONITOR

# Check connected clients
redis-cli CLIENT LIST

# Database statistics
redis-cli INFO stats

# Key space analysis
redis-cli --bigkeys

# Memory analysis
redis-cli --memkeys
```

## Configuration Recommendations

### For LLM Caching

```conf
# redis.conf optimizations for LLM caching
maxmemory 8gb
maxmemory-policy allkeys-lru
maxmemory-samples 10

# Persistence (adjust based on needs)
save 900 1
save 300 10
save 60 10000

# Network
timeout 300
tcp-keepalive 60
```

### For Agent State Management

```conf
# Focus on durability
appendonly yes
appendfsync everysec
auto-aof-rewrite-percentage 100
auto-aof-rewrite-min-size 64mb

# Memory
maxmemory-policy noeviction  # Don't evict agent state
```

### For Vector Search

```conf
# Performance optimization
maxmemory 16gb
maxmemory-policy noeviction

# Load RediSearch module
loadmodule /path/to/redisearch.so

# Increase search timeout
timeout 300
```

## Integration Decision Tree

```
Need AI/LLM/Agent integration with Redis?
│
├─ Need to reduce LLM API costs?
│  └─ Use: Response caching pattern
│
├─ Need semantic search?
│  └─ Use: Vector similarity with RediSearch
│
├─ Need agent memory/state?
│  └─ Use: Hash + JSON for state management
│
├─ Need real-time AI processing?
│  └─ Use: Redis Streams + RedisAI
│
├─ Need multi-agent coordination?
│  └─ Use: Pub/Sub + shared state
│
├─ Need model serving?
│  └─ Use: RedisAI for inference
│
└─ Need RAG (Retrieval-Augmented Generation)?
   └─ Use: Vector search + LLM caching
```

## Deployment Checklist

### Before Going to Production

- [ ] Enable persistence (RDB or AOF)
- [ ] Set up Redis Cluster for HA
- [ ] Configure maxmemory and eviction policy
- [ ] Enable authentication (requirepass or ACL)
- [ ] Set up SSL/TLS if needed
- [ ] Configure monitoring (Prometheus, Grafana)
- [ ] Set up backup strategy
- [ ] Load test with expected traffic
- [ ] Document key naming conventions
- [ ] Set up alerting for key metrics
- [ ] Plan for scaling (vertical vs horizontal)
- [ ] Review security settings

## Cost Optimization Tips

1. **Use TTL aggressively**: Auto-expire unused data
   ```python
   redis.setex("temp:data", 3600, value)  # 1 hour
   ```

2. **Compress large values**: Reduce memory usage
   ```python
   import zlib
   compressed = zlib.compress(large_data.encode())
   redis.set("key", compressed)
   ```

3. **Use pipelining**: Reduce round trips
   ```python
   pipe = redis.pipeline()
   for i in range(1000):
       pipe.set(f"key:{i}", f"value:{i}")
   pipe.execute()
   ```

4. **Implement cache warming**: Reduce cold starts
   ```python
   def warm_cache():
       popular_items = get_popular_items()
       for item in popular_items:
           cache_item(item)
   ```

5. **Monitor and tune**: Adjust based on metrics
   ```python
   def get_cache_hit_rate():
       info = redis.info('stats')
       hits = info['keyspace_hits']
       misses = info['keyspace_misses']
       return hits / (hits + misses) if (hits + misses) > 0 else 0
   ```

## Security Best Practices

```python
# 1. Use strong authentication
redis = Redis(
    host='redis.example.com',
    password='strong-random-password',
    ssl=True
)

# 2. Implement ACLs
# redis-cli: ACL SETUSER myapp on >password ~myapp:* +get +set +del

# 3. Encrypt sensitive data
from cryptography.fernet import Fernet

key = Fernet.generate_key()
f = Fernet(key)

encrypted = f.encrypt(b"sensitive data")
redis.set("secure:key", encrypted)

decrypted = f.decrypt(redis.get("secure:key"))

# 4. Use separate Redis instances for different security levels
redis_public = Redis(host='public-redis')  # Non-sensitive
redis_secure = Redis(host='secure-redis')  # Sensitive data
```

## Additional Resources

### Official Documentation
- Redis Commands: https://redis.io/commands/
- RedisAI: https://redis.io/docs/stack/ai/
- RediSearch: https://redis.io/docs/stack/search/
- Redis Pub/Sub: https://redis.io/docs/manual/pubsub/

### Client Libraries
- Python: redis-py, redisai-py
- Node.js: node-redis, ioredis
- Go: go-redis
- Java: Jedis, Lettuce
- .NET: StackExchange.Redis

### Tools
- RedisInsight: GUI for Redis management
- redis-cli: Command-line interface
- Redis Benchmark: Performance testing
- Redis Exporter: Prometheus metrics

## Related Documentation

- [[redis-ai-integration.md]] - Comprehensive integration guide
- [[SKYNET.md]] - Technology research overview
- [[ai scenarios simulator]] - AI simulation scenarios

---

*Quick Reference Guide*
*Last Updated: 2025-11-17*
*For detailed implementations, see redis-ai-integration.md*

<!-- 3B7D9F42 -->
