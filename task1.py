import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
base_url = "https://books.toscrape.com/catalogue/page-{}.html"
data = []
# Fixed conversion rate for this project
GBP_TO_INR = 115
for page in range(1, 6):
    url = base_url.format(page)
    print("Scraping page:", page)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    books = soup.find_all("article", class_="product_pod")
    for book in books:
        title = book.h3.a["title"]
        # Get price
        price_text = book.find("p", class_="price_color").get_text(strip=True)
        # Extract only numbers from the price
        price_gbp = float(re.search(r"\d+(\.\d+)?", price_text).group())
        # Convert GBP to INR
        price_inr = round(price_gbp * GBP_TO_INR, 2)
        # Get rating
        rating = book.find("p", class_="star-rating")["class"][1]
        # Get availability
        availability = book.find("p", class_="instock").get_text(strip=True)
        data.append({
            "Title": title,
            "Price (INR)": price_inr,
            "Rating": rating,
            "Availability": availability
        })
# Create DataFrame
df = pd.DataFrame(data)
# Save CSV
df.to_csv("books_dataset.csv", index=False)
print("\nScraping completed!")
print("Total books collected:", len(df))
print("Dataset saved as books_dataset.csv")