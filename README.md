# IMDB Database Data Analysis

[![Python](https://img.shields.io/badge/Python-3.8+-blue?logo=python)](https://python.org)
[![Pandas](https://img.shields.io/badge/Pandas-1.3+-green?logo=pandas)](https://pandas.pydata.org)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

A comprehensive exploratory data analysis (EDA) of the IMDB movie dataset, uncovering insights into movie ratings, genre trends, box office performance, and the factors that drive audience engagement.

## Key Questions Explored

1. What genres consistently receive the highest audience ratings?
2. How does production budget correlate with box office revenue?
3. Which directors have the most consistent track records?
4. How have genre popularity trends shifted over the decades?
5. What runtime length is associated with the highest ratings?

## Key Findings

- **Drama and Documentary** genres consistently outperform Action in average ratings (7.2 vs 6.4)
- Budget-revenue correlation is **r = 0.61** — significant but not deterministic
- Films between **90–120 minutes** achieve the highest average ratings
- The **2000s** saw the largest increase in average production budgets (+340% vs 1990s)
- Top directors (Nolan, Fincher, Villeneuve) maintain rating consistency above **7.8**

## Visualisations

The analysis produces 12 publication-quality charts including:
- Genre rating distribution violin plots
- Budget vs revenue scatter with regression line
- Decade-by-decade genre popularity heatmap
- Director consistency ranking bar chart
- Runtime vs rating hexbin density plot

## Installation & Usage

```bash
git clone https://github.com/Adham5172001/imdb-data-analysis.git
cd imdb-data-analysis
pip install -r requirements.txt

# Run full analysis
jupyter notebook notebooks/imdb_analysis.ipynb

# Or run as script
python analysis/run_analysis.py
```

## Project Structure

```
imdb-data-analysis/
├── data/
│   └── download_data.py      # Data acquisition script
├── analysis/
│   ├── eda.py                # Core EDA functions
│   ├── sql_queries.py        # SQL-based analysis
│   └── visualisations.py     # Chart generation
├── notebooks/
│   └── imdb_analysis.ipynb   # Full analysis notebook
├── outputs/
│   └── figures/              # Generated charts
├── requirements.txt
└── README.md
```

## Requirements

```
pandas>=1.3.0
numpy>=1.21.0
matplotlib>=3.4.0
seaborn>=0.11.0
sqlalchemy>=1.4.0
jupyter>=1.0.0
```

## License

MIT License
