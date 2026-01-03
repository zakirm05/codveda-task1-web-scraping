import requests
from bs4 import BeautifulSoup
import pandas as pd

# 1. Website URL
url = "https://books.toscrape.com/"

# 2. Page request
response = requests.get(url)

# 3. HTML parse
soup = BeautifulSoup(response.text, "html.parser")

# 4. Data store karne ke liye lists
titles = []
prices = []
availability = []

# 5. Books data nikaalna
books = soup.find_all("article", class_="product_pod")

for book in books:
    title = book.h3.a["title"]
    price = book.find("p", class_="price_color").text
    stock = book.find("p", class_="instock availability").text.strip()

    titles.append(title)
    prices.append(price)
    availability.append(stock)

# 6. DataFrame banana
df = pd.DataFrame({
    "Book Title": titles,
    "Price": prices,
    "Availability": availability
})

# 7. CSV me save karna
df.to_csv("books_data.csv", index=False)

print("Task 1 completed successfully")
