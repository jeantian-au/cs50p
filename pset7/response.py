import validators

user_email = input("What's your email address? ")

check_validation = validators.email(user_email)

if check_validation:
    print("Valid")

else:
    print("Invalid")
