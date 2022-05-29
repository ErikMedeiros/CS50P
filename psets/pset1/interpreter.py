# https://cs50.harvard.edu/python/2022/psets/1/interpreter/

x, operator, y = input("Expression: ").strip().split(" ")
x = int(x)
y = int(y)

if operator == "+":
    result = x + y
elif operator == "-":
    result = x - y
elif operator == "/":
    result = x / y
elif operator == "*":
    result = x * y

print(f"{result:.1f}")