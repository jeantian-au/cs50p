def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

# rule out all the scenarios that's False.
# 1. digits are not right
# 2. first and second digit should both be alphabet
# 3. digit in the middle is not right)
# 4. if there's special characters
# 5. if there's number:

def is_valid(s):

    if not (2 <= len(s) <= 6):
        return False

    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    number_appears = False

    for user_input in s:
        if not user_input.isalnum():
            return False

        if user_input.isdigit():
            if not number_appears and user_input == "0":
                return False
            number_appears = True

        if user_input.isalpha():
            if number_appears:
                return False

    return True


main()

