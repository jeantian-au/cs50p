def main():
    while True:
        try:
            fuel_fraction = input("Fraction: ").split("/")
            x = int(fuel_fraction[0])
            y = int(fuel_fraction[1])
            if not (0 <= x <= y):
                continue

        except (ValueError, ZeroDivisionError):
            continue

        else:
            percentage = round((x / y) * 100)
            fuel_status(percentage)
            break


def fuel_status(n):
    if n >= 99:
        print("F")
    elif n <= 1:
        print("E")
    else:
        print(f"{n}%")


if __name__ == "__main__":
    main()
