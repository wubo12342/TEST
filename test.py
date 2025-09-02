import mysql.connector
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

# 連線到 MySQL (XAMPP)
conn = mysql.connector.connect(
    host="localhost",
    user="root",      # 預設 root
    password="",      # XAMPP 預設密碼通常是空的
    database="movieDB"
)
cursor = conn.cursor()

driver = webdriver.Chrome()
driver.get("https://www.showtimes.com.tw/programs")
time.sleep(5)

for i in range(2):  # 測試爬兩部電影
    movies = driver.find_elements(By.CSS_SELECTOR, "a.sc-iGgWBj")
    movies[i].click()
    time.sleep(3)

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    # 抓標題
    try:
        title = soup.find("h1", {"class": "sc-dyGzUR"}).text.strip()
    except:
        title = "未找到標題"

    infos = soup.find_all("div", {"class": "sc-kAkpmW efezeh"})
    labels = ["length", "release_date", "theaters", "genre", "actors", "director", "plot"]
    values = [info.text.strip() for info in infos[1:]]

    while len(values) < len(labels):
        values.append("")

    # 存入 MySQL
    cursor.execute("""
    INSERT INTO movies (title, length, release_date, theaters, genre, actors, director, plot)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """, (title, *values))
    conn.commit()

    print(f"✅ 已存入 MySQL：{title}")
    driver.back()
    time.sleep(3)

driver.quit()
cursor.close()
conn.close()
