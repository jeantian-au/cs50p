import re
import sys


def main():
    user_input = input("Hours: ")
    try:
        start, finish = convert(user_input)
        print(f"{h_24(*start)} to {h_24(*finish)}")
    except ValueError:
        raise ValueError


def convert(s):
    time_pattern = r"([1-9]|1[0-2])(?::([0-5][0-9]))?\s+(AM|PM)"
    if matches := re.search(rf"^{time_pattern}\s+to\s+{time_pattern}$", s):
        start_time = (matches.group(1), matches.group(2), matches.group(3))
        end_time = (matches.group(4), matches.group(5), matches.group(6))
    else:
        raise ValueError
    return start_time, end_time


def h_24(hour, minute, half):
    hour = int(hour)

    if half == "AM" and hour == 12:
        hour = 0

    if half == "PM" and hour != 12:
        hour = hour + 12

    if minute is None:
        minute = 0

    return f"{hour:02}:{minute:02}"


if __name__ == "__main__":
    main()
