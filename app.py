import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv("sentiment_results.csv")

st.title("YouTube Sentiment Analysis Dashboard")

st.subheader("Data Preview")
st.dataframe(df)

st.subheader("Sentiment Distribution")
st.bar_chart(df['Sentiment'].value_counts())

st.subheader("Sample Comments")
st.write(df[['Comment', 'Sentiment']].head(10))