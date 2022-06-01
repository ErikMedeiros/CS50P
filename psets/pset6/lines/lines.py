# https://cs50.harvard.edu/python/2022/psets/6/lines/

from sys import argv, exit

argc = len(argv)
if argc != 2:
    message = f"{'Too few' if argc < 2 else 'Too many'} command-line arguments."
    exit(message)

filename = argv[1]
if not filename.endswith(".py"):
    exit("Not a python file.")

try:
    file = open(filename)
except OSError:
    exit("File does not exist.")

lines = 0
for line in file:
    text = line.strip()

    if not text.startswith("# ") and text != "":
        lines += 1

file.close()

print(lines)
