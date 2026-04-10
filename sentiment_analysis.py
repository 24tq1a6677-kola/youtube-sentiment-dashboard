import pandas as pd
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Load comments
df = pd.read_csv("comments.csv")

# Initialize analyzer
analyzer = SentimentIntensityAnalyzer()

# Function to classify sentiment
def get_sentiment(text):
    score = analyzer.polarity_scores(str(text))
    if score['compound'] >= 0.05:
        return "Positive"
    elif score['compound'] <= -0.05:
        return "Negative"
    else:
        return "Neutral"

# Apply sentiment
df['Sentiment'] = df['Comment'].apply(get_sentiment)

# Save output
df.to_csv("sentiment_results.csv", index=False)

print("Sentiment analysis completed!")