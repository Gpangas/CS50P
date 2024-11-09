from plates import is_valid


def main():
    test_is_valid()
    test_length()
    test_alphanumeric()
    test_letter_minimum()
    test_first_number()
    test_letters_after_numbers()


def test_is_valid():
    assert is_valid("CS50") == True


def test_length():
    # Check if plate name is between 6 and 2 characters
    assert is_valid("CSCS5050") == False
    assert is_valid("C") == False


def test_alphanumeric():
    # check alphanumeric
    assert is_valid("CS50!") == False


def test_letter_minimum():
    # Check if plate name has a minimum of 2 letters
    assert is_valid("C50") == False


def test_first_number():
    # Check if first number is zero and discover first number index
    assert is_valid("CS050") == False


def test_letters_after_numbers():
    # Check if are letters after numbers
    assert is_valid("CS50CS") == False


if __name__ == "__main__":
    main()
