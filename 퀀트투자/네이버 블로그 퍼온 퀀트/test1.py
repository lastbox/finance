from pykrx import stock
import pandas as pd
import numpy as np
import os

# 백테스트 할 날짜를 생성하기
def make_date_list(m, d):
    date_list = []
    for y in range(2003, 2021):
        day = str(y) + str(m) + str(d)
        b_day = stock.get_nearest_business_day_in_a_week(date=day) #휴일이면 근처의 영업일로 변경
        date_list.append(b_day)
    return date_list

# 실제 투자한 회사별 수익률 구하기
def row_pbr_company(date, date2):
    codes = stock.get_market_ticker_list(date)
    corp = []
    for code in codes:
        name = stock.get_market_ticker_name(code)
        corp.append([code, name])
    df1 = pd.DataFrame(data=corp, columns=['code', '종목명'])
    df1 = df1.set_index('code')

    df_f = stock.get_market_fundamental_by_ticker(date) #PER, PBR, DIV,...
    df_c = stock.get_market_cap_by_ticker(date) #종가

    df_c2 = stock.get_market_cap_by_ticker(date2) #1년 후 종가
    df_c2 = df_c2[['종가', '상장주식수']]

    df = pd.merge(df1, df_c, left_index=True, right_index=True)
    df = pd.merge(df, df_f, left_index=True, right_index=True)
    df = pd.merge(df, df_c2, left_index= True, right_index=True)

    df = df[['종목명','종가_x', '상장주식수_x', 'PBR', '종가_y', '상장주식수_y']]
    df.columns = ['종목명', '종가', '상장주식수', 'PBR', '1년후종가', '1년후상장주식수']
    df['상장주식수변동'] = df['1년후상장주식수'] - df['상장주식수']

    df = df[df['PBR'] > 0] # PBR 0이상만 구하기
    df['pbr_rank'] = df['PBR'].rank()
    df = df.sort_values(by=['pbr_rank'])

    df = df.iloc[:20] #종목개수
    df['수익'] = df['1년후종가'] - df['종가']

    df['수익'].loc[df['상장주식수변동'] < 0] = df['1년후종가'] * (1 + df['상장주식수변동'] / df['상장주식수']) - df['종가']

    df['수익률'] = (df['수익'] / df['종가'])
    df['투자년도'] = np.array([date]*len(df))

    return df

# 연도별 수익률 구하기
def row_pbr(date, date2):
    codes = stock.get_market_ticker_list(date)
    corp = []
    for code in codes:
        name = stock.get_market_ticker_name(code)
        corp.append([code, name])
    df1 = pd.DataFrame(data=corp, columns=['code', '종목명'])
    df1 = df1.set_index('code')

    df_f = stock.get_market_fundamental_by_ticker(date)  # PER, PBR, DIV,...
    df_c = stock.get_market_cap_by_ticker(date)  # 종가

    df_c2 = stock.get_market_cap_by_ticker(date2)  # 1년 후 종가
    df_c2 = df_c2[['종가', '상장주식수']]

    df = pd.merge(df1, df_c, left_index=True, right_index=True)
    df = pd.merge(df, df_f, left_index=True, right_index=True)
    df = pd.merge(df, df_c2, left_index=True, right_index=True)

    df = df[['종목명', '종가_x', '상장주식수_x', 'PBR', '종가_y', '상장주식수_y']]
    df.columns = ['종목명', '종가', '상장주식수', 'PBR', '1년후종가', '1년후상장주식수']
    df['상장주식수변동'] = df['1년후상장주식수'] - df['상장주식수']

    df = df[df['PBR'] > 0]  # PBR 0이상만 구하기
    df['pbr_rank'] = df['PBR'].rank()
    df = df.sort_values(by=['pbr_rank'])

    df = df.iloc[:20] #종목 개수
    df['수익'] = df['1년후종가'] - df['종가']

    df['수익'].loc[df['상장주식수변동'] < 0] = df['1년후종가'] * (1 + df['상장주식수변동'] / df['상장주식수']) - df['종가']

    df['투자년도'] = np.array([date] * len(df))

    df = df.iloc[:20] #종목 개수
    df['수익률'] = (df['수익'] / df['종가'])
    df['투자년도'] = np.array([date]*len(df))

    p = df['수익률'].mean()

    result = []
    result.append([date, date2, p])

    df_t = pd.DataFrame(data=result, columns=['투자일', '1년후', '수익률'])
    return df_t

# 투자 시작년도부터 마직막 년도까지 반복
def inverst_years(date_list):
    for n in range(len(date_list)):
        if n < len(date_list)-1:
            date = date_list[n]
            date2 = date_list[n+1]

            if n == 0:
                df_t = row_pbr(date, date2)
                df = row_pbr_company(date, date2)

            else:
                df_t = pd.concat([df_t, row_pbr(date, date2)])
                df = pd.concat([df, row_pbr_company(date, date2)])

    path2 = origin_path + folder_name + '\\저PBR(' + m + '월' + d + '일).xlsx'
    df.to_excel(path2)
    return df_t
    print(df_t)

test_days = ['4', '27'] # 매월 매수/매도일

for d in test_days:
    origin_path = 'D:/'
    folder_name = '\\PBR백테스트(매월' + d + '일, PBR 0이상)(20개)'
    os.mkdir(origin_path + folder_name)

    # 월별로 테스트를 반복하여 결과 얻기
    for m in range(12):
        if m == 0:
            m = '01'
            # 연도별 날짜 List 만들기
            date_list = make_date_list(m, d)

            # 백테스트 구동하기
            df_t = inverst_years(date_list)

        else:
            m += 1
            m = '0' + str(m)
            m = m[-2:]
            print(m)

            #연도별 날짜 List 만들기
            date_list = make_date_list(m, d)

            #백테스트 구동하기
            df_t = pd.concat([df_t, inverst_years(date_list)])


    path = origin_path + folder_name + '\\저PBR 0이상 백테스트(종합 매월'+ d + '일 투자) 20개.xlsx'
    df_t.to_excel(path)
