import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    matches = re.search(
        r'iframe(?:[^>]*?)\s+src="https?://(?:www\.)?youtube\.com/embed/([^"\n]+)', s
    )
    if matches:
        return f"https://youtu.be/{matches.group(1)}"
    else:
        return None


if __name__ == "__main__":
    main()
