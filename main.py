import requests
data = requests.get('http://catfact.ninja/fact')
data = data.json()
print(data)