
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
import pickle

st.set_page_config(page_title="Scotland Birth Forecast", layout="wide")

st.title("📈 Scotland Monthly Birth Forecast Dashboard")

# Load model results from .pkl file
with open("model_results.pkl", "rb") as f:
    model_results = pickle.load(f)

# Select a model
model_choice = st.selectbox("Choose a Forecasting Model", list(model_results.keys()))
selected_df = model_results[model_choice]

# Plot
st.subheader(f"📊 Actual vs Predicted Births – {model_choice}")
fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(selected_df['date'], selected_df['actual'], label='Actual', linewidth=2)
ax.plot(selected_df['date'], selected_df['predicted'], label='Predicted', linestyle='--')
ax.set_xlabel("Date")
ax.set_ylabel("Monthly Births")
ax.set_title(f"{model_choice} Forecast")
ax.legend()
ax.grid(True)
st.pyplot(fig)

# Show table
st.subheader("📋 Forecast Data Table")
st.dataframe(selected_df)

# Download button
csv = selected_df.to_csv(index=False).encode('utf-8')
st.download_button("📥 Download CSV", csv, f"{model_choice}_forecast.csv", "text/csv")
