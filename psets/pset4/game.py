# https://cs50.harvard.edu/python/2022/psets/4/game/

from random import randint

while True:
    try:
        n = int(input("Level: "))
    except ValueError:
        pass
    else:
        if n > 0:
            break

number = randint(1, n)
guess = 0

while guess != number:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        pass
    else:
        if guess > 0:
            if guess < number:
                print("Too small!")
            elif guess > number:
                print("Too large!")
            else:
                print("Just right!")
