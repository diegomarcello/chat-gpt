import requests
from bs4 import BeautifulSoup

# URL of the CNN Travel section
url = "https://www.cnn.com/travel"

# Send a request to the website and get the HTML content
response = requests.get(url)
html = response.content

# Create a BeautifulSoup object to parse the HTML content
soup = BeautifulSoup(html, "html.parser")

# Find all articles in the "Travel" section
articles = soup.find_all("article", class_="cd--article")

# Iterate through each article and print the headline and summary
for article in articles:
    headline = article.find("h3", class_="cd--headline").get_text()
    summary = article.find("div", class_="cd--excerpt").get_text()
    print(headline)
    print(summary)
    print()
