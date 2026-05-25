def main():
    emoticons = input("How are you feeling today?")
    emoji = convert(emoticons)
    print(emoji)

def convert(text):
    new_text = text.replace(":)","🙂").replace(":(","🙁")
    return new_text

main()