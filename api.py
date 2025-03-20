from fastapi import FastAPI
from utils import get_news_articles, analyze_sentiment, comparative_analysis, generate_hindi_tts

app = FastAPI()

@app.get("/news/{company_name}")
def fetch_news(company_name: str):
    articles = get_news_articles(company_name)
    
    for article in articles:
        article["sentiment"] = analyze_sentiment(article["title"])
    
    sentiment_summary = comparative_analysis(articles)
    return {"company": company_name, "articles": articles, "sentiment_analysis": sentiment_summary}

@app.get("/tts/{company_name}")
def text_to_speech(company_name: str):
    news_data = fetch_news(company_name)
    summary_text = f"Company: {company_name}. Sentiment Analysis: {news_data['sentiment_analysis']['Overall Sentiment']}."
    filename = generate_hindi_tts(summary_text)
    return {"audio_file": filename}
