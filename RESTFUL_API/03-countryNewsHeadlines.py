
import requests

def get_news(country, api_key='dba09d7beed146b9afd2dd98d219d3c3'):
    url = f"https://newsapi.org/v2/top-headlines?country={country}&apiKey={api_key}"
    r = requests.get(url)
    content = r.json()
    articles = content['articles']
    results = []
    for article in articles:
        results.append(f"TITLE:\n  {article['title']} \nDESCRIPTION:\n {article['description']}")
    return '\n\n'.join(results)
        
print(get_news(country='us'))