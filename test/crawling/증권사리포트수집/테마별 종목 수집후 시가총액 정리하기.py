import requests
from bs4 import BeautifulSoup

stocks = ["동국알앤에스", "에코프로", "에스코넥", "아모그린텍", "세아메카닉스", "국전약품",
          "유에스티", "글로벌에스엠", "포스코퓨처엠", "에코프로비엠", "나노팀", "이녹스", 
          "윈텍", "이수화학", "이아이디", "STX", "다이나믹디자인"]

for stock in stocks:
    url = "https://finance.naver.com/item/main.nhn?code=" + stock
    print('url : %s' % url)
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html.parser')
    market_cap = soup.select_one('#tab_con1 > div.first > table > tbody > tr.strong > td')
    print(stock, "시가총액:", market_cap.text)
