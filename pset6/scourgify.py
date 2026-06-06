import sys
import csv


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    if not (sys.argv[1].endswith(".csv") and sys.argv[2].endswith(".csv")):
        sys.exit("Not a CSV file.")

    try:
        students_info = []
        with open(sys.argv[1], "r") as input_file:
            reader = csv.DictReader(input_file)
            for row in reader:
                last, first = row["name"].split(",")
                last = last.strip()
                first = first.strip()
                students_info.append(
                    {"first": first, "last": last, "house": row["house"]}
                )
        with open(sys.argv[2], "w") as output_file:
            writer = csv.DictWriter(output_file, fieldnames=["first", "last", "house"])
            writer.writeheader()
            writer.writerows(students_info)

    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")


if __name__ == "__main__":
    main()
