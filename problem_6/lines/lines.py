import sys

count = 0
try:
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not ".py" in sys.argv[1]:
        sys.exit("Not a Python file")
    else:
        with open(sys.argv[1], "r") as file:
            lines = file.readlines()
            for line in lines:
                if not (line.lstrip().startswith("#") or line.isspace()):
                    count += 1
            print(count)
except IndexError:
    sys.exit("Too few command-line arguments")
except FileNotFoundError:
    sys.exit("File does not exist")
