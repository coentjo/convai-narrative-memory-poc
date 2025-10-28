# 🧠 ConvAI Narrative Memory System - Presentation Outline

## 🎯 Presentation Goals
- Demonstrate a **psychologically-grounded** memory system for Virtual Humans
- Show how it differs from traditional RAG (Retrieval-Augmented Generation)
- Live demo of time-based memory decay and activation patterns
- Highlight the event-driven architecture and scalability

---

## 📋 Presentation Structure (15-20 minutes + Q&A)

### 1. **The Problem** (2-3 minutes)
**Hook**: *"Traditional chatbots have perfect memory or no memory at all - but humans don't work that way!"*

- Current AI memory limitations:
  - RAG systems: Static retrieval, no temporal dynamics
  - Context windows: Everything equally "fresh"
  - No forgetting curves or emotional weighting

**The Vision**: Virtual Humans that remember like humans do 🤖➡️👤

### 2. **Our Solution: Psychologically-Grounded Memory** (3-4 minutes)

#### Core Innovation: **Time-Based Memory Decay**
**Historical Foundation**: Hermann Ebbinghaus (1885) - The Pioneer of Memory Science 🎓
*[Show: `images/ebbinghaus_portrait.jpg` and `images/nonsense_syllables.png`]*

**Ebbinghaus's Original Findings**:
- Memorized nonsense syllables: "WID", "ZOF", "KAF"
- **20 minutes**: 60% retention
- **1 hour**: 45% retention  
- **1 day**: 34% retention
- **2 days**: 30% retention

*[Show: `images/ebbinghaus_forgetting_curve.png` - the original data]*

**Our Implementation**:
- **Ebbinghaus Forgetting Curve**: `decay = exp(-λ × age_in_days)`
- **Activation Strength**: `similarity × decay × emotional_salience`
- **Realistic Aging**: "yesterday" → "about 3 months ago" → "years back"

*[Show: `images/decay_function_graph.png` and `images/activation_scores_timeline.png`]*

#### Key Differentiators:
✅ **Temporal Awareness**: Recent memories dominate recall  
✅ **Emotional Weighting**: Important events resist forgetting  
✅ **Natural Forgetting**: Old memories fade unless reactivated  
✅ **Multilingual**: BGE-M3 embeddings support 100+ languages  

### 3. **Architecture Deep Dive** (4-5 minutes)

#### **Event-Driven Microservices** 🔄
*[Show: `images/architecture_overview.png` and `images/kafka_flow.png`]*

```
User Input → Kafka → [Indexer] → Qdrant
                  ↓
Query → [Resonance] → [Reteller] → Response
```

**Why Event-Driven?**
- **Auditability**: Every memory operation is logged
- **Scalability**: Components scale independently  
- **Resilience**: Failure-tolerant message queues
- **Temporal Decoupling**: Async processing

#### **The Memory Pipeline**:
1. **Indexer**: Text → Vector embeddings → Qdrant storage
2. **Resonance**: Query → Similarity search → Time decay → Activation scoring
3. **Reteller**: Memory beats → LLM narrative → Human-like response

### 4. **Live Demo** (8-10 minutes) 🎬

#### **Demo Script**: "The Ebbinghaus Experiment - 140 Years Later" 🧪

**Phase 1: Memory Formation** (like Ebbinghaus learning syllables)
```
🎭 "I learned three key concepts today: WID means 'Working with Intelligent Data', 
   ZOF stands for 'Zero-Overhead Forgetting', and KAF represents 'Kafka-Anchored Flows'"
📝 Show: Anchor storage, embedding generation, salience scoring
```

**Phase 2: Immediate Recall** (100% retention - just like Ebbinghaus)
```
🎭 Query: "What did I learn about WID, ZOF, and KAF?"
🔍 Show: Perfect recall, high activation scores, "just now" age labels
```

**Phase 3: The 20-Minute Test** ⏰ (Ebbinghaus: 60% retention)
```
🎭 Command: `/advance_time 20m` (simulating 20 minutes)
🎭 Query: "What were those three concepts again?"
🔍 Show: Slight decay, still strong activation, "20 minutes ago"
```

**Phase 4: The 1-Day Test** ⏰ (Ebbinghaus: 34% retention)
```
🎭 Command: `/advance_time 1d`
🎭 Query: "What did I learn yesterday?"
🔍 Show: Noticeable decay, lower activation, "yesterday"
```

