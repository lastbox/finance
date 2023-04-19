import requests
import pandas as pd

url = 'https://stockdata.finup.co.kr/api/news/NewsListPage'
data = {
    'KeywordIdx': 4435,
    'PageNo': 7,
    'PageSize': 10
}

response = requests.post(url, data=data)
json_data = response.json()

news_list = json_data['News']
news_data = []
for item in news_list:
    for key, value in item.items():
        news_duple = {
            if key == 'PublishDT':
                
            elif key == 'Title':
            elif key == 'url':
            elif key == 'Summary':
            elif key == 'DiffDate':
        }
    news_data.append(news_duple)

df = pd.DataFrame(news_data)
df.to_excel('news.xlsx', index=False)
