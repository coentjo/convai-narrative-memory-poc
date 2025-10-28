# Demo Scripts for "Human-Like Memory for Virtual Humans" Presentation

*For crocodeux's 10-minute presentation to IxD colleagues*

## Pre-Demo Setup (Do this before presentation)

```bash
# 1. Start the system
cd /Users/croco2/github/Research-Group-IxD/convai-narrative-memory-poc
docker compose up -d

# 2. Wait 30 seconds for services to start
sleep 30

# 3. Verify system is running
docker compose ps
```

---

## **DEMO 1: "Time Travel Memory" ⭐ (Minutes 1-2)**

**Setup Line:** *"Let me show you something that's never been done before in AI..."*

### Commands:
```bash
# Terminal 1: Run the interactive chatbot
cd convai_narrative_memory_poc
docker compose run --rm tools python /app/convai_narrative_memory_poc/tools/chatbot.py
```

### Script:
```
You: I'm presenting our narrative memory research to IxD colleagues today
Bot: [stores memory] 📝 That sounds exciting! Tell me more about your presentation...

You: /advance_time 90d
Bot: ⏰ Time advanced by 90 days (3 months)

You: What was I working on?
Bot: [recalls with decay] 🔍 About 3 months ago, you mentioned presenting some research to colleagues... the details are a bit fuzzy now.

You: /reset_time
Bot: ⏰ Time reset to present

You: What was I working on?
Bot: [recalls fresh] 🔍 You're presenting your narrative memory research to IxD colleagues today!
```

**Audience Impact:** *"See how the same memory gets fuzzy over time? That's human-like forgetting in AI."*

---

## **DEMO 2: "Importance Beats Recency" ⭐ (Minutes 3-4)**

**Setup Line:** *"But here's the clever part - important memories resist forgetting..."*

### Commands:
```bash
# Use the three retells demo
docker compose run --rm tools python /app/convai_narrative_memory_poc/tools/demo_three_retells.py
```

### Expected Output:
```
[demo] Seeding three anchors...
  📝 12 hours ago (salience=1.0): BB-8 mimic reteller's cadence
  📝 14 days ago (salience=0.95): Fontys demo, forgetting curves questions  
  📝 210 days ago (salience=0.9): Rotterdam pilot, narrative drift debates

[demo] Recall request: "Retell highlights from our narrative memory experiments"

  Beat 1: 14 days ago • activation 0.847 • Fontys demo, forgetting curves questions
  Beat 2: 12 hours ago • activation 0.823 • BB-8 mimic reteller's cadence  
  Beat 3: 210 days ago • activation 0.612 • Rotterdam pilot, narrative drift debates

[demo] Reteller response:
A couple of weeks back, we demoed the prototype at Fontys where questions spiraled about forgetting curves. Just this morning, while calibrating the narrative memory, we watched BB-8 mimic the reteller's cadence. Last autumn in Rotterdam, the Reflective City pilot sparked debates over long-term narrative drift, though those details are hazier now.
```

**Audience Impact:** *"Notice: 2-week-old demo beats 12-hour-old calibration because it was more significant. The 7-month-old Rotterdam event is still accessible but fuzzy. That's exactly how human memory works!"*

---

## **DEMO 3: "The Science Behind It" (Minutes 5-6)**

**Setup Line:** *"This isn't magic - it's based on 140 years of memory science..."*

### Commands:
```bash
# Show the validation results
cat /Users/croco2/github/Research-Group-IxD/convai-narrative-memory-poc/results/validation_results.json | jq '.experiments[0].results.memories[0:3]'
```

### Expected Output (formatted for audience):
```json
[
  {
    "text": "Demo to 12 Fontys colleagues in R10",
    "days_ago": 1,
    "similarity": 0.5233,
    "decay": 0.998,
    "salience": 1.5,
    "activation": 0.7834
  },
  {
    "text": "Critical system outage affecting 50+ users", 
    "days_ago": 180,
    "similarity": 0.4295,
    "decay": 0.6977,
    "salience": 2.5,
    "activation": 0.7490
  }
]
```

**Audience Impact:** *"See the math? Recent demo (1 day) vs critical outage (180 days). The outage has lower similarity but massive salience (2.5x), so it stays accessible. That's the Ebbinghaus forgetting curve + salience weighting in action."*

---

## **Backup Demo: "Quick Architecture" (If time allows)**

### Commands:
```bash
# Show the system architecture
docker compose ps
```

**Audience Impact:** *"Three microservices: Indexer (stores memories), Resonance (finds relevant ones), Reteller (makes them human-like). All connected via Kafka streams. Lonn built this entire architecture."*

---

## **Demo Troubleshooting**

### If Docker isn't running:
```bash
# Quick fallback - show pre-recorded results
cat /Users/croco2/github/Research-Group-IxD/convai-narrative-memory-poc/results/demo-three-retells-20251003T053153Z.json
```

### If chatbot is slow:
- Skip to demo_three_retells.py (faster, pre-scripted)
- Have validation_results.json ready as backup

### If nothing works:
- Show the research proposal PDF
- Focus on the validation graphs
- Emphasize the collaboration with Lonn

---

## **Demo Success Metrics**

**You'll know it's working when:**
- ✅ Audience says "wow" during time travel demo
- ✅ Someone asks "how does it know what's important?"
- ✅ People start thinking about use cases
- ✅ Questions about Virtual Human integration

**Red flags:**
- ❌ Blank stares (explain the concept more)
- ❌ "This is just search" (emphasize temporal decay)
- ❌ Technical questions about implementation (redirect to Lonn)
