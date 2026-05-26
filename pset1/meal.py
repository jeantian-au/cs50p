def main():
    time = input("What time is it? ")
    n = convert(time)

    if 7.0 <= n <= 8.0:
        print("breakfast time")
    elif 12.0 <= n <= 13.0:
        print("lunch time")
    elif 18.0 <= n <= 19.0:
        print("dinner time")

def convert(time_number):
    hour, minutes = time_number.split(":")
    return int(hour) + int(minutes)/60

if __name__ == "__main__":
    main()


