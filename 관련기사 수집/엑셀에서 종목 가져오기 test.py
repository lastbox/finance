import pandas as pd

# 엑셀 파일 불러오기
# pd.read_excel('D:/lastBox/당일 거래대금 1000억 이상/당일 거래대금 1000억 이상 xlsx/거래대금 1000억 이상_2023-04-26 14-39-$S.xlsx')

# 이름으로 불러오기
# pd.read_excel('경로/파일명.xlsx', sheet_name = '시트명')

# 번호로 불러오기 (시작이 0)
pd.read_excel('D:/lastBox/당일 거래대금 1000억 이상/당일 거래대금 1000억 이상 xlsx/거래대금 1000억 이상_2023-04-26 14-39-$S.xlsx', sheet_name = 0, header = 1)

# 헤더 지정
#pd.read_excel('파일명.xlsx', header = 1)

for code, name in stock_list[['Code', 'Name']].values:
    print(code, name)
    while True:
        try:
            data = fdr.DataReader(code, "2011-01-01", "2021-09-30")
            if len(data) > 300:
                data.to_csv('D:\lastBox/퀀트투자/data/{}.csv'.format(name))
            time.sleep(1)
            break
        except:
            time.sleep(10*60)