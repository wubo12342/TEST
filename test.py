import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
b = []
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/139.0.0.0 Safari/537.36"
}
i = 0
url = "https://books.toscrape.com/"
while url:
    res = requests.get(url, headers=headers).text
    soup = BeautifulSoup(res, 'html.parser')

    books = soup.select('ol.row li')

    for book in books:
        name = book.select_one('h3 a')['title'] 
        rating = book.select_one('p')['class']
        price = book.select_one('p.price_color').text
        print(f"Name : {name}\nRating : {rating[1]}\nPrice : {price}\n")
        b.append({
        "name": name,
        "rating": rating[1],
        "price": price
        })

    next_page = soup.select_one('li.next a')
    if next_page:
        url = urljoin(url, next_page['href'])
    else:
        url = None
    i += 1
    print(i)
