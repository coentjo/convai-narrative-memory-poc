# 🎬 Live Demo Script: "The Ebbinghaus Experiment - 140 Years Later"

## 🎯 Demo Objective
Recreate Ebbinghaus's famous memory experiments using our AI system to demonstrate psychologically-realistic memory decay in action.

---

## 🚀 Pre-Demo Setup (5 minutes before presentation)

### 1. Start the System
```bash
cd /Users/croco2/github/Research-Group-IxD/convai-narrative-memory-poc
bash convai_narrative_memory_poc/scripts/create_topics.sh
docker compose -f convai_narrative_memory_poc/docker-compose.yml up -d kafka qdrant indexer resonance reteller streamlit
```

### 2. Verify System Health
- Open Streamlit UI: http://localhost:8501
- Test basic interaction: "Hello, I'm testing the system"
- Confirm memory operations appear in sidebar

### 3. Reset for Clean Demo
```
/reset_session
```

---

## 🎭 Live Demo Script

### **Opening Hook** (30 seconds)
*"In 1885, Hermann Ebbinghaus conducted the first scientific study of human memory. He memorized nonsense syllables like 'WID', 'ZOF', and 'KAF', then tested his recall over time. Today, 140 years later, we're going to recreate his experiment - but with an AI that remembers like a human."*

---

### **Phase 1: Memory Formation** 📝 (1 minute)

**Say to the system:**
```
I learned three key concepts today: WID means 'Working with Intelligent Data', ZOF stands for 'Zero-Overhead Forgetting', and KAF represents 'Kafka-Anchored Flows'. These are the core principles of our narrative memory system.
```

**Point out to audience:**
- 📝 Watch the "Memory Activity" sidebar - anchor being stored
- Show the embedding generation happening in real-time
- Note the salience score (emotional importance weight)

---

### **Phase 2: Immediate Recall** 🧠 (1 minute)
*"Ebbinghaus found 100% retention immediately after learning"*

**Query the system:**
```
What did I just learn about WID, ZOF, and KAF?
```

**Point out to audience:**
- 🔍 Perfect recall with high activation scores
- "just now" age labels in the memory beats
- System retrieves exact details, just like Ebbinghaus at time zero

---

### **Phase 3: The 20-Minute Test** ⏰ (1 minute)
*"After 20 minutes, Ebbinghaus retained 60% - let's see what happens to our AI"*

**Time travel:**
```
/advance_time 20m
```

**Query again:**
```
What were those three concepts I learned earlier?
```

**Point out to audience:**
- ⏰ Time advancement logged in the system
- Slight decay in activation scores (but still strong)
- Age labels now show "20 minutes ago"
- Memory still very accessible (matches Ebbinghaus's 60%)

---

### **Phase 4: The 1-Day Test** ⏰ (1 minute)
*"After 1 day, Ebbinghaus dropped to 34% retention"*

**Time travel:**
```
/advance_time 1d
```

**Query:**
```
What did I learn yesterday about those acronyms?
```

**Point out to audience:**
- 📉 Noticeable decay in activation scores
- "yesterday" age perception
- Some details may be less prominent (realistic forgetting)
- System mirrors human memory decay patterns

---

### **Phase 5: The 2-Day Test** ⏰ (1 minute)
*"At 2 days, Ebbinghaus was down to 30% - the forgetting curve flattens"*

**Time travel:**
```
/advance_time 2d
```

**Query:**
```
What were those technical concepts I learned a few days ago?
```

**Point out to audience:**
- 📉 Further decay, but curve is flattening (just like Ebbinghaus found)
- "2 days ago" age perception
- Memory still retrievable but weaker activation

---

### **Phase 6: Beyond Ebbinghaus - Emotional Salience** 🎯 (2 minutes)
*"But we can do something Ebbinghaus couldn't - show how emotions affect memory retention"*

**Reset time and add emotional context:**
```
/reset_time
The ZOF concept was absolutely brilliant - it solved our biggest technical challenge! I was so excited when I understood how Zero-Overhead Forgetting could revolutionize our system. This breakthrough will change everything!
```

**Time travel again:**
```
/advance_time 2d
```

**Query:**
```
What was I excited about a few days ago?
```

**Point out to audience:**
- 🌟 Higher salience score due to emotional content
- Better retention despite same time decay
- Emotional memories resist forgetting (psychological realism)
- System demonstrates both time decay AND emotional weighting

---

### **Phase 7: Multiple Memory Integration** 🧩 (1 minute)
*"Finally, let's see how the system weaves multiple time-stamped memories together"*

**Add another memory:**
```
/reset_time
Today I'm presenting this system to show how we've implemented Ebbinghaus's findings in AI. The audience will see both the technical architecture and the psychological grounding.
```

**Query that should trigger multiple memories:**
```
Tell me about my work with memory systems and presentations.
```

**Point out to audience:**
- 🔗 System retrieves memories from different time periods
- Coherent narrative weaving past and present
- Realistic age perception across multiple memories
- Demonstrates practical application beyond simple recall

---

## 🎯 Key Talking Points During Demo

### **Technical Highlights:**
- "Notice the activation scores - that's similarity × time_decay × emotional_salience"
- "The age perception is computed dynamically - 'yesterday', 'about 2 days ago'"
- "Each memory operation creates an event in Kafka - full auditability"

### **Psychological Realism:**
- "This mirrors exactly what Ebbinghaus found 140 years ago"
- "But we've added emotional weighting - excited memories resist forgetting"
- "The system doesn't just retrieve - it experiences time passing"

### **Practical Applications:**
- "Imagine a virtual therapist that remembers your progress over months"
- "Or a customer service AI that recalls your history with realistic aging"
- "Educational systems that adapt to how students naturally forget and remember"

---

## 🚨 Backup Plans

### **If Streamlit UI Fails:**
```bash
docker compose -f convai_narrative_memory_poc/docker-compose.yml run --rm chatbot
```
- Use terminal chatbot (more reliable)
- Same commands work
- Less visual but equally effective

### **If Docker Issues:**
```bash
python convai_narrative_memory_poc/tools/demo_three_retells.py
```
- Pre-scripted demo without Kafka
- Shows same concepts
- Fallback to pure Python

### **If Everything Fails:**
- Walk through the architecture slides
- Show code snippets of the decay function
- Explain the concept with the Ebbinghaus data

---

## 📊 Success Indicators

### **Audience Engagement:**
- "Aha!" moments when memories decay
- Questions about the psychological accuracy
- Interest in the technical implementation
- Requests for code or deployment details

### **Demo Effectiveness:**
- Clear visualization of time decay
- Understanding of emotional salience
- Appreciation for event-driven architecture
- Connection between Ebbinghaus and modern AI

---

## 🎤 Closing Hook
*"Hermann Ebbinghaus gave us the science of forgetting. Today, we've shown how that science can make AI more human. When machines remember like we do - with time, emotion, and gradual forgetting - they become partners in our cognitive journey, not just tools."*

---

**Total Demo Time: ~8-10 minutes**  
**Preparation Time: ~5 minutes**  
**Risk Level: Low (multiple fallbacks)**  
**Impact Level: High (visceral demonstration of concepts)** 🎯

