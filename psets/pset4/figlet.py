# https://cs50.harvard.edu/python/2022/psets/4/figlet/

from pyfiglet import Figlet
from random import choice
from sys import argv, exit

argc = len(argv)

figlet = Figlet()
fonts = figlet.getFonts()

if argc not in [1, 3]:
    exit("Invalid argument count.")
elif argc == 3:
    if argv[1] not in ["-f", "--font"]:
        exit("Invalid option.")
    elif argv[2] not in fonts:
        exit("Invalid font name.")

s = input("Input: ")

if argc == 1:
    f = choice(fonts)
else:
    f = argv[2]

figlet.setFont(font=f)
print(figlet.renderText(s))
