import requests
from bs4 import BeautifulSoup

# URL сторінки
url = "https://www.quotegarden.com/mind.html"

# Надсилаємо GET-запит
response = requests.get(url)

# Створюємо об'єкт BeautifulSoup для аналізу HTML
soup = BeautifulSoup(response.text, 'html.parser')

quotes = soup.find_all('span', class_='text')
for quote in quotes:
    print(quote.text.strip())