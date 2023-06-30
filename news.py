import requests
import json

topic = input("Enter news Topic to search: \n")
date = input("Enter Date:")

API_KEY = "8f9c8e4d7e76432fb7cfa5c6230d755e"

url = ('https://newsapi.org/v2/everything?'
       f'q={topic}&'
       f'from={date}&'
       'sortBy=popularity&'
       f'apiKey={API_KEY}')

response = requests.get(url)

data = response.json()

articles = []

for article in data['articles']:

    single_article = {
        "source": article['source']['name'],
        "content": article['content']
    }

    articles.append(single_article)

data = json.dumps(articles, indent=4, ensure_ascii=False)
# print(data := json.dumps(data, indent=4))

# for article in data['articles']:
#     print(article)

print(data)