# https://cs50.harvard.edu/python/2022/psets/1/bank/

answer = input("Greeting: ").strip().lower()

if answer.startswith("hello"):
    print("$0")
elif answer.startswith("h"):
    print("$20")
else:
    print("$100")
