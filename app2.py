import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# PAGE CONFIG


st.set_page_config(
    page_title="Unemployment Analysis",
    page_icon="📉",
    layout="wide"
)


# CUSTOM CSS


st.markdown("""
<style>

.main {
    background-color: #f4f6f9;
}

.title {
    text-align: center;
    font-size: 45px;
    font-weight: bold;
    color: #ff6b6b;
}

.subtitle {
    text-align: center;
    font-size: 20px;
    color: gray;
    margin-bottom: 25px;
}

.card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 0px 12px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}

</style>
""", unsafe_allow_html=True)


# TITLE


st.markdown(
    '<p class="title">📉 Unemployment Analysis Dashboard</p>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">Data Analysis using Streamlit</p>',
    unsafe_allow_html=True
)


# LOAD DATASET


df = pd.read_csv("Unemployment in India.csv")


# DATASET OVERVIEW


st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("📊 Dataset Overview")

st.write("Dataset Shape:")

st.write(df.shape)

st.write("First 10 Rows")

st.dataframe(df.head(10))

st.write("Column Names")

st.write(df.columns)

st.write("Dataset Description")

st.write(df.describe())

st.markdown('</div>', unsafe_allow_html=True)


# MISSING VALUES


st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("🔍 Missing Values")

st.write(df.isnull().sum())

st.markdown('</div>', unsafe_allow_html=True)


# DATA CLEANING


df = df.dropna()


# DATE CONVERSION


df[' Date'] = pd.to_datetime(
    df[' Date'],
    dayfirst=True
)


# CLEANED DATASET INFO


st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("🧹 Dataset After Cleaning")

st.write("Dataset Shape After Cleaning")

st.write(df.shape)

st.markdown('</div>', unsafe_allow_html=True)


# UNEMPLOYMENT TREND


st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("📈 Unemployment Trend Over Time")

fig1, ax1 = plt.subplots(figsize=(12,5))

ax1.plot(
    df[' Date'],
    df[' Estimated Unemployment Rate (%)']
)

ax1.set_xlabel("Date")

ax1.set_ylabel("Unemployment Rate (%)")

ax1.grid(True)

st.pyplot(fig1)

st.markdown('</div>', unsafe_allow_html=True)


# STATE-WISE ANALYSIS


state_avg = df.groupby("Region")[
    " Estimated Unemployment Rate (%)"
].mean()


# HIGHEST UNEMPLOYMENT STATES


col1, col2 = st.columns(2)

with col1:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("🚨 Highest Unemployment States")

    highest_states = state_avg.sort_values(
        ascending=False
    ).head()

    st.write(highest_states)

    st.markdown('</div>', unsafe_allow_html=True)


# LOWEST UNEMPLOYMENT STATES


with col2:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("✅ Lowest Unemployment States")

    lowest_states = state_avg.sort_values().head()

    st.write(lowest_states)

    st.markdown('</div>', unsafe_allow_html=True)


# STATE-WISE BAR CHART


st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("📊 Average Unemployment Rate by State")

fig2, ax2 = plt.subplots(figsize=(10,8))

state_avg.sort_values().plot(
    kind="barh",
    ax=ax2
)

ax2.set_xlabel("Unemployment Rate (%)")

st.pyplot(fig2)

st.markdown('</div>', unsafe_allow_html=True)


# HEATMAP


st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("🔥 Correlation Heatmap")

numeric_df = df.select_dtypes(include=['float64', 'int64'])

fig3, ax3 = plt.subplots(figsize=(8,6))

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap='coolwarm',
    ax=ax3
)

st.pyplot(fig3)

st.markdown('</div>', unsafe_allow_html=True)


# REGION SELECTION


st.sidebar.header("📍 Select Region")

selected_region = st.sidebar.selectbox(
    "Choose Region",
    df["Region"].unique()
)

filtered_df = df[
    df["Region"] == selected_region
]


# REGION DATA


st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader(f"📌 Data for {selected_region}")

st.dataframe(filtered_df.head(10))

st.markdown('</div>', unsafe_allow_html=True)


# REGION TREND VISUALIZATION


st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("📉 Region-wise Trend")

fig4, ax4 = plt.subplots(figsize=(10,5))

ax4.plot(
    filtered_df[' Date'],
    filtered_df[' Estimated Unemployment Rate (%)']
)

ax4.set_xlabel("Date")

ax4.set_ylabel("Unemployment Rate (%)")

ax4.grid(True)

st.pyplot(fig4)

st.markdown('</div>', unsafe_allow_html=True)


# PROJECT INSIGHTS


st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("📚 Project Insights")

st.write("1. Data was cleaned by removing missing values.")

st.write("2. Unemployment rates vary significantly across states.")

st.write("3. Some states show very high unemployment trends.")

st.write("4. Some states maintain comparatively low unemployment.")

st.write("5. Visualization helps identify employment patterns.")

st.markdown('</div>', unsafe_allow_html=True)


# FOOTER


st.markdown("""
<hr>

""", unsafe_allow_html=True)