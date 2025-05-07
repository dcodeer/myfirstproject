import requests
import json
import random
from textblob import TextBlob

greetings = ["Hello", "Hi", "Hey", "Howdy", "Greetings", "Whatsup", "Salutations", "Bonjour", "Hola", "Ciao"]
farewell = ["Goodbye", "Bye", "See you later", "Take care", "Farewell", "Adios", "Ciao", "Sayonara", "Au revoir", "Later"]

print(random.choice(greetings),"!")

user = input("Say something about your mood and life\n").strip().lower()

#Initialize the list of quotes
quote_arr = []

def get_quote():
    with open("quote_bank.txt", "r") as f:
        for line in f:
           quote, author, type = line.strip().split(":")
           quote_arr.append(quote)
    return random.choice(quote_arr)
                
#Sentiment Analysis
user_sentiment = TextBlob(user)
user_polarity = user_sentiment.sentiment.polarity  # Ranges from -1 (negative) to 1 (positive)
user_subjectivity = user_sentiment.sentiment.subjectivity  # Ranges from 0 (objective) to 1 (subjective)

if user_polarity > 0:
    print("The sentiment is Positive 😊")
    quote = get_quote()
elif user_polarity < 0:
    print("The sentiment is Negative 😞")
    quote = get_quote()
else:
    print("The sentiment is Neutral 😐")
    quote = get_quote()
print("Today's Wisdom: ", quote)