while True:
    try:
        x, y = input("Fraction: ").split('/')
        x = int(x)
        y = int(y)
        if x <= y:
            break
    except (ValueError, ZeroDivisionError):
        pass

fuel = round(100 * x / y)

if(fuel <= 1):
    print("E")
elif(fuel >= 99):
    print("F")
else:
    print(str(fuel) + "%")
