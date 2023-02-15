import requests
from bs4 import BeautifulSoup

# Define the URL for the Google Flights search
url = "https://www.google.com/flights?hl=en#flt=SFO.LAX.2023-02-20;c:USD;e:1;sd:1;t:f"

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML response with Beautiful Soup
soup = BeautifulSoup(response.text, "html.parser")

# Extract the flight information
flight_data = []
for element in soup.find_all("div", {"class": "gws-flights-results__result-item"}):
    flight_info = {}
    flight_info["airline"] = element.find("div", {"class": "gws-flights-results__carriers"}).text.strip()
    flight_info["price"] = element.find("div", {"class": "gws-flights-results__price"}).text.strip()
    flight_info["departure_time"] = element.find("div", {"class": "gws-flights-results__times"}).find_all("div")[0].text.strip()
    flight_info["arrival_time"] = element.find("div", {"class": "gws-flights-results__times"}).find_all("div")[1].text.strip()
    flight_data.append(flight_info)

# Print the flight data
for flight in flight_data:
    print(flight)
