# https://cs50.harvard.edu/python/2022/psets/2/camel/

def main():
    camel_case = input("camelCase: ").strip()
    output = snake_case(camel_case)

    print(f"snake_case: {output}")


def snake_case(word):
    snake, i = word, 0

    while i < len(snake):
        letter = snake[i]

        if letter.isupper():
            snake = snake[:i] + f"_{letter.lower()}" + snake[i+1:]
            # Offset index for the underline added
            i += 1

        i += 1
    return snake


if __name__ == "__main__":
    main()
