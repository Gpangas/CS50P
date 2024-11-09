from bank import value


def main():
    test_value()


def test_value():
    assert value("Hello") == 0
    assert value("hello") == 0
    assert value("Hey") == 20
    assert value("hey") == 20
    assert value("piss off") == 100


if __name__ == "__main__":
    main()
