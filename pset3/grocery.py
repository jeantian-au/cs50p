def main():
    grocery = {}
    while True:
        try:
            items = input().strip().lower()
            grocery[items] = grocery.get(items, 0) + 1

        except ValueError:
            continue

        except EOFError:
            print()
            for key in sorted(grocery):
                print(f"{grocery[key]} {key.upper()}")
            break


if __name__ == "__main__":
    main()
