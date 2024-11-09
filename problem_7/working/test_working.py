from working import convert
import pytest


def main():
    test_time()
    test_raise()


def test_time():
    assert convert("9:35 AM to 5:35 PM") == "09:35 to 17:35"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("9:35 AM to 5 PM") == "09:35 to 17:00"
    assert convert("9 AM to 5:35 PM") == "09:00 to 17:35"
    assert convert("8 PM to 8 AM") == "20:00 to 08:00"
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"

def test_raise():
    with pytest.raises(ValueError):
        convert("8 PM 8 AM")
    with pytest.raises(ValueError):
        convert(" PM to 8 AM")
    with pytest.raises(ValueError):
        convert("8  to 8 AM")
    with pytest.raises(ValueError):
        convert("8 PM 8 AM")
    with pytest.raises(ValueError):
        convert("8 PM to  AM")
    with pytest.raises(ValueError):
        convert("8 PM to 8")
    with pytest.raises(ValueError):
        convert("8:60 PM to 8 AM")
    with pytest.raises(ValueError):
        convert("8 PM to 8:60 AM")
    with pytest.raises(ValueError):
        convert("15 PM to 8 AM")
    with pytest.raises(ValueError):
        convert("8 PM to 15 AM")


if __name__ == "__main__":
    main()
