# https://newsapi.org/v2/everything?q=apple&from=2024-10-07&to=2024-10-07&sortBy=popularity&apiKey=dba09d7beed146b9afd2dd98d219d3c3

import requests

# r = requests.get('https://newsapi.org/v2/everything?qInTitle=stock%20market&from=2024-10-07&to=2024-10-07&sortBy=popularity&language=en&apiKey=dba09d7beed146b9afd2dd98d219d3c3')
# content = r.json()

# # print(content['articles'][0])
# articles = content['articles']
# print(type(articles))
# print(type(content))

# for article in articles:
#     print('\nTITLE:\n ', article['title'], '\nDESCRIPTION:\n', article['description'])
    
# News api
def get_news(topic, from_date, to_date, language='en',
             api_key='dba09d7beed146b9afd2dd98d219d3c3'):
    url = f"https://newsapi.org/v2/everything?qInTitle={topic}&from={from_date}&to={to_date}&sortBy=popularity&language={language}&apiKey={api_key}"
    r = requests.get(url)
    content = r.json()
    articles = content['articles']
    results = []
    for article in articles:
        results.append(f"TITLE:\n  {article['title']} \nDESCRIPTION:\n {article['description']}")
    return '\n\n'.join(results)
        
print(get_news(topic='technology', from_date='2024-10-05', to_date='2024-10-08'))