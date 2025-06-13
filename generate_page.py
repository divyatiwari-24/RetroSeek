import os
import requests
import json
from summarizer import summarize_webpage
from nostalgia_score import score_nostalgia
from wiby_crawler import get_wiby_links  # <--- add this

sites = get_wiby_links(limit=5)



# Generate site data
cards_html = ""
for url in sites:
    try:
        print(f"\nFetching: {url}")
        html = requests.get(url, timeout=10).text
        print("Page length:", len(html))

        summary = summarize_webpage(url)
        score = score_nostalgia(html)
    except Exception as e:
        print(f"❌ Error for {url}: {e}")
        summary = "Could not summarize."
        score = 0


    cards_html += f"""
    <div class="site">
      <h2><a href="{url}" target="_blank">{url}</a></h2>
      <p class="score">🌟 Nostalgia Score: {score}/5</p>
      <p class="summary">🤖 AI Summary: {summary}</p>
    </div>
    """

# Write to index.html
html_template = f"""
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>RetroSeek</title>
  <link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap" rel="stylesheet">
  <style>
    body {{
      font-family: 'Press Start 2P', monospace;
      background-color: #111;
      color: #0f0;
      padding: 40px;
    }}
    h1 {{
      color: #00ffff;
      text-align: center;
      font-size: 24px;
      margin-bottom: 30px;
    }}
    .site {{
      border: 2px dashed #0f0;
      padding: 20px;
      margin-bottom: 20px;
    }}
    .site h2 a {{
      color: #ff0;
      text-decoration: none;
    }}
    .site h2 a:hover {{
      text-decoration: underline;
    }}
    .score, .summary {{
      margin-top: 10px;
    }}
    footer {{
      margin-top: 50px;
      text-align: center;
      color: #888;
      font-size: 10px;
    }}
  </style>
</head>
<body>
  <h1>🕹️ RetroSeek – Explore the Web's Past with AI</h1>
  {cards_html}
  <footer>
    🚀 Built with love by RetroSeek team | Hackathon 2025
  </footer>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print("✅ Retro dashboard generated: index.html")
