# https://cs50.harvard.edu/python/2022/psets/6/scourgify/

from csv import DictReader, DictWriter
from sys import argv, exit


argc = len(argv)
if argc != 3:
    message = f"{'Too few' if argc < 3 else 'Too many'} command-line arguments"
    exit(message)

input_name = argv[1]
try:
    input_file = open(input_name)
except OSError:
    exit(f"Could not read {input_name}")

output_name = argv[2] if argv[2].endswith(".csv") else f"{argv[2]}.csv"

with input_file:
    reader = DictReader(input_file)

    with open(output_name, "w") as output_file:
        writer = DictWriter(output_file, fieldnames=["first", "last", "house"])
        writer.writeheader()

        for row in reader:
            last_name, first_name = row["name"].split(", ")
            house = row["house"]

            writer.writerow(
                {"first": first_name, "last": last_name, "house": house})
