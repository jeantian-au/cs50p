WORDS = {"pair":4, "hair":4, "chair":5 ,"graphic":7}

def main():
    print("Hello spelling bee player.")
    print("Your letters are: P C H I R A E G")

    while len(WORDS) > 0:
        print(f"{len(WORDS)} words left")
        guess = input("Guess a word! ")

        if guess == "graphic"：
            WORDS.clear()
            # clear all the items from the dictionary
            print("You won!")

        if guess in WORDS.keys():
            points = WORDS.pop(guess)
            # points get the return value of the key, and then remove that key+value from dic
            print(f"Good job, you scored {points} points")

    print("that's all")

main()

==========
WORDS = {"pair":4, "hair":4, "chair":5 ,"graphic":7}

def main():
    print("Welcoming to spelling bee!")
    for word, points in WORDS.items():
        print(f"this {word} is worth {points} points!")

main()
