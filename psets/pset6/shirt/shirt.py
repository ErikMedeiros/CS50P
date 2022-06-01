# https://cs50.harvard.edu/python/2022/psets/6/shirt/

from sys import argv, exit
from PIL import Image, ImageOps


argc = len(argv)
if argc != 3:
    message = f"{'Too few' if argc < 3 else 'Too many'} command-line arguments."
    exit(message)

input_name, output_name = argv[1:3]

input_ext = input_name[input_name.rfind(".") + 1:]
output_ext = output_name[output_name.rfind(".") + 1:]

valid_extensions = ["jpg", "jpeg", "png"]

if input_ext not in valid_extensions:
    exit("Invalid input.")
elif output_ext not in valid_extensions:
    exit("Invalid output.")
elif input_ext != output_ext:
    exit("Input and output have different extensions.")

try:
    input = Image.open(input_name)
except FileNotFoundError:
    exit("Input does not exist.")

try:
    shirt = Image.open("shirt.png")
except FileNotFoundError:
    exit("shirt.png does not exist.")

with input, shirt:
    output = ImageOps.fit(input, shirt.size)
    output.paste(shirt, (0, 0), shirt)

output.save(output_name)
