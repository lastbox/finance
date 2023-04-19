import requests
from bs4 import BeautifulSoup
import openpyxl
from datetime import datetime

def get_related_stocks_info(theme_name):
    url = f'https://finance.finup.co.kr/Search/GetSearchStock?searchWord={theme_name}&page=1&countPerPage=10'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', {'class': 'tbl_type_01'})

    print("url : %s" % url)

    # Create an Excel workbook and worksheet
    wb = openpyxl.Workbook()
    ws = wb.active

    # Write the header row to the worksheet
    ws.append(['종목명', '현재가', '등락률', '거래대금', '테마포함사유'])

    # Loop through each row in the table and extract the desired information
    for tr in table.find_all('tr')[1:]:
        row = []
        # Extract stock name
        name = tr.find_all('td')[0].text.strip()
        row.append(name)
        # Extract current price
        price = tr.find_all('td')[1].text.strip()
        row.append(price)
        # Extract price change percentage
        change_pct = tr.find_all('td')[2].text.strip()
        row.append(change_pct)
        # Extract trading volume
        volume = tr.find_all('td')[3].text.strip()
        row.append(volume)
        # Extract reason for inclusion in theme
        reason = tr.find_all('td')[4].text.strip()
        row.append(reason)

        # Write the row to the worksheet
        ws.append(row)

    # Generate a filename based on the current date and time
    now = datetime.now()
    filename = now.strftime(f"D:/lastBox/테마별 관련종목 수집/테마별 관련종목 수집 xlsx/{theme_name}_%Y-%m-%d_%H-%M-%S.xlsx")

    # Save the workbook to an Excel file
    wb.save(filename)

theme_name = input('검색할 주제를 입력하세요: ')
get_related_stocks_info(theme_name)
