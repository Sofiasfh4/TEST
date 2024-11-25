import requests
from bs4 import BeautifulSoup

# URL сторінки
url = "https://www.quotegarden.com/mind.html"

# Надсилаємо GET-запит
response = requests.get(url)

# Створюємо об'єкт BeautifulSoup для аналізу HTML
soup = BeautifulSoup(response.text, 'html.parser')

# Знаходимо всі елементи, які можуть містити текст цитат
quotes = soup.find_all(string=True)

# Фільтруємо тільки ті елементи, які містять цитати
for quote in quotes:
    # Перевірка, чи містить елемент текст цитати (якщо він не порожній)
    if quote.strip():
        print(quote.strip())