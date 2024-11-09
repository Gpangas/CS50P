from numb3rs import validate


def main():
    test_validate()


def test_validate():
    assert validate("Hello") == False
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("555.255.255.255") == False
    assert validate("255.555.255.255") == False
    assert validate("255.255.555.255") == False
    assert validate("255.255.255.555") == False
    assert validate("1000.2.3.4") == False
    assert validate("1.2.3.1000") == False


if __name__ == "__main__":
    main()
