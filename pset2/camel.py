
def main():
    camel = input("camelCase: ")
    print(f"snake_case: {snake_version(camel)}")

def snake_version(words):
    lower_letter = []
    current_word = words[0]

    for letter in words[1:]:
        if letter.isupper():
            lower_letter.append(current_word.lower())
            current_word = letter
        else:
            current_word += letter

    lower_letter.append(current_word.lower())

    return "_".join(lower_letter)

main()
