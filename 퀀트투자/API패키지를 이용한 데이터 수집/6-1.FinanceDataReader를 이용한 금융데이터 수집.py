import FinanceDataReader as fdr

KP_stock_list = fdr.StockListing("KRX")
print('KP_stock_list:%s'%KP_stock_list)

#sp_data = fdr.DataReader("005380", "2020-01-01", "2020-10-30")
#print('sp_data:%s'%sp_data)