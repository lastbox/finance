import requests
import re
from bs4 import BeautifulSoup
import pandas as pd

URL = 'https://finance.naver.com/'
raw = requests.get(URL)
html = BeautifulSoup(raw.text,'lxml')
units_up =  html.select('#_topItems2>tr')  # 오늘 상한가 종목들 전부 다 가져오는거

data = []
for unit in units_up[:5]:
    title_up = unit.select_one('#_topItems2 > tr> th > a').text
    price_up = unit.select_one('#_topItems2 > tr> td')
    up = unit.select_one('#_topItems2 > tr > td:nth-child(3)').text
    percent_up = unit.select_one('#_topItems2 > tr> td:nth-child(4)')
    up = up.replace('상한가', '↑')
    news_up = 'https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query='+title_up
    raw2 = requests.get(news_up)
    html2= BeautifulSoup(raw2.text,'lxml')
    news_up_box = html2.find('div',{'class':'group_news'})
    news_up_list = news_up_box.find_all('div',{'class':'news_area'}) # 박스
    news_data = []
    for new in news_up_list[:3]:
        new_title_up = new.find('a',{'class' : 'news_tit'})
        link_up = new.find('a',{'class' : 'api_txt_lines dsc_txt_wrap'})
        news_data.append({'뉴스 제목': new_title_up.text, '뉴스 링크': link_up['href']})
    chart_up_url = 'https://finance.naver.com'+unit.select_one('#_topItems2 > tr> th > a')['href']
    chart_up_raw = requests.get(chart_up_url)
    chart_up_html = BeautifulSoup(chart_up_raw.text,'lxml')
    chart_up = chart_up_html.select_one('#img_chart_area')
    chart_up = chart_up['src']
    chart_up_day = chart_up.replace('area','candle')  #일봉
    chart_up_week = chart_up_day.replace('day','week') #주봉
    chart_up_month = chart_up_day.replace('day','month')#월봉
    data.append({'종목 이름': title_up, '한 주당 가격': price_up.text+'원', '전날 대비 가격 변동': up, '전날 대비 등락': percent_up.text, '관련 된 뉴스기사': news_data, '일봉': chart_up_day, '주봉': chart_up_week, '월봉': chart_up_month})

df = pd.DataFrame(data)
with pd.ExcelWriter('D:/lastBox/당일 상한가 종목 수집/당일 상한가 종목 수집 xlsx/상한가.xlsx') as writer:
    df.to_excel(writer, sheet_name='상한가', index=False)
