def main():
    word = input("Input: ")

    print(f"Output: {shorten(word)}")


def shorten(word):
    wrd = ""
    for letter in word:
        if letter.lower() not in ["a", "e", "i", "o", "u"]:
            wrd = wrd + letter

    return wrd


if __name__ == "__main__":
    main()
