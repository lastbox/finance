import requests

# API 호출을 위한 파라미터
params = {
    'ApiGB': 'KEYWORD',
    'ApiID': 'KEYWORD_DETAIL_PRICE',
    'KeywordIdx': '4435',
}

# API URL
url = 'https://apiradar.finup.co.kr/APP'

# API 호출하기
response = requests.post(url, data=params, verify=False)

# 결과 확인하기
if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f'Error: {response.status_code}')
