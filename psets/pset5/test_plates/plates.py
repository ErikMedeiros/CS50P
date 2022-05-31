# https://cs50.harvard.edu/python/2022/psets/5/test_plates/

from re import match


def main():
    plate = input("Plate: ")
    valid = is_valid(plate)

    print("Valid" if valid else "Invalid")


def is_valid(s):
    regex = r"(?=.{2,6}$)^([A-Z]{2}[A-Z]*(?!0)[0-9]*)$"
    return match(regex, s) != None


if __name__ == "__main__":
    main()
