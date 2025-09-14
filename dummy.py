import streamlit as st
import pandas as pd
import plotly.express as px

# -------------------------
# Dummy Benchmark Dataset
# -------------------------
benchmark_data = {
    "Aluminium": {"energy_use": 200, "emissions": 150, "recycling_rate": 70},
    "Copper": {"energy_use": 250, "emissions": 180, "recycling_rate": 60}
}

# -------------------------
# App Layout
# -------------------------
st.set_page_config(page_title="Sustainable Metals Prototype", layout="centered")

st.title("🌍 Sustainable Metals LCA Prototype")
st.write("Prototype tool to compare processes with benchmarks and get recommendations")

# User Input Form
st.header("🔹 Enter Your Process Details")
metal = st.selectbox("Select Metal", list(benchmark_data.keys()))
energy_use = st.number_input("Energy Use (kWh per ton)", min_value=0, step=10)
emissions = st.number_input("Emissions (kg CO₂ per ton)", min_value=0, step=10)
recycling_rate = st.slider("Recycling Rate (%)", 0, 100, 50)

if st.button("Compare with Benchmark"):
    st.subheader(f"📊 Results for {metal}")
    
    # Get benchmarks
    bm = benchmark_data[metal]
    
    # Create dataframe for chart
    df = pd.DataFrame({
        "Category": ["Energy Use", "Emissions", "Recycling Rate"],
        "Your Input": [energy_use, emissions, recycling_rate],
        "Benchmark": [bm["energy_use"], bm["emissions"], bm["recycling_rate"]]
    })
    
    # Bar Chart
    fig = px.bar(df, x="Category", y=["Your Input", "Benchmark"], 
                 barmode="group", title="Your Process vs Benchmark")
    st.plotly_chart(fig)
    
    # Recommendations
    st.subheader("💡 Recommendations")
    if energy_use > bm["energy_use"]:
        st.write("- Reduce energy consumption by adopting renewable or efficient furnaces.")
    else:
        st.write("- Good job! Your energy use is below benchmark.")
    
    if emissions > bm["emissions"]:
        st.write("- Switch to cleaner energy sources to cut emissions.")
    else:
        st.write("- Your emissions are within sustainable limits.")
    
    if recycling_rate < bm["recycling_rate"]:
        st.write("- Improve recycling practices to reach benchmark standards.")
    else:
        st.write("- Excellent recycling practices!")

# Chatbot (simple Q&A)
st.sidebar.header("🤖 Chatbot Assistant")
user_q = st.sidebar.text_input("Ask a question (e.g., How to reduce emissions?)")
if user_q:
    if "emissions" in user_q.lower():
        st.sidebar.write("👉 Try using renewable energy and efficient processes to cut emissions.")
    elif "energy" in user_q.lower():
        st.sidebar.write("👉 Optimize machinery and consider heat recovery systems.")
    elif "recycling" in user_q.lower():
        st.sidebar.write("👉 Collaborate with scrap suppliers and set up closed-loop recycling.")
    else:
        st.sidebar.write("👉 Sorry, I don't know that yet (prototype bot).")
