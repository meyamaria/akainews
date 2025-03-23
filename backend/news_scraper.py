import requests
from bs4 import BeautifulSoup

def fetch_news_articles(company_name):
    search_url = f"https://www.bing.com/news/search?q={company_name}&form=NWRFSH"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    articles = []
    for item in soup.find_all('a', href=True)[40:50]:
        title = item.get_text()
        link = item['href']
        if title and (link.startswith("http") or link.startswith("http")):
            articles.append({"title": title, "link": link})

    return articles


