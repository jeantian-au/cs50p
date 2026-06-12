def main():
    while True:
        try:
            fraction = input("Fraction: ")
            percentage = convert(fraction)
            final = gauge(percentage)
            print(final)
            break
        except (ZeroDivisionError, ValueError):
            continue


def convert(fraction):
    fraction = fraction.split("/")
    x = int(fraction[0])
    y = int(fraction[1])
    if x > y:
        raise ValueError
    return round(int(x) / int(y) * 100)


def gauge(percentage):
    if percentage >= 99:
        return "F"
    elif percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
