import requests

api_url = 'https://www.webmotors.com.br/api/search/car?url=https://www.webmotors.com.br/carros/estoque/?tipoveiculo=carros&estadocidade=estoque&marca1=Chevrolet'

response = requests.get(api_url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print(f"Error: {response.status_code}")
