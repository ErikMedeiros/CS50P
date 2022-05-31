# https://cs50.harvard.edu/python/2022/psets/4/adieu/

from inflect import engine

p = engine()
names = []

while True:
    try:
        name = input("Name: ")
        names.append(name)
    except EOFError:
        print()
        break

print("Adieu, adieu, to", p.join(names))
