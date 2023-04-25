import requests
from bs4 import BeautifulSoup as BS
import pandas as pd


url = 'http://www.paxnet.co.kr/stock/report/report?menuCode=2222'
response = requests.get(url)
html = response.content
html = BS(html, 'lxml')

'''
ul = html.find("ul", attrs={'class':'board-list'})
li_list = ul.find_all('li')
'''

div = html.find('div', {'class':'board-type'})
li_list = div.find_all('li')

check_str = '<strong class="color-cate"><span class="bracket">'
data = []

def parsing_li(li):
    stock = li.find_all("a")[0].text
    title = li.find_all("a")[1].text
    price = li.find('div', attrs = {'class':'line3'}).text
    price = price.replace('\r', '').replace('\t', '').replace('\n', '')
    price = price.split('  ')[1].replace(',', '')[:-1]
    opinion = li.find_all('div', attrs={'class':'line3'})[1].text
    opinion = opinion.replace('\r', '').replace('\t', '').replace('\n', '')
    trading_firm = li.find_all('div', attrs={'class':'line3'})[2].text
    date = li.find_all('div', attrs={'class':'line3'})[3].text
    date = pd.to_datetime(date)

for li in li_list:
    if check_str in str(li):
        record = parsing_li(li)
        data.append(record)

print(parsing_li(li_list[1]))

data = pd.DataFrame(data, columns=['종목명', '리포트 제목', '적정가격', '의견', '증권사', '날짜'])