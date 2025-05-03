#Scrape quotes, authors, and tags from http://quotes.toscrape.com/.

import requests
from bs4 import BeautifulSoup
import csv

# CSV file setup
with open('quotes.csv', mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Quote', 'Author', 'Tags'])  # CSV header

    # Start at the first page
    base_url = 'http://quotes.toscrape.com'
    page_url = '/page/1/'

    while page_url:
        # Send a GET request
        response = requests.get(base_url + page_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find all quotes on the page
        quotes = soup.find_all('div', class_='quote')

        # Extract and write each quote's data
        for quote in quotes:
            text = quote.find('span', class_='text').text
            author = quote.find('small', class_='author').text
            tags = [tag.text for tag in quote.find_all('a', class_='tag')]
            writer.writerow([text, author, ', '.join(tags)])

        # Check for next page
        next_button = soup.find('li', class_='next')
        if next_button:
            page_url = next_button.find('a')['href']
        else:
            page_url = None

print(" All quotes scraped and saved to 'quotes.csv'.")

