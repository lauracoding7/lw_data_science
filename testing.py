import requests
data = requests.get("https://opengraph.lewagon.com/?url=https://www.lewagon.com").json()
print(data)
