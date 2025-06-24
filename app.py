import streamlit as st
import pandas as pd
from textblob import TextBlob

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("StemmingJumbo (2).csv")
    return df

# Analisis sentimen
def analyze_sentiment(text):
    try:
        polarity = TextBlob(str(text)).sentiment.polarity
        if polarity > 0:
            return "Positif"
        elif polarity < 0:
            return "Negatif"
        else:
            return "Netral"
    except:
        return "Netral"

# App
st.title("📊 Aplikasi Analisis Sentimen Otomatis")
st.caption("Deteksi otomatis sentimen dari data komentar/teks.")

df = load_data()

# Pilih kolom teks
text_columns = df.select_dtypes(include='object').columns.tolist()
selected_column = st.selectbox("Pilih kolom teks untuk analisis sentimen:", text_columns)

# Tambah kolom sentimen
df['Sentimen'] = df[selected_column].apply(analyze_sentiment)

# Filter
sentiment_option = st.radio("Tampilkan data dengan sentimen:", ["Semua", "Positif", "Netral", "Negatif"])

if sentiment_option != "Semua":
    filtered_df = df[df['Sentimen'] == sentiment_option]
else:
    filtered_df = df

st.write(f"Jumlah data: {len(filtered_df)}")
st.dataframe(filtered_df)
