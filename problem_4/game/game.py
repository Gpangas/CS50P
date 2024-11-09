from random import randint

while True:
    try:
        level = int(input("Level: "))
        if level <= 0:
            raise ValueError
        break
    except ValueError:
        pass
    except EOFError:
        print()
        break

r = randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess < 0:
            raise ValueError
        if guess == r:
            print("Just right!")
            break
        elif guess > r:
            print("Too large!")
        else:
            print("Too small!")
    except ValueError:
        pass
    except EOFError:
        print()
        break
