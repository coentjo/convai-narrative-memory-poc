# PowerPoint Slide Deck: "Human-Like Memory for Virtual Humans"

**Instructions:** Copy each slide section into PowerPoint. Use the design guidelines at the bottom for consistent styling.

---

## SLIDE 1: Title Slide

### Title (Large, Bold):
**Human-Like Memory for Virtual Humans**

### Subtitle (Medium, Italic):
*Making AI forget like humans do*

### Authors:
**Coen Crombach & Lonn van Bokhorst**

### Date & Affiliation:
October 2025 • Research Group IxD • Fontys University

### Background:
- Subtle brain/memory imagery (optional)
- Deep blue (#2C3E50) or clean white background

### Speaker Notes:
"Hey everyone! Lonn and I have been working on something that might sound like science fiction, but it's actually based on 140-year-old memory science..."

---

## SLIDE 2: The Problem

### Title:
**The Problem with AI Memory**

### Layout: Split Screen (Two Columns)

#### LEFT COLUMN - Title: "Current AI" (Red accent #E74C3C)

**🤖 Perfect Recall**
"On October 15th at 14:32:17 you said..."

**🤖 Total Amnesia**
"I don't remember our previous conversation"

#### RIGHT COLUMN - Title: "Humans" (Green accent #27AE60)

**👤 Fuzzy Memory**
"Last week we talked about... something important"

**👤 Selective Forgetting**
"I remember the meeting but not what I wore"

### Speaker Notes:
"Current AI either remembers EVERYTHING perfectly - which is creepy - or forgets EVERYTHING between sessions - which is frustrating. Humans don't work that way. We forget details but keep the important stuff."

---

## SLIDE 3: Our Solution - The Ebbinghaus Curve

### Title:
**Our Solution: The Ebbinghaus Curve**

### Visual: Graph/Chart
- **X-axis:** Time (days) - Label: 0, 30d, 6m, 1y, 2y
- **Y-axis:** Memory retention (%) - Label: 0%, 25%, 50%, 75%, 100%
- **Curve:** Exponential decay from 100% to ~23% over 2 years
- **Line color:** Warm orange (#E67E22)
- **Key points marked with dots:**
  - 94% after 30 days
  - 70% after 180 days (6 months)
  - 48% after 1 year

### Text Below Graph:
**94%** after 30 days • **70%** after 180 days • **48%** after 1 year

### Demo Indicator (Orange box):
🎬 **LIVE DEMO: Time Travel Memory**

### Speaker Notes:
"We implemented the Ebbinghaus forgetting curve - discovered in 1885 - into AI memory. Recent memories stay crisp, old memories fade gradually, but they never completely disappear."

---

## SLIDE 4: Important Things Resist Forgetting

### Title:
**Important Things Resist Forgetting**

### Formula Box (Centered, Large):
```
Memory Activation = Similarity × Decay × Salience
                   ↑          ↑       ↑
               How relevant  How old  How important
```

### Comparison (Two Columns Below Formula):

#### LEFT: Recent Trivial (Red accent)
**Recent Trivial**
0.4 × 0.998 × 0.3 = **0.12**

#### RIGHT: Old Critical (Green accent)
**Old Critical**
0.6 × 0.70 × 2.5 = **1.05** ← Wins!

### Demo Indicator (Orange box):
🎬 **LIVE DEMO: Importance Beats Recency**

### Speaker Notes:
"Here's the clever part - we don't just use time. Important memories get higher 'salience' scores, so they resist forgetting. A system outage from 6 months ago can beat yesterday's weather chat."

---

## SLIDE 5: What This Means for Virtual Humans

### Title:
**What This Means for Virtual Humans**

### Layout: Three Columns (or Three Boxes)

#### BOX 1: 🎯 Personalized Assistance
**Personalized Assistance**
- Remembers your preferences
- Forgets your typos

#### BOX 2: 🤝 Relationship Building
**Relationship Building**
- Builds authentic connections over time
- Natural conversation continuity

#### BOX 3: 👥 Multi-Agent Teams
**Multi-Agent Teams**
- Shared important knowledge
- Individual personality perspectives

### Speaker Notes:
"Imagine Virtual Humans that remember you worked late last Friday but forget you misspelled 'definitely'. Or a customer service team where agents share critical knowledge but each has their own personality and perspective."

---

## SLIDE 6: The Architecture

### Title:
**The Architecture (Lonn's Masterpiece)**

### Visual: Flow Diagram (Horizontal)

```
📝 Indexer    →    🧠 Resonance    →    💬 Reteller
     ↓                  ↓                    ↓
  Stores            Finds                Makes
 memories         relevant            human-like
                    ones
```

### Text Below Diagram:
Connected by: **Kafka Streams + Qdrant Vector DB**

### Optional Demo Indicator (Gray box):
📊 **Optional: Show the Science**

### Speaker Notes:
"Lonn built this entire architecture - three microservices connected by Kafka streams. Indexer stores memories, Resonance finds relevant ones using our decay formula, Reteller makes them sound naturally human."

---

## SLIDE 7: What's Next - 12 Week Roadmap

### Title:
**What's Next: 12-Week Roadmap**

### Layout: Timeline (Two Rows, Three Columns Each)

#### ROW 1:
**Weeks 1-3:** 👥 Multi-agent shared memories

**Weeks 4-6:** 🎭 Character-driven retelling

**Weeks 7-8:** 🔒 Security & privacy

#### ROW 2:
**Weeks 9-10:** ⚡ Scale testing (100+ agents)

**Weeks 11-12:** 🔗 Virtual Human integration

**Outcome:** 📄 Publication

### Speaker Notes:
"Next 12 weeks: Multiple Virtual Humans sharing memories, each with distinct personalities. Same event, different retellings based on character traits. Plus security, scalability, and full integration with our Virtual Human platform."

---

## SLIDE 8: Questions & Contact

### Title:
**Questions?**

### Content (Centered):

**Coen Crombach** - c.crombach@fontys.nl

**Lonn van Bokhorst** - l.vanbokhorst@fontys.nl

GitHub: Research-Group-IxD/convai-narrative-memory-poc

### Quote (Large, Italic, Blue):
*"This isn't just better AI - it's more human AI"*

### Optional:
- Team photo or professional headshots
- Fontys/MindLabs logo

### Speaker Notes:
"This isn't just better AI - it's more human AI. Lonn handled the technical architecture brilliantly, I focused on the memory psychology and validation. Together we've proven this works, and we're excited to take it to the next level."

"Questions?"

---

## DESIGN GUIDELINES FOR POWERPOINT

### Color Palette:
- **Primary:** Deep blue (#2C3E50) - for headers and main text
- **Accent:** Warm orange (#E67E22) - for highlights, graphs, callouts
- **Background:** Clean white or light gray (#F8F9FA)
- **Text:** Dark gray (#34495E) - for body text
- **Success/Positive:** Green (#27AE60) - for human examples
- **Warning/Negative:** Red (#E74C3C) - for AI problems

### Typography:
- **Title Font:** Bold, modern sans-serif (e.g., Calibri Bold, Arial Black, or Segoe UI Bold)
- **Body Font:** Clean, readable sans-serif (e.g., Calibri, Arial, or Segoe UI)
- **Code/Formula Font:** Monospace (e.g., Consolas, Courier New)
- **Title Size:** 44-54pt
- **Body Size:** 18-24pt
- **Speaker Notes:** 12-14pt

### Layout Principles:
- **Minimal text per slide** - max 6-7 bullet points
- **Large, clear visuals** - graphs, icons, diagrams
- **Consistent spacing** - use PowerPoint's alignment guides
- **Professional but approachable** - not too corporate, not too casual

### Slide Transitions:
- Use simple transitions (Fade or None)
- Keep it professional
- Avoid distracting animations

### Icons & Emojis:
- Use emojis sparingly for visual interest
- Consider PowerPoint's built-in icons for a more professional look
- Keep emoji size consistent

### Graph for Slide 3:
If creating the Ebbinghaus curve in PowerPoint:
1. Insert → Chart → Scatter with Smooth Lines
2. Data points (approximate):
   - Day 0: 100%
   - Day 30: 94%
   - Day 180: 70%
   - Day 365: 48%
   - Day 730: 23%
3. Format line: Orange (#E67E22), 3pt width
4. Add data labels for key points (94%, 70%, 48%)

### Formula for Slide 4:
Use PowerPoint's Equation Editor:
1. Insert → Equation
2. Or use text boxes with superscript arrows (↑)
3. Format formula in monospace font, larger size

---

## TIMING REMINDERS

- **Slide 1:** 30 seconds
- **Slide 2:** 1 minute
- **Slide 3:** 2 minutes (includes Demo 1)
- **Slide 4:** 2 minutes (includes Demo 2)
- **Slide 5:** 1.5 minutes
- **Slide 6:** 1.5 minutes (includes Demo 3 if time)
- **Slide 7:** 1 minute
- **Slide 8:** 30 seconds + Q&A

**Total: ~10 minutes + questions**

---

## QUICK COPY-PASTE TIPS

1. **Create 8 blank slides** in PowerPoint
2. **Copy title** from each slide section above
3. **Copy content** into text boxes
4. **Add speaker notes** by right-clicking slide → Notes
5. **Apply design theme** with the color palette above
6. **Insert graph** for Slide 3 using chart tool
7. **Use SmartArt** for Slide 5 (three boxes) and Slide 7 (timeline)
8. **Add icons** from Insert → Icons (or use emojis)

Good luck with your presentation! 🚀

