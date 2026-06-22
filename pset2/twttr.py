def main():
    user_input = input("Input: ")
    print(f"Output: {shorten(user_input)}")


def shorten(words):
    vowels = ["a", "e", "i", "o", "u"]
    shortened_words = ["" if letter.lower() in vowels else letter for letter in words]
    return "".join(shortened_words)


if __name__ == "__main__":
    main()
