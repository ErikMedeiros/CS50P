# https://cs50.harvard.edu/python/2022/psets/2/twttr/

vowels = ["a", "e", "i", "o", "u"]

text = input("Input:  ")
output = ""

for letter in text:
    if letter.lower() not in vowels:
        output += letter

print("Output:", output)
