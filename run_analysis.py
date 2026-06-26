"""IMDB Analysis Pipeline — Author: Adham Aboulkheir | University of Essex"""
import numpy as np, matplotlib, os, sys
matplotlib.use("Agg")
import matplotlib.pyplot as plt
sys.path.insert(0, os.path.dirname(__file__))
from analysis.eda import generate_imdb_data, genre_analysis, budget_revenue_analysis

def main():
    print("IMDB Database Data Analysis")
    os.makedirs("outputs", exist_ok=True)
    df = generate_imdb_data(n=5000)
    genre_stats = genre_analysis(df)
    ba = budget_revenue_analysis(df)
    print(f"  {len(df)} movies | Correlation: {ba['correlation']:.3f}")
    fig, axes = plt.subplots(1, 3, figsize=(15, 4), facecolor="#0d1117")
    for ax in axes: ax.set_facecolor("#161b22")
    top = genre_stats.head(8)
    colors = ["#00c9b1" if r>=7.0 else "#58a6ff" if r>=6.5 else "#ff7b72" for r in top["mean_rating"]]
    axes[0].barh(list(top.index)[::-1], list(top["mean_rating"])[::-1], color=colors[::-1], alpha=0.85)
    axes[0].set_title("Average Rating by Genre", color="white"); axes[0].set_xlabel("Rating", color="white"); axes[0].tick_params(colors="white"); axes[0].grid(axis="x", alpha=0.3, color="#21262d"); axes[0].set_xlim(5.5, 8.0)
    sample = df.sample(500, random_state=42)
    axes[1].scatter(sample["budget_m"], sample["revenue_m"], c="#00c9b1", alpha=0.3, s=15)
    axes[1].set_xscale("log"); axes[1].set_yscale("log")
    axes[1].set_title(f"Budget vs Revenue (r={ba['correlation']:.2f})", color="white"); axes[1].set_xlabel("Budget ($M)", color="white"); axes[1].set_ylabel("Revenue ($M)", color="white"); axes[1].tick_params(colors="white"); axes[1].grid(alpha=0.3, color="#21262d")
    decade_stats = df.groupby("decade")["rating"].mean().reset_index()
    axes[2].plot(decade_stats["decade"], decade_stats["rating"], color="#00c9b1", linewidth=2.5, marker="o", markersize=7)
    axes[2].set_title("Rating by Decade", color="white"); axes[2].set_xlabel("Decade", color="white"); axes[2].tick_params(colors="white", axis="x", rotation=30); axes[2].grid(alpha=0.3, color="#21262d")
    plt.tight_layout()
    plt.savefig("outputs/imdb_results.png", dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
    print("  Saved: outputs/imdb_results.png")

if __name__ == "__main__":
    main()
