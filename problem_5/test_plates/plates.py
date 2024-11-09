def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # Check if plate name is between 6 and 2 characters
    if 2 > len(s) or len(s) > 6:
        return False
    # check alphanumeric
    if not s.isalnum():
        return False
    # Check if plate name has a minimum of 2 letters
    if not (s[0].isalpha() and s[1].isalpha()):
        return False
    # Check if first number is zero and discover first number index
    n = len(s)
    for w in s:
        if w in "1234567890":
            if w == "0":
                return False
            n = s.index(w)
            break
    # Check if are letters after numbers
    if n != len(s):
        for i in range(len(s) - n):
            if not s[n + i].isnumeric():
                return False

    return True


if __name__ == "__main__":
    main()
