"""
IMDB SQL Analysis using SQLite
Author: Adham Aboulkheir | University of Essex
"""
import sqlite3
import pandas as pd
import numpy as np
import os
import sys
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from analysis.eda import generate_imdb_data


def create_imdb_database(df: pd.DataFrame, db_path: str = ":memory:") -> sqlite3.Connection:
    """Create SQLite database from IMDB dataframe."""
    conn = sqlite3.connect(db_path)
    df.to_sql("movies", conn, if_exists="replace", index=False)
    return conn


def run_analysis_queries(conn: sqlite3.Connection) -> dict:
    """Run a series of analytical SQL queries."""
    results = {}

    # Top genres by average rating
    results["top_genres"] = pd.read_sql_query("""
        SELECT genre,
               ROUND(AVG(rating), 3) AS avg_rating,
               COUNT(*) AS film_count,
               ROUND(AVG(budget_m), 1) AS avg_budget_m
        FROM movies
        GROUP BY genre
        HAVING film_count >= 50
        ORDER BY avg_rating DESC
        LIMIT 10
    """, conn)

    # Decade trends
    results["decade_trends"] = pd.read_sql_query("""
        SELECT decade,
               ROUND(AVG(rating), 3) AS avg_rating,
               COUNT(*) AS film_count,
               ROUND(AVG(runtime), 0) AS avg_runtime_min
        FROM movies
        GROUP BY decade
        ORDER BY decade
    """, conn)

    # Budget vs revenue analysis
    results["budget_analysis"] = pd.read_sql_query("""
        SELECT
            CASE
                WHEN budget_m < 10  THEN 'Low (<$10M)'
                WHEN budget_m < 50  THEN 'Mid ($10-50M)'
                WHEN budget_m < 150 THEN 'High ($50-150M)'
                ELSE 'Blockbuster (>$150M)'
            END AS budget_tier,
            COUNT(*) AS count,
            ROUND(AVG(rating), 3) AS avg_rating,
            ROUND(AVG(revenue_m / budget_m), 2) AS avg_roi
        FROM movies
        GROUP BY budget_tier
        ORDER BY avg_roi DESC
    """, conn)

    # Director consistency
    results["director_stats"] = pd.read_sql_query("""
        SELECT director,
               COUNT(*) AS film_count,
               ROUND(AVG(rating), 3) AS avg_rating,
               ROUND(MIN(rating), 2) AS min_rating,
               ROUND(MAX(rating), 2) AS max_rating
        FROM movies
        GROUP BY director
        HAVING film_count >= 5
        ORDER BY avg_rating DESC
    """, conn)

    return results


if __name__ == "__main__":
    print("IMDB SQL Analysis Demo")
    print("=" * 45)

    df = generate_imdb_data(n=5000)
    conn = create_imdb_database(df)

    results = run_analysis_queries(conn)

    print("\nTop Genres by Rating:")
    print(results["top_genres"].to_string(index=False))

    print("\nDecade Trends:")
    print(results["decade_trends"].to_string(index=False))

    print("\nBudget Tier Analysis:")
    print(results["budget_analysis"].to_string(index=False))

    print("\nTop Directors:")
    print(results["director_stats"].head(5).to_string(index=False))

    conn.close()
