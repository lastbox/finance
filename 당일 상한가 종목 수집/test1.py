import requests
import re
from bs4 import BeautifulSoup
import openpyxl
import datetime
import re

now = datetime.datetime.now()
date = now.strftime('%Y-%m-%d %H-%M-%S')

def get_bs_obj():

 

    url = "https://finance.naver.com/sise/sise_upper.nhn"

    result = requests.get(url)

    bs_obj = BeautifulSoup(result.content, "html.parser")

    units_up = bs_obj.find_all('table', {'class':'type_5'})
    
    for unit in units_up:
        tr_up = unit.find_all('tr')
        #header = units_up.select('th')
        print('tr_up: %s' %tr_up)


 

units_up = get_bs_obj()
