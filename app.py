import pandas as pd

# Load data
df = pd.read_csv('sentiment_with_labels.csv')
df = pd.read_csv(file_path)

# Lexicon Anda
sentiment_lexicon = {
    'bagus': 1, 'baik': 1, 'suka': 1, 'cinta': 1, 'menarik': 1, 'seru': 1,
    'hebat': 1, 'lucu': 1, 'tertawa': 1, 'senang': 1, 'puas': 1, 'rekomen': 1,
    'keren': 1, 'mantap': 1, 'favorit': 1, 'amazing': 1, 'brilian': 1,
    'jelek': -1, 'buruk': -1, 'tidak suka': -1, 'benci': -1, 'bosan': -1,
    'kecewa': -1, 'menyesal': -1, 'buruk sekali': -1, 'membosankan': -1,
    'tidak sangat': -1
}

# Fungsi dengan substring matching
def analyze_sentiment(text):
    score = 0
    text = str(text).lower()  # Pastikan teks lowercase
    for phrase, value in sentiment_lexicon.items():
        if phrase in text:
            score += value
    if score > 0:
        return 'positive'
    elif score < 0:
        return 'negative'
    else:
        return 'neutral'

# Terapkan fungsi ke kolom normalized_text
df['sentiment_label'] = df['normalized_text'].apply(analyze_sentiment)

# Hitung jumlah masing-masing label
sentiment_counts = df['sentiment_label'].value_counts()
print(sentiment_counts)

# Simpan file hasil
df.to_csv('sentiment_with_labels.csv', index=False)
print('File berhasil disimpan dengan label sentimen.')
