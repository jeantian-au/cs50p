import re

url = input("URL: ").strip()

# username = re.sub(r"^http(s)?://twitter\.com/", "", url)

if matches := re.search(r"^https?//:(wwww\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print(f"username is", matches.group(2))

# or we can do this instead: ?: would be uncapturing....
if matches := re.search(r"^https?//:(?:wwww\.)?twitter\.com/(.+)$", url, re.IGNORECASE):
    print(f"username is", matches.group(1))


import re


def main():

    code = input("Hexadecimal color code:")
    pattern = r"[]{6}"
    match = re.search(pattern, code)
    if match:
        print(f"Valid, color code is: {match.group()}")
    else:
        print("Invalid")


main()
