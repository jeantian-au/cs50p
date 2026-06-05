import sys


def main():
    if len(sys.argv) <= 1:
        sys.exit("Too few command-line arguments")

    elif len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")

    elif not sys.argv[1].endswith(".py"):
        sys.exit("Not a Python file")

    else:
        try:
            with open(sys.argv[1], "r") as file:
                line_count = 0
                lines = file.readlines()
                for line in lines:
                    clean_line = line.strip()
                    if clean_line == "":
                        continue
                    elif clean_line.startswith("#"):
                        continue
                    else:
                        line_count += 1
                print(line_count)

        except FileNotFoundError:
            sys.exit("File does not exist")


if __name__ == "__main__":
    main()
