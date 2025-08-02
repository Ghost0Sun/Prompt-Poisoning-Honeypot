import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("🐝 Prompt Poisoning Honeypot Dashboard")

df = pd.read_csv("data/attacks_log.csv")

st.subheader("Recent Captured Attacks")
st.dataframe(df.tail(10))

st.subheader("Attack Frequency Over Time")
df['timestamp'] = pd.to_datetime(df['timestamp'])
df['date'] = df['timestamp'].dt.date
attack_counts = df.groupby('date').size()

fig, ax = plt.subplots()
attack_counts.plot(kind='bar', ax=ax)
st.pyplot(fig)
