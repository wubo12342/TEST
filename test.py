import mysql.connector
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time
import re
from datetime import datetime, timedelta


driver = webdriver.Chrome()
driver.get("https://www.ccmovie.com.tw/product.php?_path=product_showtimes")

time.sleep(5)  # 等待 JS 載入


for i in range(1):  # 測試爬兩部電影
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')
    movie = soup.select_one("div.showtime-item#m_666")

    date = movie.select_one("span.dateDisplay")
    print(date.text)

    lene = movie.select_one("div.info")
    tim = movie.select("span.float-left.info")
    for t in tim:   
        timee = datetime.strptime(t.text, "%H:%M")
        new_time = timee + timedelta(minutes=int(re.findall(r'\d+', lene.text)[0]))  
        print(f"播映時間 {t.text} ~　{new_time.strftime("%H:%M")}")

    

driver.quit()
