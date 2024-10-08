import requests

api = requests.get('https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=dba09d7beed146b9afd2dd98d219d3c3')
content = api.json()

print(content['articles'], "\n")
print(content['articles'][0]['title'], "\n")
print(content['articles'][0]['description'])

# print(type(content))