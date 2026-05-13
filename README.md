# 🏬 Superstore Sales Performance Analytics

A comprehensive sales & profitability analysis of a global superstore — covering 4 years of orders across regions, categories, and customer segments.

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## 🎯 Project Overview

This project performs a deep-dive on Superstore sales data to identify:
- 💰 **Profit drivers and drains**
- 🌍 **Regional performance**
- 📦 **Best & worst sub-categories**
- 🚚 **Shipping & discount impact on profit**

## 🔍 Key Questions

1. Which sub-categories are unprofitable despite high sales?
2. How do discounts erode profit?
3. Which regions/segments are most profitable?
4. Are there seasonal patterns in sales?

## 📁 Structure

```
superstore-sales/
├── data/
│   └── superstore.csv
├── notebooks/
│   └── superstore_analysis.ipynb
├── src/
│   ├── analysis.py
│   └── generate_data.py
├── outputs/
├── images/
├── requirements.txt
└── README.md
```

## 🛠️ Tech Stack

Python · Pandas · Matplotlib · Seaborn · Plotly

## 🚀 Run

```bash
git clone https://github.com/yourusername/superstore-sales.git
cd superstore-sales
pip install -r requirements.txt
python src/generate_data.py
python src/analysis.py
```

## 📈 Key Insights

- 💸 **Tables** sub-category loses money despite strong sales (high discount rate)
- 🌍 **West** region most profitable; **Central** least
- 🛒 **Consumer** segment generates most revenue, **Corporate** highest margin
- 🎁 **Discounts >20%** consistently produce negative margin

## 📝 License

[MIT](LICENSE)
