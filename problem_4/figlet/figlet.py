import sys
from pyfiglet import Figlet
from random import choice

f = Figlet()
font_type = f.getFonts()

if len(sys.argv) == 1:
    f.setFont(font = choice(font_type))

elif len(sys.argv) == 3:
    if not (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        sys.exit("Invalid first-input(-f or --font)")
    elif sys.argv[2] not in font_type:
        sys.exit("Invalid font")
    else:
        f.setFont(font = sys.argv[2])
else:
    sys.exit("Invalid input")

text = input("Input: ")

print("Output:")
print(f.renderText(text))
