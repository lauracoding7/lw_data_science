# pylint: disable=missing-docstring,invalid-name

# TODO: paste the code from Kitt's instructions
import requests

url = "https://weather.lewagon.com/geo/1.0/direct?q=Barcelona"
response = requests.get(url).json() # requests.get(url) returns the response code

city = response[0] # response is a list and city is a dictionary

print(f"{city['name']}: ({city['lat']}, {city['lon']})") # city['lat'] is a float -> JSON supports different data types
