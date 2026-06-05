import sys
from tabulate import tabulate
import csv


def main():
    if len(sys.argv) <= 1:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    elif not sys.argv[1].endswith(".csv"):
        sys.exit("Not a CSV file")

    else:
        try:
            with open(sys.argv[1]) as file:
                reader = csv.reader(file)
                item_list = []
                for row in reader:
                    item_list.append(row)
                header = item_list[0]
                table = item_list[1:]
                print(tabulate(table, headers=header, tablefmt="grid"))

        except FileNotFoundError:
            sys.exit("File does not exist")


if __name__ == "__main__":
    main()
