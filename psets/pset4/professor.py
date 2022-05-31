# https://cs50.harvard.edu/python/2022/psets/4/professor/

from random import randrange


def main():
    level = get_level()

    score = 0
    for i in range(10):
        x, y = generate_integer(level), generate_integer(level)
        result = x + y

        misses, last_score = 0, score
        while misses < 3 and last_score == score:
            try:
                answer = int(input(f"{x} + {y} = "))
            except ValueError:
                pass
            else:
                if answer != result:
                    print("EEE")
                    misses += 1
                else:
                    score += 1

        if misses == 3:
            print(f"{x} + {y} = {result}")

    print("Score:", score)


def get_level():
    while True:
        try:
            l = int(input("Level: "))
        except ValueError:
            pass
        else:
            if 1 <= l <= 3:
                return l


def generate_integer(level):
    if not 1 <= level <= 3:
        raise ValueError

    lower = 0 if level == 1 else 10 ** (level - 1)
    upper = 10 ** level

    return randrange(lower, upper)


if __name__ == "__main__":
    main()
