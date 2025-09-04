import mysql.connector
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time


driver = webdriver.Chrome()
driver.get("https://www.showtimes.com.tw/programs")

time.sleep(5)  # 等待 JS 載入


for i in range(1):  # 測試爬兩部電影
    html = driver.page_source
    soup = BeautifulSoup(html,'html.parser')
    movies = driver.find_elements(By.CSS_SELECTOR, "a.sc-iGgWBj")

    # 點擊第 i 部電影
    movies[i].click()
    time.sleep(3)
    fdo = driver.find_elements(By.CSS_SELECTOR, "button.sc-gsFSXq")
    fdo[5].click()

    time.sleep(1)
    fd = driver.find_elements(By.CSS_SELECTOR, "div.sc-krNlru")

    for f in fd:
        print(f.text.replace("\n"," "))
        f.click()
        a = driver.find_elements(By.CSS_SELECTOR, "div.grid.grid-cols-2 div.text-lg")
        for b in a:
            print("電影時間資訊：", b.text)
        print()
        time.sleep(1)

    # 回到上一頁
    driver.back()

driver.quit()
