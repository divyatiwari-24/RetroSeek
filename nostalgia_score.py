from bs4 import BeautifulSoup

def score_nostalgia(html):
    soup = BeautifulSoup(html, 'html.parser')
    score = 0

    if soup.find('marquee'): score += 2
    if soup.find('font'): score += 1
    if soup.find('table'): score += 1
    if soup.find('center'): score += 1
    if len(soup.find_all('script')) < 2: score += 1  # Less modern JS = more old

    return min(score, 5)


