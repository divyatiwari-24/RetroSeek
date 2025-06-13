from transformers import pipeline
from bs4 import BeautifulSoup
import requests

summarizer = pipeline("summarization", model="t5-small")

def summarize_webpage(url):
    html = requests.get(url, timeout=10).text
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text(separator=' ', strip=True)
    text = text[:1000]

    if len(text) < 20:
        raise ValueError("Not enough content to summarize.")

    summary = summarizer(text)[0]['summary_text']
    return summary
