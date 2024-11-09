from seasons import birth_date, number_minutes, date_print
import pytest
from datetime import date

def main():
    test_birth_date()
    test_number_minutes()
    date_print()

#Test birth date input
def test_birth_date():
    with pytest.raises(SystemExit):
        birth_date("2000, 8 of setember")
    with pytest.raises(SystemExit):
        birth_date("2000-11-1")
    with pytest.raises(SystemExit):
        birth_date("2000-1-01")
    with pytest.raises(SystemExit):
        birth_date("200-11-01")
    with pytest.raises(SystemExit):
        birth_date("2000-15-01")
    with pytest.raises(SystemExit):
        birth_date("2000-11-35")
    assert birth_date("2023-10-23") == date(2023, 10, 23)

#Test convertion from date to minutes
def test_number_minutes():
    Difference = date(2022, 10, 23)
    assert number_minutes(Difference) == 1054080

#Test date print
def test_date_print():
    assert date_print(1054080) == "One million, fifty-four thousand eighty minutes"

if __name__ == "__main__":
    main()
