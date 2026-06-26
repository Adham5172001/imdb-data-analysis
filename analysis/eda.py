"""IMDB Data Analysis — Author: Adham Aboulkheir | University of Essex"""
import numpy as np
import pandas as pd

def generate_imdb_data(n=5000, seed=42):
    np.random.seed(seed)
    genres = ["Drama","Documentary","Biography","Crime","Adventure","Comedy","Action","Horror","Thriller","Romance"]
    directors = ["Christopher Nolan","David Fincher","Denis Villeneuve","Quentin Tarantino","Martin Scorsese"]
    years = np.random.randint(1960, 2024, n)
    budgets = np.random.lognormal(3.5, 1.2, n)
    return pd.DataFrame({
        "title": [f"Movie_{i}" for i in range(n)],
        "genre": np.random.choice(genres, n),
        "director": np.random.choice(directors, n),
        "year": years, "decade": (years//10)*10,
        "rating": np.clip(np.random.normal(6.8, 1.1, n), 1.0, 10.0),
        "votes": np.random.lognormal(10, 2, n).astype(int),
        "budget_m": budgets,
        "revenue_m": budgets*(1.5+np.random.exponential(1.5, n))*np.random.uniform(0.3, 3.0, n),
        "runtime": np.random.normal(105, 25, n).clip(60, 240).astype(int),
    })

def genre_analysis(df):
    return df.groupby("genre").agg(mean_rating=("rating","mean"), count=("rating","count")).sort_values("mean_rating", ascending=False)

def budget_revenue_analysis(df):
    correlation = df["budget_m"].corr(df["revenue_m"])
    roi = (df["revenue_m"] - df["budget_m"]) / df["budget_m"]
    return {"correlation": float(correlation), "mean_roi": float(roi.mean()), "profitable_pct": float((roi>0).mean())}

if __name__ == "__main__":
    df = generate_imdb_data(n=5000)
    print(f"Dataset: {len(df)} movies | Avg rating: {df.rating.mean():.2f}")
    print("\nTop genres:")
    print(genre_analysis(df).head(5)[["mean_rating","count"]].to_string())
    ba = budget_revenue_analysis(df)
    print(f"\nBudget-Revenue correlation: {ba['correlation']:.3f}")
    print(f"Profitable films: {ba['profitable_pct']:.1%}")
