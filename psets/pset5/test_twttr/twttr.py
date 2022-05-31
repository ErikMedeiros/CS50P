# https://cs50.harvard.edu/python/2022/psets/5/test_twttr/

def main():
    word = input("Input: ")
    short = shorten(word)

    print(short)


def shorten(word):
    vowels = ["a", "e", "i", "o", "u"]

    output = ""
    for letter in word:
        if letter.lower() not in vowels:
            output += letter

    return output



if __name__ == "__main__":
    main()
