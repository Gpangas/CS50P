groceries = {}

while True:
    try:
        item = input().strip().lower()

        if item in groceries:
            n = groceries[item] + 1
            groceries.update({item:n})
        else:
            groceries[item] = 1
    except KeyError:
        pass
    except EOFError:
        print()
        break

sorted_groceries = list(groceries.keys())
sorted_groceries.sort()

for item in sorted_groceries:
    print(groceries[item], item.upper())
