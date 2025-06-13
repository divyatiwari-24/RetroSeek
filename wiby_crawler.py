import requests
from bs4 import BeautifulSoup
import re

def get_wiby_links(limit=5):
    print("🔍 Crawling Wiby Surprise Page for links...")
    url = "https://wiby.me/surprise/"
    headers = {"User-Agent": "Mozilla/5.0"}

    links = []

    try:
        for i in range(limit):
            res = requests.get(url, headers=headers, timeout=5)
            soup = BeautifulSoup(res.text, "html.parser")

            # Find the <meta http-equiv="refresh"> tag
            meta = soup.find("meta", attrs={"http-equiv": "refresh"})

            if meta and "content" in meta.attrs:
                # Extract the actual URL from content string
                match = re.search(r"URL='?([^']+)'?", meta["content"])
                if match:
                    redirect_url = match.group(1)
                    print(f"✅ Found: {redirect_url}")
                    links.append(redirect_url)
                else:
                    print("⚠️ No URL found in meta tag.")
            else:
                print("⚠️ No meta refresh tag found.")

    except Exception as e:
        print("❌ Error while crawling Wiby:", e)

    return links
