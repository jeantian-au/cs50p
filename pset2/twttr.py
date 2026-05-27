
def main():
    user_input = input("Input: ")
    print(f"Output: {omitted_version(user_input)}")

def omitted_version(words):
    vowels = ["a", "e", "i", "o", "u"]
    shortened_words = ["" if letter.lower() in vowels else letter for letter in words]
    return "".join(shortened_words)

main()
