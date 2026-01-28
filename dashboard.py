# Interactive Sales Dashboard
# Simple & Beginner Friendly

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import os

# Create visualization folder if not exists
os.makedirs("visualizations", exist_ok=True)

# Load data
try:
    df = pd.read_csv("sales_data.csv")
except FileNotFoundError:
    print("❌ sales_data.csv not found!")
    exit()

# Clean column names
df.columns = df.columns.str.strip()

# Convert date column
df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")

# -----------------------------
# 1️⃣ SALES TREND (Line Chart)
# -----------------------------
sales_trend = df.groupby(df["Order_Date"].dt.month)["Sales"].sum()

plt.figure()
sales_trend.plot(marker="o")
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Total Sales")
plt.savefig("visualizations/sales_trend.png")
plt.show()

# -----------------------------
# 2️⃣ BOX PLOT (Category vs Sales)
# -----------------------------
plt.figure()
sns.boxplot(x="Category", y="Sales", data=df)
plt.title("Sales Distribution by Category")
plt.savefig("visualizations/category_boxplot.png")
plt.show()

# -----------------------------
# 3️⃣ VIOLIN PLOT
# -----------------------------
plt.figure()
sns.violinplot(x="Category", y="Sales", data=df)
plt.title("Sales Violin Plot")
plt.show()

# -----------------------------
# 4️⃣ CORRELATION HEATMAP
# -----------------------------
plt.figure()
corr = df[["Sales", "Quantity"]].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm")
plt.title("Correlation Heatm
