# https://cs50.harvard.edu/python/2022/psets/2/plates/

from re import match


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    regex = r"(?=.{2,6}$)^([A-Z]{2})([^0][A-Z]*[0-9]*)$"
    return match(regex, s) != None


main()
