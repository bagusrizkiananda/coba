import streamlit as st
import pandas as pd

# Load the dataset
@st.cache_data
def load_data():
    df = pd.read_csv("StemmingJumbo (2).csv")  # Pastikan file ini ada di root repo
    return df

df = load_data()

st.title("📊 Sentimen Analysis Viewer")
st.write("Gunakan filter di bawah ini untuk melihat data berdasarkan sentimen.")

# Deteksi nama kolom sentimen
sentiment_column = None
for col in df.columns:
    if 'sentimen' in col.lower():
        sentiment_column = col
        break

if sentiment_column is None:
    st.error("Kolom sentimen tidak ditemukan di file CSV.")
else:
    # Pilihan filter
    sentiments = df[sentiment_column].unique().tolist()
    selected_sentiment = st.selectbox("Pilih sentimen", sentiments)

    # Filter data
    filtered_data = df[df[sentiment_column] == selected_sentiment]
    st.write(f"Menampilkan {len(filtered_data)} data dengan sentimen '{selected_sentiment}':")
    st.dataframe(filtered_data)
