import time
import FinanceDataReader as fdr

# 종목 목록 가져오기
stock_list = fdr.StockListing("KOSPI")
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