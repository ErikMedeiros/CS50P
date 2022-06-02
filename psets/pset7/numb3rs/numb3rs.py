# https://cs50.harvard.edu/python/2022/psets/7/numb3rs/

import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    return re.fullmatch(
        r"(?:(?:[01]?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])(?:\.(?!$)|$)){4}", ip) != None


if __name__ == "__main__":
    main()
