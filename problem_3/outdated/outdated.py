months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        inpt = input("Date: ")
        if inpt[0].isalpha():
            mm, dd, yy = inpt.split(" ")
            dd.rindex(",")
            dd = dd.removesuffix(",")
            mm = months.index(mm) + 1
        else:
            mm, dd, yy = inpt.split("/")

        if not (1 <= int(mm) <= 12):
            raise ValueError

        if  not (1 <= int(dd) <= 30):
            raise ValueError

        print(f"{int(yy):02}-{int(mm):02}-{int(dd):02} ")
        break
    except (ValueError, NameError):
        pass
    except EOFError:
        print()
        break
