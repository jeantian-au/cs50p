
# one way to print three times directly and aesthetically.
print("meow\n" *3, end="")

# better this way:
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("How many meow do you want?"))
        if n > 0:
            break
    return n

# range is for Integer! range doesn't take a list of strings
def meow(n):
    for _ in range(n):
        print("meow")

main()
