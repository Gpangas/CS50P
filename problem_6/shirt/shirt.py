import os, sys
from PIL import Image, ImageOps

#Check if it's introduced two command-line arguments
if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")

#Check two files extensions
extension_in = os.path.splitext(sys.argv[1])
extension_out = os.path.splitext(sys.argv[2])
if extension_in[1] not in (".jpg", ".jpeg", ".png"):
    sys.exit("Not a CSV file")
elif extension_out[1] not in (".jpg", ".jpeg", ".png"):
    sys.exit("Not a CSV file")
elif extension_in[1] != extension_out[1]:
    sys.exit("Input and output have different extensions")

try:
    shirt = Image.open("shirt.png")
    muppet = Image.open(sys.argv[1])
    muppet = ImageOps.fit(muppet, shirt.size)
    muppet.paste(shirt, shirt)
    muppet.save(sys.argv[2])
except FileNotFoundError:
    sys.exit("File does not exist")
