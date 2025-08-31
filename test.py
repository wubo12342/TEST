import requests
from bs4 import BeautifulSoup

response = requests.get('https://www.showtimes.com.tw/programs')
html = response.content.decode("utf-8")  # ✅ 這樣才會真的解碼

print(html)