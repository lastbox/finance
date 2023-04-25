import FinanceDataReader as fdr

# 종목 목록 가져오기
stock_list = fdr.StockListing("KRX")

#코낵스 종목 제외
stock_list = stock_list.loc[stock_list["Market"] != "KONEX"]

print(stock_list)

# 지역이 있는 종목만 필터링하기
#stock_list = stock_list.loc[stock_list["HomePage"].notnull()]
#
#print('stock_list: %s'% stock_list)
#종목 정보 내보내기
stock_list.to_csv("D:/lastBox/퀀트투자/data/종목정보.txt", sep='\t', index=False, encoding='euc-kr')