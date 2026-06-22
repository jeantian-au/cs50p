from datetime import date, datetime
import inflect
import sys


def main():
    dob = input("Date of Birth: ")
    try:
        date1 = datetime.strptime(dob, "%Y-%m-%d").date()
    except Exception:
        sys.exit("Invalid date")
    today = date.today()
    delta = (abs(date1 - today)).days * 1440
    delta_minute = convert_minutes(delta)
    print(f"{delta_minute} minutes")


def convert_minutes(minutes):
    p = inflect.engine()
    words = p.number_to_words(minutes, wantlist=False).replace("and ", "")
    return words.capitalize()


if __name__ == "__main__":
    main()
