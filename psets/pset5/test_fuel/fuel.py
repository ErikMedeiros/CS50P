# https://cs50.harvard.edu/python/2022/psets/5/test_fuel/

def main():
    ratio = input("Fraction: ")
    percentage = convert(ratio)

    print(gauge(percentage))


def convert(fraction):
    x, y = [int(n) for n in fraction.split("/")]

    if y == 0:
        raise ZeroDivisionError
    elif x > y or x < 0:
        raise ValueError

    return round((x / y) * 100)


def gauge(percentage):
    if percentage <= 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
