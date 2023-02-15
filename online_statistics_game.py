import requests

# Set the URL of the API endpoint
url = "http://api.football-data.org/v2/matches"

# Set the match ID of the game you want to get statistics for
match_id = 123456

# Set the headers with your API key
headers = {"X-Auth-Token": "YOUR_API_KEY"}

# Set the query parameters with the match ID
params = {"match_id": match_id}

# Send the HTTP GET request to the API endpoint
response = requests.get(url, headers=headers, params=params)

# Parse the response JSON data
data = response.json()

# Extract the statistics for the match
statistics = data["matches"][0]["score"]["fullTime"]

# Print the statistics
print("Goals: {}-{}".format(statistics["homeTeam"], statistics["awayTeam"]))
print("Possession: {}-{}".format(data["matches"][0]["homeTeam"]["possession"], data["matches"][0]["awayTeam"]["possession"]))
print("Shots: {}-{}".format(data["matches"][0]["homeTeam"]["shots"]["total"], data["matches"][0]["awayTeam"]["shots"]["total"]))
