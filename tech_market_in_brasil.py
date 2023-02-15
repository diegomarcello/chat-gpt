# Using Globo.com
import requests
from bs4 import BeautifulSoup

# Set the URL of the tech news section of the G1 website
url = 'https://g1.globo.com/economia/tecnologia/'

# Send a GET request to the URL and check for errors
response = requests.get(url)
response.raise_for_status()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the news article links on the page
article_links = soup.find_all('a', class_='feed-post-link')

# Print the title and URL of each article
for link in article_links:
    article_title = link.get_text()
    article_url = link.get('href')
    print(article_title)
    print(article_url)
    print('-' * 80)



