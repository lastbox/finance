import selenium
from selenium.webdriver.common.by import By
from selenium import webdriver
driver = webdriver.Chrome("../chromedriver.exe")


url = "https://news.naver.com/"
driver.get(url)


elements = driver.find_elements(By.CLASS_NAME, "comp_journal_subscribe")
print('elements:%s'%elements)