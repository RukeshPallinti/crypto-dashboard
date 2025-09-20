# ------------------------------------------
# Cryptocurrency Dashboard (INR) – Top 50 Coins
# Streamlit dashboard showcasing prices, volatility, and market cap
# ------------------------------------------

import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# -----------------------------
# 1. Load and Clean Data
# -----------------------------
df = pd.read_csv("crypto_cleaned_inr.csv")

# Remove rows with missing or zero values in key columns
df = df.dropna(subset=["price_in_inr", "trading_volume_inr", "market_cap"])
df = df[df["price_in_inr"] > 0]

# Create new features for analysis
df["trading_volume_millions"] = df["trading_volume_inr"] / 1_000_000
df["log_price"] = np.log(df["price_in_inr"])
df["volatility_score"] = df["price_change_percentage_24h"].abs()

# -----------------------------
# 2. Select Top 50 Coins by Market Cap
# -----------------------------
TOP_N = 50
top_coins = df.nlargest(TOP_N, "market_cap")

# -----------------------------
# 3. Dashboard Title
# -----------------------------
st.title("📊 Cryptocurrency Dashboard – Top 50 Coins (INR)")
st.markdown(
    "This interactive dashboard shows the top 50 cryptocurrencies by market capitalization. "
    "Explore prices, volatility, trading volume, and market share of the leading coins."
)

# -----------------------------
# 4. Key Metrics Overview
# -----------------------------
st.subheader("🔑 Key Metrics")
col1, col2, col3, col4 = st.columns(4)

# Identify the top coin by market cap
top_coin = top_coins.iloc[0]

col1.metric("Total Market Cap (INR)", f"{top_coins['market_cap'].sum():,.0f}")
col2.metric("Highest Price (INR)", f"{top_coins['price_in_inr'].max():,.2f}")
col3.metric("Most Volatile (%)", f"{top_coins['volatility_score'].max():.2f}")
col4.metric("Total Trading Volume (M INR)", f"{top_coins['trading_volume_millions'].sum():,.0f}")

st.markdown(f"**🏆 Top Coin by Market Cap:** {top_coin['coin']}")

# -----------------------------
# 5. Price Comparison
# -----------------------------
st.subheader("💰 Current Prices")
fig_price = px.bar(
    top_coins,
    x="coin",
    y="price_in_inr",
    color="coin",
    text="price_in_inr",
    title=f"Prices of Top {TOP_N} Cryptocurrencies",
    labels={"price_in_inr": "Price (INR)", "coin": "Coin"},
    color_discrete_sequence=px.colors.qualitative.Set3
)
st.plotly_chart(fig_price, use_container_width=True)

# -----------------------------
# 6. 24h Volatility
# -----------------------------
st.subheader("⚡ 24-Hour Volatility")
fig_volatility = px.bar(
    top_coins,
    x="coin",
    y="volatility_score",
    color="coin",
    text="volatility_score",
    title="Volatility in the Last 24 Hours (%)",
    labels={"volatility_score": "Volatility (%)", "coin": "Coin"},
    color_discrete_sequence=px.colors.qualitative.Set3
)
st.plotly_chart(fig_volatility, use_container_width=True)

# -----------------------------
# 7. Market Cap Distribution
# -----------------------------
st.subheader("🏛 Market Cap Share")
fig_marketcap = px.pie(
    top_coins,
    values="market_cap",
    names="coin",
    title="Market Capitalization Distribution",
    hole=0.4,
    color_discrete_sequence=px.colors.qualitative.Set3
)
st.plotly_chart(fig_marketcap, use_container_width=True)

# -----------------------------
# 8. 24h High vs Low Prices
# -----------------------------
st.subheader("📈 24h High vs Low Prices")
df_prices = top_coins.melt(
    id_vars="coin",
    value_vars=["high_24h", "low_24h"],
    var_name="Metric",
    value_name="Price (INR)"
)
fig_highlow = px.bar(
    df_prices,
    x="coin",
    y="Price (INR)",
    color="Metric",
    barmode="group",
    text="Price (INR)",
    color_discrete_map={"high_24h": "#636EFA", "low_24h": "#EF553B"}
)
st.plotly_chart(fig_highlow, use_container_width=True)

# -----------------------------
# 9. Price vs Trading Volume
# -----------------------------
st.subheader("📊 Price vs Trading Volume")
fig_scatter = px.scatter(
    top_coins,
    x="price_in_inr",
    y="trading_volume_millions",
    size="market_cap",
    color="coin",
    hover_data=["coin", "price_in_inr", "trading_volume_millions"],
    title="Price vs Trading Volume (Log Scale)",
    log_x=True,
    log_y=True,
    labels={"price_in_inr": "Price (INR)", "trading_volume_millions": "Trading Volume (M INR)"},
    color_discrete_sequence=px.colors.qualitative.Set3
)
st.plotly_chart(fig_scatter, use_container_width=True)

# -----------------------------
# 10. Feature Correlation Heatmap
# -----------------------------
st.subheader("📊 Feature Correlation Heatmap")

# Select numeric columns for correlation
numeric_cols = [
    "price_in_inr",
    "trading_volume_inr",
    "market_cap",
    "price_change_percentage_24h",
    "volatility_score"
]

corr_matrix = top_coins[numeric_cols].corr()

# Plot heatmap
fig, ax = plt.subplots(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", cbar=True, ax=ax)
st.pyplot(fig)
