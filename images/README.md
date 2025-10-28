# 📸 Presentation Images Directory

This directory contains visual assets for the ConvAI Narrative Memory presentation.

## 🎯 Required Images for Maximum Impact

### **1. Historical Foundation**
- `ebbinghaus_portrait.jpg` - Hermann Ebbinghaus (1850-1909)
- `ebbinghaus_forgetting_curve.png` - Original forgetting curve graph
- `nonsense_syllables.png` - Examples: WID, ZOF, KAF with retention percentages

### **2. System Architecture**
- `architecture_overview.png` - Event-driven microservices diagram
- `kafka_flow.png` - Message flow through topics
- `memory_pipeline.png` - Indexer → Resonance → Reteller flow

### **3. Memory Decay Visualization**
- `activation_scores_timeline.png` - How activation changes over time
- `decay_function_graph.png` - Mathematical visualization of exp(-λ × days)
- `salience_impact.png` - How emotional weight affects retention

### **4. Demo Screenshots**
- `streamlit_ui_overview.png` - Main interface
- `memory_beats_sidebar.png` - Real-time memory activity
- `time_advancement_demo.png` - Before/after time travel

### **5. Comparison Charts**
- `traditional_vs_narrative_memory.png` - RAG vs our approach
- `human_vs_ai_memory.png` - Parallel memory characteristics

## 🎨 Image Creation Suggestions

### **For Ebbinghaus Curve:**
```python
import matplotlib.pyplot as plt
import numpy as np

# Ebbinghaus's actual data points
time_points = [0, 20/60/24, 1/24, 9/24, 1, 2, 6, 31]  # in days
retention = [100, 60, 45, 35, 34, 30, 25, 21]  # percentage

# Our decay function
days = np.linspace(0, 31, 1000)
lambda_val = 0.002
decay = 100 * np.exp(-lambda_val * days)

plt.figure(figsize=(10, 6))
plt.plot(time_points, retention, 'ro-', label='Ebbinghaus (1885)', markersize=8)
plt.plot(days, decay, 'b-', label='Our Implementation', linewidth=2)
plt.xlabel('Time (days)')
plt.ylabel('Memory Retention (%)')
plt.title('The Ebbinghaus Forgetting Curve: 1885 vs 2025')
plt.legend()
plt.grid(True, alpha=0.3)
plt.savefig('ebbinghaus_comparison.png', dpi=300, bbox_inches='tight')
```

### **For Architecture Diagram:**
- Use draw.io or similar tool
- Show Kafka as central nervous system
- Color-code different worker types
- Include data flow arrows with labels

### **For Demo Screenshots:**
- Capture Streamlit UI in action
- Show memory beats with different ages
- Highlight activation score changes
- Include time advancement commands

## 📁 File Naming Convention

- Use descriptive names: `ebbinghaus_forgetting_curve.png`
- Include resolution in filename if multiple sizes: `architecture_overview_1920x1080.png`
- Use PNG for diagrams, JPG for photos
- Keep file sizes reasonable for presentations (< 2MB each)

## 🎯 Usage in Presentation

### **Slide Integration:**
- Reference images in presentation outline
- Use as visual anchors for key concepts
- Include in demo backup slides

### **Demo Enhancement:**
- Show Ebbinghaus portrait when introducing historical context
- Display forgetting curve during decay explanation
- Use architecture diagram during technical deep dive

## 🔍 Image Sources

### **Historical Images:**
- Wikimedia Commons (public domain)
- Psychology textbook archives
- Academic paper illustrations

### **Technical Diagrams:**
- Create custom diagrams matching our system
- Use consistent color scheme and fonts
- Ensure high resolution for projection

### **Screenshots:**
- Capture from actual running system
- Use realistic demo data
- Highlight key UI elements

## 📊 Recommended Tools

### **Diagram Creation:**
- **Draw.io**: Free, web-based, great for architecture diagrams
- **Lucidchart**: Professional diagramming tool
- **Figma**: Modern design tool with collaboration features

### **Graph/Chart Creation:**
- **Python + Matplotlib**: Programmatic, reproducible charts
- **Excel/Google Sheets**: Quick charts with export options
- **D3.js**: Interactive web-based visualizations

### **Screenshot Tools:**
- **macOS**: Cmd+Shift+4 for selection screenshots
- **CleanShot X**: Professional screenshot tool with annotations
- **Snagit**: Cross-platform with editing features

## 🎨 Visual Style Guide

### **Colors:**
- **Primary**: #2E86AB (blue) - for system components
- **Secondary**: #A23B72 (purple) - for memory/psychological elements  
- **Accent**: #F18F01 (orange) - for highlights and callouts
- **Neutral**: #C73E1D (red) - for warnings/decay

### **Typography:**
- **Headers**: Bold, sans-serif (Arial, Helvetica)
- **Body**: Regular, readable (Arial, Calibri)
- **Code**: Monospace (Courier New, Monaco)

### **Layout:**
- Clean, minimal design
- Consistent spacing and alignment
- High contrast for projection
- Large fonts (minimum 24pt for text)

---

*This directory structure will make your presentation visually compelling and professionally polished! 🎯*

