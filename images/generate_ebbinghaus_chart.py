#!/usr/bin/env python3
"""
Generate Ebbinghaus Forgetting Curve visualization for presentation.
Shows original 1885 data vs our 2025 implementation.
"""

import matplotlib.pyplot as plt
import numpy as np
from pathlib import Path

def create_ebbinghaus_comparison():
    """Create the Ebbinghaus forgetting curve comparison chart."""
    
    # Ebbinghaus's actual data points (converted to days)
    time_points = [
        0,           # Immediate
        20/60/24,    # 20 minutes
        1/24,        # 1 hour  
        9/24,        # 9 hours
        1,           # 1 day
        2,           # 2 days
        6,           # 6 days
        31           # 31 days
    ]
    retention_percent = [100, 60, 45, 35, 34, 30, 25, 21]
    
    # Our decay function implementation
    days = np.linspace(0, 31, 1000)
    lambda_val = 0.002  # Same as in resonance worker
    our_decay = 100 * np.exp(-lambda_val * days)
    
    # Create the plot
    plt.figure(figsize=(12, 8))
    
    # Plot Ebbinghaus's original data
    plt.plot(time_points, retention_percent, 'ro-', 
             label='Ebbinghaus (1885)', markersize=10, linewidth=3)
    
    # Plot our implementation
    plt.plot(days, our_decay, 'b-', 
             label='Our AI Implementation (λ=0.002)', linewidth=3)
    
    # Styling
    plt.xlabel('Time (days)', fontsize=14, fontweight='bold')
    plt.ylabel('Memory Retention (%)', fontsize=14, fontweight='bold')
    plt.title('The Ebbinghaus Forgetting Curve: 1885 vs 2025\n' + 
              'Psychological Realism in AI Memory Systems', 
              fontsize=16, fontweight='bold', pad=20)
    
    plt.legend(fontsize=12, loc='upper right')
    plt.grid(True, alpha=0.3)
    
    # Add annotations for key points
    plt.annotate('100% (Immediate)', xy=(0, 100), xytext=(2, 95),
                arrowprops=dict(arrowstyle='->', color='red', alpha=0.7),
                fontsize=10, color='red')
    
    plt.annotate('60% (20 min)', xy=(20/60/24, 60), xytext=(1, 70),
                arrowprops=dict(arrowstyle='->', color='red', alpha=0.7),
                fontsize=10, color='red')
    
    plt.annotate('34% (1 day)', xy=(1, 34), xytext=(3, 45),
                arrowprops=dict(arrowstyle='->', color='red', alpha=0.7),
                fontsize=10, color='red')
    
    # Set axis limits and ticks
    plt.xlim(-0.5, 32)
    plt.ylim(0, 105)
    
    # Custom x-axis labels for better readability
    x_ticks = [0, 1/24, 1, 2, 7, 14, 31]
    x_labels = ['0', '1h', '1d', '2d', '1w', '2w', '1m']
    plt.xticks(x_ticks, x_labels)
    
    plt.tight_layout()
    
    # Save the chart
    output_path = Path(__file__).parent / 'ebbinghaus_comparison.png'
    plt.savefig(output_path, dpi=300, bbox_inches='tight', 
                facecolor='white', edgecolor='none')
    
    print(f"✅ Ebbinghaus comparison chart saved to: {output_path}")
    
    # Also create a version showing our decay function parameters
    plt.figure(figsize=(12, 6))
    
    # Show different lambda values
    lambdas = [0.001, 0.002, 0.005, 0.01]
    colors = ['blue', 'green', 'orange', 'red']
    
    for i, lam in enumerate(lambdas):
        decay = 100 * np.exp(-lam * days)
        plt.plot(days, decay, color=colors[i], linewidth=2, 
                label=f'λ = {lam} ({"slow" if lam < 0.003 else "fast"} forgetting)')
    
    # Add Ebbinghaus data for reference
    plt.plot(time_points, retention_percent, 'ko-', 
             label='Ebbinghaus (1885)', markersize=8, alpha=0.7)
    
    plt.xlabel('Time (days)', fontsize=14, fontweight='bold')
    plt.ylabel('Memory Retention (%)', fontsize=14, fontweight='bold')
    plt.title('Tuning Memory Decay: Different λ (Lambda) Values\n' + 
              'Configurable Forgetting Rates in Our System', 
              fontsize=16, fontweight='bold', pad=20)
    
    plt.legend(fontsize=11, loc='upper right')
    plt.grid(True, alpha=0.3)
    plt.xlim(0, 31)
    plt.ylim(0, 105)
    plt.xticks(x_ticks, x_labels)
    
    plt.tight_layout()
    
    # Save the parameter comparison
    param_path = Path(__file__).parent / 'decay_parameters.png'
    plt.savefig(param_path, dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    
    print(f"✅ Decay parameters chart saved to: {param_path}")

def create_activation_timeline():
    """Create activation score timeline visualization."""
    
    # Simulate memory activation over time
    days = np.linspace(0, 30, 100)
    
    # Different memory types with different salience
    normal_memory = 0.8 * np.exp(-0.002 * days)  # Normal salience
    emotional_memory = 1.2 * np.exp(-0.002 * days)  # High emotional salience
    repeated_memory = 0.8 * np.exp(-0.001 * days)  # Repeated/reinforced (slower decay)
    
    plt.figure(figsize=(12, 8))
    
    plt.plot(days, normal_memory, 'b-', linewidth=3, 
             label='Normal Memory (salience=0.8)')
    plt.plot(days, emotional_memory, 'r-', linewidth=3, 
             label='Emotional Memory (salience=1.2)')
    plt.plot(days, repeated_memory, 'g-', linewidth=3, 
             label='Reinforced Memory (slower decay)')
    
    # Add threshold line
    plt.axhline(y=0.3, color='gray', linestyle='--', alpha=0.7, 
                label='Recall Threshold')
    
    plt.xlabel('Time (days)', fontsize=14, fontweight='bold')
    plt.ylabel('Activation Score', fontsize=14, fontweight='bold')
    plt.title('Memory Activation Over Time\n' + 
              'How Salience and Reinforcement Affect Retention', 
              fontsize=16, fontweight='bold', pad=20)
    
    plt.legend(fontsize=12, loc='upper right')
    plt.grid(True, alpha=0.3)
    plt.xlim(0, 30)
    plt.ylim(0, 1.3)
    
    # Add annotations
    plt.annotate('Emotional memories\nresist forgetting', 
                xy=(15, emotional_memory[50]), xytext=(20, 1.0),
                arrowprops=dict(arrowstyle='->', color='red', alpha=0.7),
                fontsize=11, color='red', ha='center')
    
    plt.tight_layout()
    
    # Save the activation timeline
    activation_path = Path(__file__).parent / 'activation_timeline.png'
    plt.savefig(activation_path, dpi=300, bbox_inches='tight',
                facecolor='white', edgecolor='none')
    
    print(f"✅ Activation timeline chart saved to: {activation_path}")

if __name__ == "__main__":
    print("🎨 Generating Ebbinghaus presentation charts...")
    
    # Set matplotlib style for better presentation visuals
    plt.style.use('default')
    plt.rcParams['font.size'] = 12
    plt.rcParams['axes.linewidth'] = 1.5
    plt.rcParams['grid.alpha'] = 0.3
    
    create_ebbinghaus_comparison()
    create_activation_timeline()
    
    print("\n🎯 All charts generated successfully!")
    print("📁 Files created in images/ directory:")
    print("   - ebbinghaus_comparison.png")
    print("   - decay_parameters.png") 
    print("   - activation_timeline.png")
    print("\n💡 Use these in your presentation slides for maximum impact!")

