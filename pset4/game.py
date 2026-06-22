import random


def main():

    while True:
        try:
            user_level = int(input("Level: "))
            if user_level > 0:
                break
        except ValueError:
            continue

    random_number = random.randint(1, user_level)

    while True:
        try:
            user_guess = int(input("Guess: "))
            if user_guess <= 0:
                continue
        except ValueError:
            continue

        if user_guess < random_number:
            print("Too small!")
        elif user_guess > random_number:
            print("Too large!")
        else:
            print("Just right!")
            break


if __name__ == "__main__":
    main()
