import sys
import csv

try:
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not (".csv" in sys.argv[1] and ".csv" in sys.argv[2]):
        sys.exit("Not a CSV file")
    else:
        with open(sys.argv[1], "r") as input, open(sys.argv[2], "w") as output:
            f = ["first", "last", "house"]
            reader = csv.DictReader(input)
            writer = csv.DictWriter(output, fieldnames=f)
            writer.writeheader()
            for row in reader:
                last, first = row["name"].split(",")
                writer.writerow({f[0]: first.strip(), f[1]: last.strip(), f[2]: row[f[2]].strip()})
except IndexError:
    sys.exit("Too few command-line arguments")
except FileNotFoundError:
    sys.exit("File does not exist")
