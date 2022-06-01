# https://cs50.harvard.edu/python/2022/psets/6/pizza/

from sys import argv, exit
from csv import DictReader
from tabulate import tabulate


if len(argv) != 2:
    exit("Wrong argument count.")

filename = argv[1]
if not filename.endswith(".csv"):
    exit("Not a CSV file.")

try:
    file = open(filename)
except OSError:
    exit("File does not exist.")

menu_data = []

reader = DictReader(file)
for row in reader:
    menu_data.append(row)

file.close()

menu = tabulate(menu_data, headers="keys", tablefmt="grid")
print(menu)
