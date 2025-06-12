from transformers import pipeline
from bs4 import BeautifulSoup
import requests

summarizer = pipeline("summarization", model="t5-small")

def summarize_webpage(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text()
    text = text[:1000]  # T5 input limit

    summary = summarizer(text)[0]['summary_text']
    return summary
