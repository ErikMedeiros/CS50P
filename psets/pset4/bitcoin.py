# https://cs50.harvard.edu/python/2022/psets/4/bitcoin/

from requests import get
from sys import argv, exit


if len(argv) != 2:
    exit("Wrong argument count.")
try:
    dollars = float(argv[1])
except ValueError:
    exit("Argument is not a number.")

response = get("https://api.coindesk.com/v1/bpi/currentprice.json")
json_object = response.json()

bitcoins = json_object["bpi"]["USD"]["rate_float"]
value = bitcoins * dollars

print(f"${value:,.4f}")
