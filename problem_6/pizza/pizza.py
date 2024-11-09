from tabulate import tabulate
import sys
import csv

try:
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif not ".csv" in sys.argv[1]:
        sys.exit("Not a CSV file")
    else:
        with open(sys.argv[1], "r") as file:
            reader = csv.DictReader(file)
            print(tabulate(reader, headers="keys", tablefmt="grid"))
except IndexError:
    sys.exit("Too few command-line arguments")
except FileNotFoundError:
    sys.exit("File does not exist")
