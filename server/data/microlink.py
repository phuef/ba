import requests

url = 'https://api.microlink.io'
params = {'url': 'https://wiediversistmeingarten.org/view/'}

response = requests.get(url, params)

print(response.json())