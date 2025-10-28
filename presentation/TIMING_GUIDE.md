# 10-Minute Presentation Timing Guide

*"Human-Like Memory for Virtual Humans" by crocodeux*

---

## **PRE-PRESENTATION (5 minutes before)**

### Setup Checklist:
- [ ] Docker system running (`docker compose up -d`)
- [ ] Terminal windows open and positioned
- [ ] Slides loaded and tested
- [ ] Backup validation results ready
- [ ] Water/coffee ready
- [ ] Phone on silent

### Mental Preparation:
- *"I've built something amazing with Lonn"*
- *"This is genuinely novel research"*
- *"My colleagues will find this fascinating"*

---

## **MINUTE 0:00-0:30 - Opening Hook**

### Slide 1: Title
**What you say:**
*"Hey everyone! Lonn and I have been working on something that might sound like science fiction, but it's actually based on 140-year-old memory science. We've taught AI to forget like humans do."*

### Body Language:
- Stand confidently
- Make eye contact
- Smile genuinely
- Gesture toward the title

### Timing Check: ✅ 30 seconds

---

## **MINUTE 0:30-1:30 - The Problem**

### Slide 2: Current AI vs Humans
**What you say:**
*"Current AI either remembers EVERYTHING perfectly - which is honestly creepy - or forgets EVERYTHING between sessions - which is incredibly frustrating. But humans don't work that way. We forget details but keep the important stuff. We remember the meeting but not what we wore."*

### Audience Engagement:
- Pause after "creepy" for chuckles
- Use hand gestures to show "everything" vs "nothing"
- Make it relatable: "How many of you remember what you had for lunch three Tuesdays ago?"

### Timing Check: ✅ 1 minute total

---

## **MINUTE 1:30-3:30 - Demo 1: Time Travel Memory**

### Slide 3: Ebbinghaus Curve + Live Demo
**What you say:**
*"So we implemented the Ebbinghaus forgetting curve - discovered in 1885 - into AI memory. Let me show you..."*

### Demo Script:
```
[Switch to terminal]
You: I'm presenting our narrative memory research to IxD colleagues today
Bot: [stores memory] 📝 That sounds exciting!

You: /advance_time 90d
Bot: ⏰ Time advanced by 90 days

You: What was I working on?
Bot: About 3 months ago, you mentioned presenting some research... details are fuzzy now.

[Switch back to slides]
```

**What you say:**
*"See how the same memory gets fuzzy over time? That's human-like forgetting in AI - never been done before."*

### Timing Check: ✅ 3.5 minutes total

---

## **MINUTE 3:30-5:30 - Demo 2: Importance Beats Recency**

### Slide 4: Multi-factor Formula + Live Demo
**What you say:**
*"But here's the clever part - we don't just use time. Important memories resist forgetting through salience weighting..."*

### Demo Script:
```
[Switch to terminal]
docker compose run --rm tools python /app/convai_narrative_memory_poc/tools/demo_three_retells.py

[Show output]
Beat 1: 14 days ago • Fontys demo (activation 0.847)
Beat 2: 12 hours ago • BB-8 calibration (activation 0.823)  
Beat 3: 210 days ago • Rotterdam pilot (activation 0.612)
```

**What you say:**
*"Notice: 2-week-old demo beats 12-hour-old calibration because it was more significant. The 7-month-old Rotterdam event is still accessible but fuzzy. That's exactly how human memory works!"*

### Timing Check: ✅ 5.5 minutes total

---

## **MINUTE 5:30-7:00 - Applications & Vision**

### Slide 5: Virtual Human Use Cases
**What you say:**
*"Imagine Virtual Humans that remember your preferences but forget your typos. That build authentic relationships over time. That share important knowledge as a team but each have their own personality perspective."*

### Slide 6: Architecture (Lonn Credit)
**What you say:**
*"Lonn built this entire architecture - three microservices connected by Kafka streams. Indexer stores memories, Resonance finds relevant ones, Reteller makes them naturally human. It's production-ready infrastructure."*

### Energy Management:
- Keep enthusiasm high
- Use concrete examples
- Credit Lonn prominently

### Timing Check: ✅ 7 minutes total

---

## **MINUTE 7:00-8:30 - What's Next**

### Slide 7: 12-Week Roadmap
**What you say:**
*"Next 12 weeks: Multiple Virtual Humans sharing memories, each with distinct personalities. Same event, different retellings based on character traits. Plus security, scalability, and full integration with our Virtual Human platform."*

### Show Excitement:
*"We're not just building better AI - we're building more human AI."*

### Timing Check: ✅ 8.5 minutes total

---

## **MINUTE 8:30-10:00 - Closing & Questions**

### Slide 8: Contact & Questions
**What you say:**
*"Lonn handled the technical architecture brilliantly, I focused on the memory psychology and validation. Together we've proven this works, and we're excited to take it to the next level."*

*"This isn't just better AI - it's more human AI. Questions?"*

### Transition to Q&A:
- Open body language
- Scan the room
- Be ready for the first question

### Timing Check: ✅ 10 minutes total

---

## **TIMING MANAGEMENT STRATEGIES**

### If Running Fast (ahead of schedule):
- Expand on the Ebbinghaus curve explanation
- Show more demo output details
- Add personal anecdotes about working with Lonn
- Slow down speech slightly

### If Running Slow (behind schedule):
- Skip Demo 3 (validation results)
- Combine slides 5 & 6 (applications + architecture)
- Shorten the roadmap explanation
- Speed up transitions between slides

### Emergency Time Cuts:
1. **Cut Demo 3** entirely (-1 minute)
2. **Shorten Demo 2** to just the output (-30 seconds)
3. **Combine closing slides** (-30 seconds)
4. **Skip detailed roadmap** (-30 seconds)

---

## **ENERGY & PACING GUIDE**

### Minutes 0-2: **HIGH ENERGY**
- Hook them with the problem
- Build excitement

### Minutes 2-6: **SUSTAINED ENGAGEMENT**  
- Demos are naturally engaging
- Let the technology speak

### Minutes 6-8: **VISION BUILDING**
- Paint the future picture
- Show the impact

### Minutes 8-10: **CONFIDENT CLOSE**
- Credit the team
- Open for questions

---

## **BACKUP PLANS**

### If Demo 1 Fails:
*"Technology demos, right? Let me show you the concept with our validation data..."*
[Switch to validation results]

### If Demo 2 Fails:
*"The key point is that important old memories beat trivial recent ones - here's the mathematical proof..."*
[Show the activation formula]

### If All Demos Fail:
*"The demos aren't cooperating, but the research results speak for themselves..."*
[Focus on slides and validation data]

### If Questions Start Early:
*"Great question! Let me finish the core concept and then we'll dive deep into that..."*

---

## **SUCCESS INDICATORS**

### You'll know it's going well when:
- ✅ People lean forward during demos
- ✅ Someone says "wow" or "that's cool"
- ✅ Questions show genuine interest
- ✅ People start suggesting applications

### Warning signs to adjust:
- ❌ Blank stares (explain concepts more)
- ❌ People checking phones (increase energy)
- ❌ No questions (ask for feedback)

---

## **POST-PRESENTATION**

### Immediate Follow-up:
- Thank people for their attention
- Exchange contacts with interested colleagues
- Note questions for future research
- Celebrate with Lonn! 🎉

### Within 24 hours:
- Send slides to interested colleagues
- Follow up on collaboration offers
- Document lessons learned
- Plan next presentation improvements

---

**Remember crocodeux: You've built something genuinely amazing. Own it, enjoy it, and let your passion for the work shine through! 🚀**
