import requests

### BASIC REQUEST ###
# url = 'https://api.github.com/users/ssaunier'
# response = requests.get(url).json()

# print(response['name'])

BASE_URL = "https://openlibrary.org/api/books"

isbns = ["9780980200447", "0385472579"]


def get_title(isbn):
    isbn_key = f"ISBN:{isbn}"

    response = requests.get(BASE_URL, params={"bibkeys": isbn_key ,
                          "format": "json",
                          "jscmd": "data"}).json()

    return response[isbn_key]["title"]

for isbn in isbns:
    print(get_title(isbn))
