camel = input("Insert camelCase:").strip()

snake = ""
for letter in camel:
    if letter.isupper():
        snake += "_" + letter.lower()
    else:
        snake += letter

print("snake_case:", snake)
