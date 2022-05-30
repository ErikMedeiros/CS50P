# https://cs50.harvard.edu/python/2022/psets/3/fuel/

def main():
    percentage = fraction_to_percentage("Fraction: ")

    if percentage <= 1:
        print("E")
    elif percentage >= 99:
        print("F")
    else:
        print(f"{percentage}%")


def fraction_to_percentage(prompt):
    while True:
        fraction = input(prompt).strip()

        try:
            x, y = [int(n) for n in fraction.split("/")]
        except ValueError:
            pass
        else:
            if x <= y:
                try:
                    return round((x / y) * 100)
                except ZeroDivisionError:
                    pass


if __name__ == "__main__":
    main()
