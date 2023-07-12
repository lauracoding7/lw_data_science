# pylint: disable=missing-docstring

# TODO: add some currency rates
RATES = {
    "USDEUR": 0.85,
    "EURUSD": 1.09,
    "GBPEUR": 1.13,
    "CHFEUR": 0.86,
    "EURCHF": 1.02,
    "EURGBP": 0.885
        }

def convert(amount, currency):
    """returns the converted amount in the given currency
    amount is a tuple like (100, "EUR")
    currency is a string
    """
    # YOUR CODE HERE
    for rate in RATES.items():
        if amount[1] == rate[0][0:3] and currency == rate[0][3:6]:
            result = round(rate[1] * amount[0])
            return result
    return None
