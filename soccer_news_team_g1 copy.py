import requests
from bs4 import BeautifulSoup

# Define the URL to scrape
url = 'https://www.uol.com.br/esporte/futebol/mercado-da-bola/'

# Send a request to the URL and get the response
response = requests.get(url)

# Use BeautifulSoup to parse the HTML content of the response
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the news articles in the HTML content
articles = soup.find_all('div', class_='thumbnails-wrapper')

# Loop through the articles and print the title and link of each one
for article in articles:
    title = article.find('h2').text.strip()
    link = article.find('a')['href']
    print(title)
    print(link)
