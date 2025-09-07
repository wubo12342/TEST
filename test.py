import cv2
import pytesseract
from PIL import Image
import numpy as np

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome()
driver.get("https://mcp.fda.gov.tw/")
time.sleep(5)  # 等待 JS 載入
fd = driver.find_element(By.CSS_SELECTOR,'input[title="中文品名查詢"]')
fd.send_keys("阿斯匹靈")
# 載入圖片
img_element = driver.find_element(By.ID, "s_code1")
img_bytes = img_element.screenshot_as_png

# 轉成 OpenCV 可讀格式
nparr = np.frombuffer(img_bytes, np.uint8)
img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

# ==== 去紅線 ====
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# 紅色範圍
lower_red1 = np.array([0, 50, 50])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 50, 50])
upper_red2 = np.array([180, 255, 255])

mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
mask = cv2.bitwise_or(mask1, mask2)

# 把紅線變成白色
img[mask > 0] = (255, 255, 255)

# ==== 灰階 + 二值化 ====
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# ==== 存檔檢查 ====
cv2.imwrite("processed.png", thresh)

# ==== Tesseract 辨識 ====
pytesseract.pytesseract.tesseract_cmd = r"D:\文字辨識\tesseract.exe"  # 改成你 Tesseract 路徑
custom_config = r'--oem 3 --psm 7 -c tessedit_char_whitelist=0123456789'
text = pytesseract.image_to_string(thresh, config=custom_config)

print("辨識結果:", text.strip())
time.sleep(1)
fde = driver.find_element(By.CSS_SELECTOR,'input[title="驗證碼"]')
fde.send_keys(text.strip())
time.sleep(1)
fdee = driver.find_element(By.CSS_SELECTOR,'button#btnImSearch')
fdee.click()
time.sleep(5)
fdeee = driver.find_element(By.CSS_SELECTOR,'input[title="仿單"]')
fdeee.click()
time.sleep(2)
hee = driver.find_element(By.CSS_SELECTOR, 'a[rel="noopener noreferrer"]')
hee.click()
time.sleep(100)
# ==== 關閉瀏覽器 ====
driver.quit()

