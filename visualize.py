# visualize.py
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def visualize_performance(topic_performance):
    # Plot the topic performance
    plt.figure(figsize=(12, 8))
    sns.set_theme(style="whitegrid")
    ax = sns.barplot(
        x='score',
        y='topic',
        hue='topic',  # Assign the y variable to hue
        data=topic_performance.reset_index(),
        palette='mako',
        dodge=False  # No need for dodge since we use hue
    )

    # Add annotations for exact scores
    for i, row in topic_performance.iterrows():
        ax.text(
            row['score'] + 0.5, i, f"{row['score']:.1f}",
            color='black', va='center', fontsize=10
        )

    # Customize plot aesthetics
    plt.xlabel('Average Score', fontsize=12, labelpad=10)
    plt.ylabel('Topic', fontsize=12, labelpad=10)
    plt.title('Average Score by Topic', fontsize=14, fontweight='bold', pad=15)
    plt.legend([],[], frameon=False)  # Hide the legend
    plt.tight_layout()

    # Show the plot
    plt.show()