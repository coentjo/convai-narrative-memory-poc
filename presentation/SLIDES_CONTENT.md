# Slide Content for "Human-Like Memory for Virtual Humans"

*10-minute presentation for IxD colleagues by crocodeux*

---

## **SLIDE 1: Title Slide**

### Visual:
- Large title: **"Human-Like Memory for Virtual Humans"**
- Subtitle: *"Making AI forget like humans do"*
- Authors: **Coen Crombach & Lonn van Bokhorst**
- Date: October 2025
- Background: Subtle brain/memory imagery

### Speaker Notes:
*"Hey everyone! Lonn and I have been working on something that might sound like science fiction, but it's actually based on 140-year-old memory science..."*

---

## **SLIDE 2: The Problem**

### Visual:
Split screen comparison:

**Left Side - Current AI:**
- 🤖 Perfect recall: "On October 15th at 14:32:17 you said..."
- 🤖 Total amnesia: "I don't remember our previous conversation"

**Right Side - Humans:**
- 👤 Fuzzy memory: "Last week we talked about... something important"
- 👤 Selective forgetting: "I remember the meeting but not what I wore"

### Speaker Notes:
*"Current AI either remembers EVERYTHING perfectly - which is creepy - or forgets EVERYTHING between sessions - which is frustrating. Humans don't work that way. We forget details but keep the important stuff."*

---

## **SLIDE 3: Our Solution - The Ebbinghaus Curve**

### Visual:
Beautiful decay curve graph showing:
- X-axis: Time (days)
- Y-axis: Memory retention (%)
- Curve: Exponential decay from 100% to ~23% over 2 years
- Key points marked:
  - 94% after 30 days
  - 70% after 180 days  
  - 48% after 1 year

### Speaker Notes:
*"We implemented the Ebbinghaus forgetting curve - discovered in 1885 - into AI memory. Recent memories stay crisp, old memories fade gradually, but they never completely disappear."*

**[LIVE DEMO 1 HERE - Time Travel Memory]**

---

## **SLIDE 4: But Important Things Resist Forgetting**

### Visual:
Formula visualization:
```
Memory Activation = Similarity × Decay × Salience
                   ↑          ↑       ↑
               How relevant  How old  How important
```

Example comparison:
- Recent trivial: 0.4 × 0.998 × 0.3 = **0.12**
- Old critical: 0.6 × 0.70 × 2.5 = **1.05** ← Wins!

### Speaker Notes:
*"Here's the clever part - we don't just use time. Important memories get higher 'salience' scores, so they resist forgetting. A system outage from 6 months ago can beat yesterday's weather chat."*

**[LIVE DEMO 2 HERE - Importance Beats Recency]**

---

## **SLIDE 5: What This Means for Virtual Humans**

### Visual:
Three use case scenarios with icons:

**🎯 Personalized Assistance**
- Remembers your preferences
- Forgets your typos

**🤝 Relationship Building**  
- Builds authentic connections over time
- Natural conversation continuity

**👥 Multi-Agent Teams**
- Shared important knowledge
- Individual personality perspectives

### Speaker Notes:
*"Imagine Virtual Humans that remember you worked late last Friday but forget you misspelled 'definitely'. Or a customer service team where agents share critical knowledge but each has their own personality and perspective."*

---

## **SLIDE 6: The Architecture (Lonn's Masterpiece)**

### Visual:
Clean microservices diagram:
```
📝 Indexer → 🧠 Resonance → 💬 Reteller
     ↓           ↓           ↓
   Stores      Finds       Makes
  memories   relevant     human-like
             ones
```

Connected by: **Kafka Streams + Qdrant Vector DB**

### Speaker Notes:
*"Lonn built this entire architecture - three microservices connected by Kafka streams. Indexer stores memories, Resonance finds relevant ones using our decay formula, Reteller makes them sound naturally human."*

**[LIVE DEMO 3 HERE - Show the science/validation if time allows]**

---

## **SLIDE 7: What's Next - 12 Week Roadmap**

### Visual:
Timeline with milestones:

**Weeks 1-3:** 👥 Multi-agent shared memories  
**Weeks 4-6:** 🎭 Character-driven retelling  
**Weeks 7-8:** 🔒 Security & privacy  
**Weeks 9-10:** ⚡ Scale testing (100+ agents)  
**Weeks 11-12:** 🔗 Virtual Human integration

### Speaker Notes:
*"Next 12 weeks: Multiple Virtual Humans sharing memories, each with distinct personalities. Same event, different retellings based on character traits. Plus security, scalability, and full integration with our Virtual Human platform."*

---

## **SLIDE 8: Questions & Contact**

### Visual:
- Team photo (if available) or professional headshots
- Contact information:
  - **Coen Crombach** - c.crombach@fontys.nl
  - **Lonn van Bokhorst** - l.vanbokhorst@fontys.nl
- GitHub repo link
- "Questions?" in large friendly font

### Speaker Notes:
*"This isn't just better AI - it's more human AI. Lonn handled the technical architecture brilliantly, I focused on the memory psychology and validation. Together we've proven this works, and we're excited to take it to the next level."*

*"Questions?"*

---

## **Slide Design Guidelines**

### Colors:
- Primary: Deep blue (#2C3E50)
- Accent: Warm orange (#E67E22)  
- Background: Clean white/light gray
- Text: Dark gray (#34495E)

### Fonts:
- Headers: Bold, modern sans-serif
- Body: Clean, readable sans-serif
- Code/formulas: Monospace

### Style:
- Minimal text per slide
- Large, clear visuals
- Consistent spacing
- Professional but approachable

### Timing:
- Slide 1: 30 seconds
- Slide 2: 1 minute
- Slide 3: 2 minutes (includes Demo 1)
- Slide 4: 2 minutes (includes Demo 2)  
- Slide 5: 1.5 minutes
- Slide 6: 1.5 minutes (includes Demo 3 if time)
- Slide 7: 1 minute
- Slide 8: 30 seconds + Q&A

**Total: ~10 minutes + questions**
