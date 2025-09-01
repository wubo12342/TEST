from selenium import webdriver
import time
from bs4 import BeautifulSoup

driver = webdriver.Chrome()  # 不用指定路徑，因為就在同一個資料夾
driver.get("https://www.showtimes.com.tw/programs")

time.sleep(5) 

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
names = soup.find_all('div', {'class':'sc-gmPhUn iQHZmV'})

for name in names:
    print(name.text)
