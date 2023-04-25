from bs4 import BeautifulSoup as BS
import requests
import time
import datetime
import pandas as pd

base_url = 'http://www.paxnet.co.kr/stock/report/report?menuCode=2222&currentPageNo={}&reportId=0&searchKey=stock&searchValue='
data = []
check_str = '<strong class="color-cate"><span class="bracket">'

def parsing_li(li):
    stock = li.find_all("a")[0].text
    title = li.find_all("a")[1].text
    price = li.find('div', attrs = {'class':'line3'}).text
    price = price.replace('\r', '').replace('\t', '').replace('\n', '')
    if type(price.split(' ')[1].strip().replace(',', '')[:-1]) == int:
        price = price.split('  ')[1].replace(',', '')[:-1]
    else:
        price = '-'
    opinion = li.find_all('div', attrs={'class':'line3'})[1].text
    opinion = opinion.replace('\r', '').replace('\t', '').replace('\n', '')
    trading_firm = li.find_all('div', attrs={'class':'line3'})[2].text
    date = li.find_all('div', attrs={'class':'line3'})[3].text
    date = pd.to_datetime(date)

    return [stock, title, price, opinion, trading_firm, date]

for page_no in range(1, 5):
    
    print('page_no:%s'%page_no)
    url = base_url.format(page_no)
    while True:
        response = requests.get(url)
        if response.status_code == 200:
            time.sleep(1)
            break
        else:
            time.sleep(10*60)

    html = response.content
    html = BS(html, 'lxml')

    div = html.find("div", attrs = {'class':'board-type'})
    li_list = div.find_all('li') 
    for li in li_list:
        if check_str in str(li):
            record = parsing_li(li)
            data.append(record)

# 현재 시간을 가져온 뒤, 시간 형식을 변경합니다.
now = datetime.datetime.now()
date_time = now.strftime("%Y%m%d_%H%M%S")

data = pd.DataFrame(data, columns=['종목명', '리포트 제목', '적정가격', '의견', '증권사', '날짜'])
result_name = "D:/lastBox/퀀트투자/증권사 피로트 수집/증권사 리포트 수집 xlsx/정보수집_" + date_time + ".xlsx"
data.to_excel(result_name, sheet_name='증권사 리포트')