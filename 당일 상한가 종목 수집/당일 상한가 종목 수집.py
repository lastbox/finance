import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/sise/sise_upper.nhn"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
table = soup.find("table", {"class": "type_5"})
print("table : %s" % table)

for tr in table.find_all("tr"):
    tds = tr.find_all("td")
    if len(tds) > 0:
        if tds[0].text.strip() != "":
            print("종목명:", tds[0].text.strip())