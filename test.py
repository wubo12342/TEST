import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/139.0.0.0 Safari/537.36"
}

url = "https://books.toscrape.com/"
res = requests.get(url, headers=headers).text
soup = BeautifulSoup(res, 'html.parser')

books = soup.select('ol.row li')

for book in books:
    name = book.select_one('h3 a')['title'] 
    rating = book.select_one('p')['class']
    price = book.select_one('p.price_color').text
    print(f"Name : {name}\nRating : {rating[1]}\nPrice : {price}")