**Phase 5: The 2-Day Test** ⏰ (Ebbinghaus: 30% retention)
```
🎭 Command: `/advance_time 2d`
🎭 Query: "What were those acronyms I learned?"
🔍 Show: Further decay, "2 days ago", some details may be lost
```

**Phase 6: Multiple Memory Integration** (Beyond Ebbinghaus)
```
🎭 Add emotional context: "The ZOF concept was brilliant - it solved our biggest problem!"
🎭 Show: How emotional salience (higher salience score) resists forgetting
🎭 Demonstrate: Multiple time-stamped memories woven into coherent narratives
```

#### **Demo Tools Available**:
- **Streamlit UI**: Real-time memory visualization 📊
- **Terminal Chatbot**: Command-line interaction 💻
- **Three Retells Demo**: Pre-scripted memory scenarios 📋

### 5. **Technical Highlights** (2-3 minutes)

#### **Production-Ready Features**:
- **Configurable Models**: Deterministic → Ollama → OpenAI/Portkey
- **Multilingual Support**: BGE-M3 embeddings
- **Docker Compose**: One-command deployment
- **Monitoring**: Kafka event logs, activation score tracking

#### **Psychological Realism**:
- **Diversity Selection**: Avoids repetitive memories
- **Session Isolation**: Current conversation doesn't pollute recall
- **Salience Weighting**: Emotional importance affects retention
- **Cross-time Damping**: Prevents temporal bleeding

### 6. **Research Impact & Future** (2 minutes)

#### **Current Achievements**:
✅ **Realistic Forgetting**: Exponential decay with configurable parameters  
✅ **Scalable Architecture**: Event-driven microservices  
✅ **Multilingual Memory**: Cross-language semantic search  
✅ **Production Deployment**: Docker-based, configurable models  

#### **Future Directions**:
🔮 **Memory Consolidation**: Merge similar memories over time  
🔮 **Emotional Tagging**: Sentiment-aware salience scoring  
🔮 **Reconsolidation**: Recently accessed memories get "refreshed"  
🔮 **False Memories**: Probabilistic memory blending  

---

## 🎬 Demo Preparation Checklist

### **Pre-Demo Setup** (5 minutes before):
- [ ] Start Docker stack: `docker compose up -d kafka qdrant indexer resonance reteller streamlit`
- [ ] Verify Streamlit UI: http://localhost:8501
- [ ] Test basic chat interaction
- [ ] Prepare backup terminal chatbot

### **Demo Environment**:
- **Primary**: Streamlit UI (visual, audience-friendly)
- **Backup**: Terminal chatbot (reliable, fast)
- **Fallback**: Pre-recorded demo video

### **Demo Data Scenarios**:
1. **Research Context**: "Working on narrative memory at Fontys"
2. **Technical Details**: "Using Kafka, Qdrant, and BGE-M3 embeddings"
3. **Time Progression**: Advance 30d → 90d → 6m to show decay
4. **Multi-memory Recall**: Query that triggers multiple time periods

---

## 🗣️ Key Talking Points

### **For Technical Audience**:
- Event-driven architecture benefits
- Vector similarity vs. activation scoring
- Kafka partitioning and scaling strategies
- Embedding model trade-offs (speed vs. quality vs. multilingual)

### **For Research Audience**:
- Psychological grounding (Ebbinghaus curve)
- Comparison with human memory systems
- Implications for Virtual Human believability
- Research validation methodology

### **For Business Audience**:
- Scalability and production readiness
- Cost implications (local vs. cloud models)
- Use cases beyond chatbots (customer service, education, therapy)

---

## 🚨 Demo Risk Mitigation

### **Potential Issues & Solutions**:
- **Kafka/Docker Issues**: Have terminal chatbot ready
- **Network Latency**: Use local Ollama models
- **Empty Memory**: Pre-seed with demo anchors
- **UI Glitches**: Terminal fallback always works

### **Backup Plans**:
1. **Plan A**: Live Streamlit demo
2. **Plan B**: Terminal chatbot demo  
3. **Plan C**: Pre-recorded video + explanation
4. **Plan D**: Architecture slides + code walkthrough

---

## 📊 Success Metrics

### **Audience Engagement**:
- Questions about psychological realism
- Interest in technical architecture
- Requests for code/deployment details

### **Demo Effectiveness**:
- Clear visualization of time decay
- "Aha!" moments when memories age
- Understanding of event-driven benefits

---

*This presentation balances technical depth with accessible concepts, using live demos to make abstract memory concepts tangible. The modular structure allows adaptation based on audience and time constraints.* 🎯
