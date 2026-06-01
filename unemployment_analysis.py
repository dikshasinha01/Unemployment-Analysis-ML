import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("Unemployment in India.csv")

# Dataset Preview
print("First 5 Rows:")
print(df.head())

print("\nColumn Names:")
print(df.columns)

print("\nDataset Info:")
print(df.info())

# Missing Values
print("\nMissing Values:")
print(df.isnull().sum())

# Data Cleaning
df = df.dropna()

print("\nDataset Shape After Cleaning:")
print(df.shape)

# Convert Date Column
df[' Date'] = pd.to_datetime(df[' Date'], dayfirst=True)


# Unemployment Trend Graph

plt.figure(figsize=(12, 5))
plt.plot(df[' Date'], df[' Estimated Unemployment Rate (%)'])

plt.title("Unemployment Rate Over Time")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.grid(True)

plt.savefig("unemployment_trend.png")
plt.close()

print("\nUnemployment Trend Graph saved as unemployment_trend.png")


# State-wise Analysis

state_avg = df.groupby("Region")[
    " Estimated Unemployment Rate (%)"
].mean()

# Highest and Lowest States
print("\nTop 5 States with Highest Unemployment:")
print(state_avg.sort_values(ascending=False).head())

print("\nTop 5 States with Lowest Unemployment:")
print(state_avg.sort_values().head())


# State-wise Bar Chart

plt.figure(figsize=(10, 8))

state_avg.sort_values().plot(kind="barh")

plt.title("Average Unemployment Rate by State")
plt.xlabel("Unemployment Rate (%)")

plt.savefig("statewise_unemployment.png")
plt.close()

print("\nState-wise Graph saved as statewise_unemployment.png")


# Conclusions

print("\n==============================")
print("PROJECT INSIGHTS")
print("==============================")
print("1. Data was cleaned by removing missing values.")
print("2. Unemployment rates vary significantly across states.")
print("3. Tripura and Haryana show high unemployment rates.")
print("4. Meghalaya and Odisha show low unemployment rates.")
print("5. Data visualization helps identify employment trends.")