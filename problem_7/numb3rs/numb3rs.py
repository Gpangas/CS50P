import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    try:
        numbers = re.search(r"^(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})$", ip)
        if not numbers:
            return False
        for i in range(4):
            print(numbers.group(i + 1))
            if int(numbers.group(i + 1)) not in range(256):
                return False
        return True
    except:
        return False


if __name__ == "__main__":
    main()
