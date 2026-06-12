menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}


def main():

    fee = 0

    while True:
        try:
            user_input = input("Items: ").strip().title()
            fee += menu[user_input]
            print(f"Total fee is: ${fee:}")

        except KeyError:
            continue

        except EOFError:
            break


if __name__ == "__main__":
    main()
