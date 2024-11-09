from datetime import date, timedelta
import inflect
import sys


def main():
    birth = input("Date of Birth: ")
    Birth = birth_date(birth)
    minutes = number_minutes(Birth)
    print(date_print(minutes))


# Input and validate birth date
def birth_date(birth):
    try:
        Birth = date.fromisoformat(birth)
        return Birth
    except ValueError:
        sys.exit("Invalid date")


# Calculate number of days
def number_minutes(birth):
    return int(timedelta.total_seconds(date.today() - birth) / 60)


# Transform integer into words string
def date_print(minutes):
    p = inflect.engine()
    return f"{str.capitalize(p.number_to_words(minutes, andword=""))} minutes"


if __name__ == "__main__":
    main()
