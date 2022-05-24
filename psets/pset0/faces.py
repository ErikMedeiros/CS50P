# https://cs50.harvard.edu/python/2022/psets/0/faces/

def convert(text):
    return text.replace(":)", "🙂").replace(":(", "🙁")


def main():
    text = input("Type something: ")
    converted_text = convert(text)

    print(converted_text)


main()
