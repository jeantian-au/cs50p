name = input("What's your name? ")

# user's input will append to names.txt
with open("names.txt", "a") as file:
    file.write(f"{name}\n")

# with user's name instored in names.txt, i want to print them one by one starting with "hello, name"
with open("names.txt", "r") as file:
    for line in file:
        print("hello", line.rstrip())

# if i want to print out "hello, name" in order:
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")

    # or a more compact way:
with open("names.txt") as file:
    for line in sorted(file):
        print("hello", line.strip())
