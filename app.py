import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load data
uploaded_file = 'sentiment_analysis_results.csv'
df = pd.read_csv(uploaded_file)

# Pastikan kolom yang digunakan benar
if 'sentiment_label' not in df.columns:
    st.error("Kolom 'sentiment_label' tidak ditemukan dalam file CSV.")
else:
    st.title("Sentiment Distribution")

    # Hitung distribusi sentimen
    sentiment_counts = df['sentiment_label'].value_counts()

    # Tampilkan tabel distribusi
    st.subheader("Sentiment Counts")
    st.write(sentiment_counts)

    # Plot distribusi sentimen
    fig, ax = plt.subplots()
    ax.bar(sentiment_counts.index, sentiment_counts.values, color=['green', 'red'])
    ax.set_xlabel('Sentiment')
    ax.set_ylabel('Count')
    ax.set_title('Sentiment Distribution')
    st.pyplot(fig)

    # Tambahkan opsi untuk filter
    st.subheader("Filter Data berdasarkan Sentiment")
    selected_sentiment = st.selectbox("Pilih Sentiment:", ['All'] + list(sentiment_counts.index))

    if selected_sentiment != 'All':
        filtered_df = df[df['sentiment_label'] == selected_sentiment]
        st.write(filtered_df)
    else:
        st.write(df)
