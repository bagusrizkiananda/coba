import pandas as pd

# Load data
file_path = 'sentiment_analysis_results.csv'
df = pd.read_csv(file_path)

# Lexicon yang Anda berikan
sentiment_lexicon = {
    'bagus': 1, 'baik': 1, 'suka': 1, 'cinta': 1, 'menarik': 1, 'seru': 1,
    'hebat': 1, 'lucu': 1, 'tertawa': 1, 'senang': 1, 'puas': 1, 'rekomen': 1,
    'keren': 1, 'mantap': 1, 'favorit': 1, 'amazing': 1, 'brilian': 1,
    'jelek': -1, 'buruk': -1, 'tidak suka': -1, 'benci': -1, 'bosan': -1,
    'kecewa': -1, 'menyesal': -1, 'buruk sekali': -1, 'membosankan': -1,
    'tidak sangat': -1
}

# Fungsi sederhana untuk analisis sentimen
def analyze_sentiment(text):
    score = 0
    for word in text.split():
        if word in sentiment_lexicon:
            score += sentiment_lexicon[word]
    if score > 0:
        return 'positive'
    elif score < 0:
        return 'negative'
    else:
        return 'neutral'

# Terapkan ke data
df['sentiment_label'] = df['normalized_text'].apply(analyze_sentiment)

# Simpan file hasil
df.to_csv('sentiment_with_labels.csv', index=False)
print('File berhasil disimpan dengan label sentimen.')
