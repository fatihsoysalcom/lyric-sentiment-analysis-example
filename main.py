import re

def analyze_sentiment(lyrics):
    """
    Performs a basic sentiment analysis on song lyrics using a predefined lexicon.
    This simulates the "AI-powered" analysis concept from the LyricLens article.
    """
    # Define simple positive and negative word lists (lexicon) in Turkish.
    # These words are chosen to reflect common emotional tones.
    positive_words = {
        "güneş", "umut", "aşk", "neşe", "mutlu", "sevinç", "güzel", "parlak",
        "huzur", "ışık", "canlı", "coşku", "gülümse", "hayat", "sevgi", "iyi"
    }
    negative_words = {
        "hüzün", "yalnızlık", "ağlar", "keder", "üzgün", "acı", "karanlık",
        "kayıp", "yorgun", "pişman", "korku", "endişe", "bitkin", "çaresiz", "kötü"
    }

    # Convert lyrics to lowercase for case-insensitive matching.
    lyrics_lower = lyrics.lower()

    # Tokenize the lyrics (split into words), removing punctuation.
    # Using re.findall to get all word characters.
    words = re.findall(r'\b\w+\b', lyrics_lower)

    positive_score = 0
    negative_score = 0

    # Iterate through words and check against lexicons.
    for word in words:
        if word in positive_words:
            positive_score += 1
        elif word in negative_words:
            negative_score += 1

    total_words = len(words)
    if total_words == 0:
        return "Neutral", 0, 0, 0

    # Calculate a simple sentiment score.
    # The sentiment score is the difference between positive and negative word counts,
    # normalized by the total number of words to get a value between -1 and 1.
    sentiment_score = (positive_score - negative_score) / total_words

    # Determine overall sentiment based on thresholds.
    if sentiment_score > 0.1: # Threshold for positive sentiment
        overall_sentiment = "Positive"
    elif sentiment_score < -0.1: # Threshold for negative sentiment
        overall_sentiment = "Negative"
    else:
        overall_sentiment = "Neutral"

    return overall_sentiment, sentiment_score, positive_score, negative_score

# --- Example Usage ---
# Sample Turkish lyric, chosen to have a mix of positive and negative elements
# to demonstrate the analysis.
sample_lyric_1 = """
Güneş doğdu içimde, umut yeşerdi yeniden. Aşk dolu kalbim, neşe saçıyor her yere.
Ama bazen hüzün çöker, yalnızlık ağlatır beni. Karanlık gecelerde kaybolurum.
Yine de bir umut var, sevgi beni kurtaracak.
"""

print("--- LyricLens Basic Sentiment Analysis ---")
print(f"\nAnalyzing Lyric 1:\n'{sample_lyric_1.strip()}'\n")

# Perform the sentiment analysis for the first lyric.
overall_sentiment_1, score_1, pos_count_1, neg_count_1 = analyze_sentiment(sample_lyric_1)

# Display results, illustrating the main concept of emotional analysis.
print(f"Overall Sentiment: {overall_sentiment_1}")
print(f"Sentiment Score (normalized): {score_1:.2f}")
print(f"Positive Word Count: {pos_count_1}")
print(f"Negative Word Count: {neg_count_1}")

# A second example for contrast, with a more clearly positive tone.
sample_lyric_2 = """
Her şey güzel, dünya harika. Mutluluk içimde, coşkuyla doluyum. Hayat çok iyi.
"""
print(f"\nAnalyzing Lyric 2:\n'{sample_lyric_2.strip()}'\n")
overall_sentiment_2, score_2, pos_count_2, neg_count_2 = analyze_sentiment(sample_lyric_2)
print(f"Overall Sentiment: {overall_sentiment_2}")
print(f"Sentiment Score (normalized): {score_2:.2f}")
print(f"Positive Word Count: {pos_count_2}")
print(f"Negative Word Count: {neg_count_2}")
