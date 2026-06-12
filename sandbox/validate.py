import re

name = input("What's your name?")
matches = re.search(r"^(.+), (.+), (.+)$", name)

if matches:
    name = matches.group(3) + " " + matches.group(2) + " " + matches.group(1)

print(f"Hello, {name}")
