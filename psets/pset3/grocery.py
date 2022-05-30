# https://cs50.harvard.edu/python/2022/psets/3/grocery/

grocery_list = {}

while True:
    try:
        item = input().strip().upper()
    except EOFError:
        print()
        break
    else:
        try:
            grocery_list[item] += 1
        except KeyError:
            grocery_list[item] = 1

for key, value in sorted(grocery_list.items()):
    print(value, key)
