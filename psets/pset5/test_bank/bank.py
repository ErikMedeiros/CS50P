# https://cs50.harvard.edu/python/2022/psets/5/test_bank/

def main():
    text = input("Input: ")
    text_value = value(text)

    print("$", text_value, sep="")


def value(greeting):
    lower = greeting.lower()

    if lower.startswith("hello"):
        return 0
    elif lower.startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
