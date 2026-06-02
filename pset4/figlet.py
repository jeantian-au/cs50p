from pyfiglet import Figlet
import sys
import random

figlet = Figlet()


def main():
    if len(sys.argv) == 1:
        all_font = figlet.getFonts()
        random_font = random.choice(all_font)
        figlet.setFont(font=random_font)

    elif len(sys.argv) == 3:
        if sys.argv[1] not in ["-f", "--font"] or sys.argv[2] not in figlet.getFonts():
            sys.exit("Invalid usage")

        else:
            figlet.setFont(font=sys.argv[2])

    else:
        sys.exit("Invalid usage")

    user_word = input("Input: ")
    print("Output:")
    print(figlet.renderText(user_word))


if __name__ == "__main__":
    main()
