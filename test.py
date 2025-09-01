from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.showtimes.com.tw/programs")

time.sleep(5)  # 等待 JS 載入

urls = []

for i in range(2):  # 抓前 5 部電影
    # 每次迴圈都要重新抓元素
    movies = driver.find_elements(By.CSS_SELECTOR, "a.sc-iGgWBj")

    # 點擊第 i 部電影
    movies[i].click()
    time.sleep(3)

    # 抓當前網址
    urls.append(driver.current_url)

    # 回到上一頁
    driver.back()
    time.sleep(3)

for j in urls:
    print("抓到的電影網址：", j[-5:])
driver.quit()
