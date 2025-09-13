import cv2
import pytesseract
from PIL import Image
import numpy as np

from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

from ultralytics import YOLO
import cv2

# 載入 YOLOv8 預訓練模型
model = YOLO("yolov8n.pt")  # yolov8n 是輕量級模型，適合初學者

# 載入圖片
image_path = "images.jpg"  # 替換為你的圖片路徑
results = model(image_path)  # 進行物件檢測

# 顯示結果
results[0].show()  # 顯示帶有邊界框的圖片
results[0].save("output.jpg")  # 儲存結果到 output.jpg

