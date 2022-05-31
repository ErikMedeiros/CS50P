# https://cs50.harvard.edu/python/2022/psets/4/emojize/

from emoji import emojize

text = input("Input: ")
output = emojize(text)

print(output)
