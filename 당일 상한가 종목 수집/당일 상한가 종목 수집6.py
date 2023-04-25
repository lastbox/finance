import requests
import re
from bs4 import BeautifulSoup
import openpyxl
import datetime
import pandas as pd
import os

df = pd.DataFrame()
df1 = pd.DataFrame()
df2 = pd.DataFrame()

html = requests.get('https://finance.naver.com/sise/sise_upper.nhn')

if html != 200:
    sys.exit

print(html)

table = pd.read_html(html.text)

df1 = table[1]
df1 = df1[['종목명', '연속', '누적', '현재가', '전일비', '거래량', '저가']].dropna()

df1 = pd.merge(df1, df_code, how='left', on='종목명')

print("코스피 상한가 목록")

if df1.size == 0:
    print("없습니다.")
else:
    print(df1)

df2 = table[2]

df2 = df2[['종목명', '연속', '누적', '현재가', '전일비', '거래량', '저가']].dropna()

df2 = pd.merge(df2, df_code, how='left', on='종목명')

print("코스닥 상한가 목록")

if df2.size == 0:
    print("없습니다.")
else:
    print(df2)

df = pd.concat([df1, df2])

print(df)

result_name = 'result' + datetime.today().strftime("%y%m%d") + '.xlsx'

df.to_excel(result_name, sheet_name='Sheet1')