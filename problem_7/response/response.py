from validator_collection import validators, errors


def main():
    print(validation(input("What's your email adress?: ")))


def validation(s):

    try:
        validators.email(s)
        return f"Valid"
    except (errors.EmptyValueError, errors.InvalidEmailError):
        return f"Invalid"


if __name__ == "__main__":
    main()
