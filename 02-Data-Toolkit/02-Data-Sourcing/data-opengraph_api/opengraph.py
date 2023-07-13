# pylint: disable=no-value-for-parameter
"""
Client of the Wagon OpenGraph API
"""
import pprint
import requests

def fetch_metadata(url):
    """
    Return a dictionary of OpenGraph metadata found in HTML of given url
    """
    # YOUR CODE HERE
    response = requests.get("https://opengraph.lewagon.com", params={'url': url})
    if response.status_code == 200:
        return response.json()["data"]
    return {}

# To manually test, please uncomment the following lines and run `python opengraph.py`:
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(fetch_metadata("https://www.github.com"))
