import sys
from os.path import splitext
from PIL import Image, ImageOps

img_extensions = ['.jpg', '.jpeg', '.png']

def check_extension(file):
    return file.lower() in img_extensions

if len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

firstfile = splitext(sys.argv[1])
secondfile = splitext(sys.argv[2])
if not check_extension(firstfile[1]) or not check_extension(secondfile[1]):
    sys.exit("Invalid input")
elif firstfile[1] != secondfile[1]:
    sys.exit("Input and output have different extensions")

if len(sys.argv) == 3:
    try:
        user_img = Image.open(sys.argv[1])
    except FileNotFoundError:
        sys.exit("Input does not exist")

    shirt = Image.open("shirt.png")
    size = shirt.size
    muppet = ImageOps.fit(user_img, size)
    muppet.paste(shirt, shirt)
    muppet.save(sys.argv[2])