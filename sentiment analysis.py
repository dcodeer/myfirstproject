import textblob
from textblob import TextBlob

# Input text
text = input("Enter a sentence for sentiment analysis:\n")

# Create a TextBlob object
blob = TextBlob(text)

# Analyze sentiment
polarity = blob.sentiment.polarity  # Ranges from -1 (negative) to 1 (positive)
subjectivity = blob.sentiment.subjectivity  # Ranges from 0 (objective) to 1 (subjective)

# Display results
if polarity > 0:
    print("The sentiment is Positive 😊")
elif polarity < 0:
    print("The sentiment is Negative 😞")
else:
    print("The sentiment is Neutral 😐")

print(f"Polarity: {polarity}, Subjectivity: {subjectivity}")