import random


def main():
    level = get_level()
    score = 0
    for i in range(10):
        n_1 = generate_integer(level)
        n_2 = generate_integer(level)

        for j in range(3):
            try:
                result = int(input(str(n_1) + " + " + str(n_2) + " = "))
                if result == n_1 + n_2:
                    score += 1
                    break
            except ValueError:
                pass
            except ValueError:
                print()
                break
            print("EEE")
            if j == 2:
                print(str(n_1) + " + " + str(n_2) + " = " + str(n_1 + n_2))

    print("Score:", score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level != 1 and level != 2 and level != 3:
                raise ValueError
            return level
        except ValueError:
            pass


def generate_integer(level):
    if level == 1:
        return random.randint(0, (10**level - 1))
    else:
        return random.randint(10 ** (level - 1), (10**level - 1))


if __name__ == "__main__":
    main()
