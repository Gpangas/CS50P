from fuel import convert, gauge
import pytest


def main():
    test_input()
    test_errors()
    test_output()


def test_input():
    assert convert("3/4") == 75
    assert convert("1/1") == 100
    assert convert("0/1") == 0


def test_errors():
    # Check correct format
    with pytest.raises(ValueError):
        convert("cat")
    # Check if x and/or y are integer
    with pytest.raises(ValueError):
        convert("3/cat")
    with pytest.raises(ValueError):
        convert("dog/4")
    # Check if x <= y
    with pytest.raises(ValueError):
        convert("4/3")
    # Check if y != 0
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_output():
    # Check empty tank
    assert gauge(1) == "E"
    # Check full tank
    assert gauge(99) == "F"
    # Check percentage display
    assert gauge(75) == "75%"


if __name__ == "__main__":
    main()
