import requests
from bs4 import BeautifulSoup

# URL of the news website
url = "https://ge.globo.com/futebol/mercado-da-bola/"

# Send a GET request to the URL and store the response in a variable
response = requests.get(url)

# Create a BeautifulSoup object with the response content
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the article elements on the page
articles = soup.find_all('article')

# Iterate over the articles and extract the title, summary, and link
for article in articles:
    title = article.h2.text.strip()
    summary = article.p.text.strip()
    link = article.a['href']
    
    # Print the article information
    print(f"Title: {title}")
    print(f"Summary: {summary}")
    print(f"Link: {link}")
    print("")
