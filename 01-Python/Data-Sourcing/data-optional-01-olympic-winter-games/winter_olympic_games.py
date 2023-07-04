# pylint: disable=missing-docstring

import csv
from collections import Counter

COUNTRIES_FILEPATH = "data/dictionary.csv"
MEDALS_FILEPATH = "data/winter.csv"


def most_decorated_athlete_ever():
    """Returns who won the most winter olympic games medals (gold/silver/bronze) ever"""
    # YOUR CODE HERE
    with open('data/winter.csv', mode='r', encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        athletes = [row["Athlete"] for row in csv_reader]
    return Counter(athletes).most_common()[0][0]

def country_with_most_gold_medals(min_year, max_year):
    """Returns which country won the most gold medals between `min_year` and `max_year`"""
    # YOUR CODE HERE
    with open('data/winter.csv', mode='r', encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        countries = [row["Country"] for row in csv_reader if int(row["Year"]) >= min_year \
                                    and int(row["Year"]) <= max_year \
                                    and row["Medal"] == "Gold"]

    country_code = Counter(countries).most_common()[0][0]
    with open('data/dictionary.csv', mode='r', encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        country = [row["Country"] for row in csv_reader if row["Code"] == country_code][0]
    print(country)
    return country

def top_three_women_in_five_thousand_meters():
    """Returns the three women with the most 5000 meters medals(gold/silver/bronze)"""
    # YOUR CODE HERE
    with open('data/winter.csv', mode='r', encoding="utf-8") as csv_file:
        csv_reader = csv.DictReader(csv_file)
        women = [row["Athlete"] for row in csv_reader if row["Gender"] == "Women" \
                                and row["Event"] == "5000M"]
    return [women[0] for women in Counter(women).most_common()[:3]]
