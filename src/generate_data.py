"""Generate synthetic Superstore-style sales data."""
import pandas as pd
import numpy as np
from pathlib import Path

np.random.seed(42)

categories = {
    "Furniture": {
        "Bookcases": (200, 1500, -0.05),   # (avg_price, max, profit_margin_mean)
        "Chairs": (100, 800, 0.10),
        "Furnishings": (20, 200, 0.15),
        "Tables": (300, 2000, -0.15),
    },
    "Office Supplies": {
        "Appliances": (50, 500, 0.08),
        "Art": (10, 80, 0.20),
        "Binders": (15, 150, 0.12),
        "Envelopes": (5, 50, 0.30),
        "Fasteners": (5, 30, 0.25),
        "Labels": (10, 60, 0.40),
        "Paper": (20, 100, 0.30),
        "Storage": (40, 400, 0.10),
        "Supplies": (15, 150, 0.15),
    },
    "Technology": {
        "Accessories": (30, 250, 0.20),
        "Copiers": (500, 5000, 0.30),
        "Machines": (300, 3000, 0.05),
        "Phones": (200, 1500, 0.18),
    },
}

regions = ["West", "East", "Central", "South"]
region_probs = [0.32, 0.28, 0.23, 0.17]
segments = ["Consumer", "Corporate", "Home Office"]
seg_probs = [0.52, 0.30, 0.18]
ship_modes = ["Standard Class", "Second Class", "First Class", "Same Day"]
ship_probs = [0.60, 0.20, 0.15, 0.05]

N = 9994
rows = []
for i in range(1, N + 1):
    category = np.random.choice(list(categories.keys()), p=[0.33, 0.45, 0.22])
    sub = np.random.choice(list(categories[category].keys()))
    avg_price, max_price, margin = categories[category][sub]

    qty = np.random.choice([1, 2, 3, 4, 5, 6, 7], p=[0.25, 0.2, 0.15, 0.15, 0.1, 0.1, 0.05])
    unit_price = np.random.uniform(avg_price * 0.5, max_price * 0.7)
    sales = round(unit_price * qty, 2)

    discount = np.random.choice([0, 0.1, 0.15, 0.2, 0.3, 0.4, 0.5], p=[0.5, 0.15, 0.1, 0.1, 0.07, 0.05, 0.03])
    sales = round(sales * (1 - discount), 2)
    base_profit = sales * margin
    profit = round(base_profit - sales * discount * 0.5, 2)

    days_back = np.random.randint(0, 1460)
    order_date = pd.Timestamp("2024-12-31") - pd.Timedelta(days=days_back)
    ship_mode = np.random.choice(ship_modes, p=ship_probs)
    ship_days = {"Standard Class": 5, "Second Class": 3, "First Class": 2, "Same Day": 0}[ship_mode]
    ship_date = order_date + pd.Timedelta(days=ship_days + np.random.randint(0, 3))

    rows.append({
        "Order ID": f"US-2024-{100000 + i}",
        "Order Date": order_date.strftime("%Y-%m-%d"),
        "Ship Date": ship_date.strftime("%Y-%m-%d"),
        "Ship Mode": ship_mode,
        "Customer ID": f"CG-{np.random.randint(10000, 99999)}",
        "Segment": np.random.choice(segments, p=seg_probs),
        "Region": np.random.choice(regions, p=region_probs),
        "Category": category,
        "Sub-Category": sub,
        "Sales": sales,
        "Quantity": qty,
        "Discount": discount,
        "Profit": profit,
    })

if __name__ == "__main__":
    df = pd.DataFrame(rows)
    out = Path(__file__).resolve().parents[1] / "data" / "superstore.csv"
    out.parent.mkdir(exist_ok=True)
    df.to_csv(out, index=False)
    print(f"✅ Generated {len(df):,} orders → {out}")
