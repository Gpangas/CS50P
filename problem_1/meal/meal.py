def main():
    time = input("What time is it? ")
    converted = convert(time)

    if 7 <= converted <= 8:
        print("breakfast time")
    elif 12 <= converted <= 13:
        print("lunch time")
    elif 18 <= converted <= 19:
        print("dinner time")


def convert(time):
    h, mm = time.split(":")

    return  float(h) + float(mm)/60


if __name__ == "__main__":
    main()
