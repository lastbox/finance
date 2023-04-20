import requests
import pandas as pd
import datetime
import xlsxwriter

url = 'https://stockdata.finup.co.kr/api/news/NewsListPage'
data = {
    'KeywordIdx': 155287,
    'PageNo': 1,
    'PageSize': 100
}

response = requests.post(url, data=data)
json_data = response.json()

news_list = json_data['News']

news_data = []
print('news_list : %s' % news_list)
for item in news_list:    
    news_items = []
    print('item : %s' % item)
    for key, value in item.items():
        if key == 'PublishDT':
            print('key : %s' % key)
            if value != '':
                val = value
            else:
                val = '-'                
            news_items.append(val)
        elif key == 'Title':
            print('key : %s' % key)
            if value != '':
                val = value
            else:
                val = '-'   
            news_items.append(val)
        elif key == 'Url':
            print('key : %s' % key)
            if value != '':
                val = value
            else:
                val = '-'   
            news_items.append(val)
        elif key == 'Summary':
            print('key : %s' % key)
            if value != '':
                val = value
            else:
                val = '-'   
            news_items.append(val)
        elif key == 'Media':
            print('key : %s' % key)
            if value != '':
                val = value
            else:
                val = '-'   
            news_items.append(val)
        elif key == 'DiffDate':
            print('key : %s' % key)
            if value != '':
                val = value
            else:
                val = '-'   
            news_items.append(val)
    news_data.append(news_items)


#print('news_data : %s' % news_data)
df = pd.DataFrame(news_data, columns=['날짜', '제목', '링크', '요약', '미디어', '기간'])
now = datetime.datetime.now()
filename = f"D:/lastBox/테마별 관련 뉴스 수집/테마별 관련 뉴스 수집/news_{now.strftime('%Y%m%d_%H%M%S')}.xlsx"
writer = pd.ExcelWriter(filename, engine='xlsxwriter')
df.to_excel(writer, sheet_name = 'Sheet1', index=False)

# 하이퍼링크 추가
workbook  = writer.book
worksheet = writer.sheets['Sheet1']

url_format = workbook.add_format({'font_color': 'blue', 'underline': 1})

for row_num, url in enumerate(df['링크']):
    worksheet.write_url(row_num+1, 1, url, url_format, string=df.iloc[row_num]['제목'])

writer.save()
