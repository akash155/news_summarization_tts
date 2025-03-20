import requests
from bs4 import BeautifulSoup

def get_news_articles(company_name, num_articles=10):
    search_url = f"https://news.google.com/search?q={company_name}"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(search_url, headers=headers)
    
    if response.status_code != 200:
        return {"error": "Failed to retrieve news articles."}
    
    soup = BeautifulSoup(response.text, "html.parser")
    articles = soup.find_all("article")[:num_articles]
    
    news_list = []
    for article in articles:
        title = article.find("h3").text if article.find("h3") else "No Title"
        link = "https://news.google.com" + article.find("a")["href"] if article.find("a") else "No Link"
        news_list.append({"title": title, "link": link})
    
    return news_list

from nltk.sentiment import SentimentIntensityAnalyzer
import nltk

nltk.download("vader_lexicon")

def analyze_sentiment(text):
    sia = SentimentIntensityAnalyzer()
    score = sia.polarity_scores(text)["compound"]
    
    if score >= 0.05:
        return "Positive"
    elif score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

import pandas as pd

def comparative_analysis(news_articles):
    sentiment_counts = {"Positive": 0, "Negative": 0, "Neutral": 0}
    
    for article in news_articles:
        sentiment_counts[article["sentiment"]] += 1
    
    analysis = {
        "Sentiment Distribution": sentiment_counts,
        "Overall Sentiment": max(sentiment_counts, key=sentiment_counts.get)
    }
    return analysis
from gtts import gTTS

def generate_hindi_tts(text, filename="output.mp3"):
    tts = gTTS(text=text, lang="hi")
    tts.save(filename)
    return filename

