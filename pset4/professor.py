import random


def main():
    level = get_level()
    total_score = 0

    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct_answer = x + y
        trials = 0

        while trials < 3:
            try:
                user_answer = int(input(f"{x} + {y} = "))
            except ValueError:
                print("EEE")
                trials += 1
                continue

            if user_answer == correct_answer:
                total_score += 1
                break
            else:
                print("EEE")
                trials += 1

        if trials == 3:
            print(f"{x} + {y} = {correct_answer}")

    print(f"Score: {total_score}")


# one thing at a time, each function do it's simplest things...don't overthinking!


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level not in range(1, 4):
                continue
        except ValueError:
            continue
        return level


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError


if __name__ == "__main__":
    main()
