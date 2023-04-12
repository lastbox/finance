import requests
from bs4 import BeautifulSoup as BS

url = "http://www.paxnet.co.kr/stock/report/report?wlog_rpt=jm&menuCode=2222"
response = requests.get(url)
html = response.content
html = BS(html)

div = html.find("div", attrs = {"class" : "board-type"})
li_list = div.find_all("li")

# 수집대상 행 결정
print(li_list[0])
print(li_list[-1])