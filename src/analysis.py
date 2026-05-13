"""
Superstore Sales Analysis
==========================
Performance and profitability deep-dive.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

sns.set_style("whitegrid")


def load(filepath: str) -> pd.DataFrame:
    df = pd.read_csv(filepath, parse_dates=["Order Date", "Ship Date"])
    df["Year"] = df["Order Date"].dt.year
    df["Month"] = df["Order Date"].dt.month
    df["ShipDuration"] = (df["Ship Date"] - df["Order Date"]).dt.days
    print(f"✅ Loaded {len(df):,} orders")
    return df


def profit_by_subcategory(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("Sub-Category")
        .agg(Sales=("Sales", "sum"), Profit=("Profit", "sum"), Orders=("Order ID", "count"))
        .assign(Margin=lambda x: (x["Profit"] / x["Sales"] * 100).round(1))
        .sort_values("Profit")
    )


def profit_by_region(df: pd.DataFrame) -> pd.DataFrame:
    return df.groupby("Region").agg(Sales=("Sales", "sum"), Profit=("Profit", "sum"))


def discount_vs_profit(df: pd.DataFrame) -> pd.DataFrame:
    """How average profit changes by discount band."""
    df = df.copy()
    df["DiscountBand"] = pd.cut(
        df["Discount"],
        bins=[-0.001, 0.0, 0.1, 0.2, 0.3, 0.5, 1.0],
        labels=["0%", "1-10%", "11-20%", "21-30%", "31-50%", ">50%"],
    )
    return df.groupby("DiscountBand", observed=True).agg(
        AvgProfit=("Profit", "mean"),
        Orders=("Order ID", "count"),
    )


def plot_subcategory_profit(s: pd.DataFrame, save_path: str = None):
    fig, ax = plt.subplots(figsize=(10, 7))
    colors = ["crimson" if p < 0 else "seagreen" for p in s["Profit"]]
    ax.barh(s.index, s["Profit"], color=colors)
    ax.set_title("Profit by Sub-Category", fontweight="bold")
    ax.set_xlabel("Profit ($)")
    ax.axvline(0, color="black", linewidth=0.8)
    plt.tight_layout()
    if save_path:
        plt.savefig(save_path, dpi=150)
    plt.show()


def main():
    root = Path(__file__).resolve().parents[1]
    df = load(str(root / "data" / "superstore.csv"))

    print("\n📦 PROFIT BY SUB-CATEGORY (sorted ascending):")
    sub = profit_by_subcategory(df)
    print(sub)

    print("\n🌎 PROFIT BY REGION:")
    print(profit_by_region(df))

    print("\n🎁 DISCOUNT vs PROFIT:")
    print(discount_vs_profit(df))

    images = root / "images"
    images.mkdir(exist_ok=True)
    plot_subcategory_profit(sub, str(images / "subcat_profit.png"))


if __name__ == "__main__":
    main()
