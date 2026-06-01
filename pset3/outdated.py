import re

month_name = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

alphabet = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

month_number = dict(zip(month_name, alphabet))


def main():
    while True:
        try:
            user_input = input("Date: ").strip()
            date = re.split(r"[/, ]+", user_input)
            month = date[0]
            day = date[1]
            year = date[2]

            if month.isalpha() and month in month_number:
                if "," not in user_input:
                    continue
                mm = int(month_number[month])
                dd = int(day)

            elif month.isdigit():
                if "/" not in user_input:
                    continue
                mm = int(month)
                dd = int(day)

            if (1 <= dd <= 31) and (1 <= mm <= 12):
                print(f"{int(year):04}-{mm:02}-{dd:02}")
                break
            else:
                continue

        except (ValueError, IndexError):
            continue


if __name__ == "__main__":
    main()
