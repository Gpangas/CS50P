expression = input("Expression: ").strip()

x, y, z = expression.split(" ")

if y == "+":
    print(round(float(x) + float(z),1))
elif y == "-":
    print(round(float(x) - float(z),1))
elif y == "*":
    print(round(float(x) * float(z),1))
elif y == "/":
    print(round(float(x) / float(z),1))
else:
    print("ERROR: invalid input!")
