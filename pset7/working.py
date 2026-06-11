import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    time_pattern = r"([1-9]|1[0-2])(?::([0-5][0-9]))?\s+(AM|PM)"

    if matches := re.search(rf"^{time_pattern}\sto\s{time_pattern}$", s):
        start_hour = matches.group(1)
        start_min = matches.group(2)
        start_half = matches.group(3)

        end_hour = matches.group(4)
        end_min = matches.group(5)
        end_half = matches.group(6)

        if start_min is None:
            start_min = "00"
        if start_hour == "12":
            start_hour = "00"
        if end_min is None:
            end_min = "00"
        if end_hour == "12":
            end_hour = "00"

        if "AM" == start_half and "PM" == end_half:
            start_time = f"{int(start_hour):02}:{start_min}"
            end_time = f"{int(end_hour)+12:02}:{end_min}"

        elif "AM" == start_half and "AM" == end_half:
            start_time = f"{int(start_hour):02}:{start_min}"
            end_time = f"{int(end_hour):02}:{end_min}"

        elif "PM" == start_half and "PM" == end_half:
            start_time = f"{int(start_hour)+12:02}:{start_min}"
            end_time = f"{int(end_hour)+12:02}:{end_min}"

        elif "PM" == start_half and "AM" == end_half:
            start_time = f"{int(start_hour)+12:02}:{start_min}"
            end_time = f"{int(end_hour):02}:{end_min}"

        return f"{start_time} to {end_time}"

    else:
        raise ValueError


if __name__ == "__main__":
    main()
