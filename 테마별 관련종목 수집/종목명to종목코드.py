import pandas as pd

def convert_to_stock_code(stock_name):
    # KRX에서 제공하는 상장 종목 리스트를 불러옵니다.
    url = 'http://kind.krx.co.kr/corpgeneral/corpList.do?method=download'
    df = pd.read_html(url, header=0)[0]

    # 종목 이름과 일치하는 종목을 찾습니다.
    df_filtered = df[df['회사명'] == stock_name]

    # 찾은 종목의 종목 코드를 반환합니다.
    if len(df_filtered) > 0:
        stock_code = str(df_filtered.iloc[0]['종목코드']).zfill(6)
        return stock_code
    else:
        return None

stock_name = input("종목명을 입력하세요: ")
stock_code = convert_to_stock_code(stock_name)

if stock_code is not None:
    print(f"{stock_name}의 종목 코드는 {stock_code}입니다.")
else:
    print(f"{stock_name}은(는) 상장되지 않은 종목입니다.")
