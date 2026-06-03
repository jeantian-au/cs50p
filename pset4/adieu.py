import inflect

p = inflect.engine()


def main():
    user_inputs = []

    while True:
        try:
            names = input("Name: ").title()
            user_inputs.append(names)

        except EOFError:
            break

    name_list = p.join(user_inputs)
    print()
    print(f"Adieu, adieu, to {name_list}")


if __name__ == "__main__":
    main()
