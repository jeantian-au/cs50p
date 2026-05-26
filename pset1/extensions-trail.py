#In a file called extensions.py, implement a program that prompts the user
# for the name of a file and then outputs that file’s media type
# if the file’s name ends, case-insensitively, in any of these suffixes:
#.gif .jpg .jpeg .png .pdf .txt .zip
#If the file’s name ends with some other suffix or has no suffix at all,
#output application/octet-stream instead, which is a common default.

def main():
    file_name = input("File name:").lower()
    image = (".gif", ".jpg", ".jpeg", ".png")
    application = (".pdf", ".txt", ".zip")

    if file_name.endswith(image):
        print(f"image/{suffix(file_name)}")
    elif file_name.endswith(application):
        print(f"application/{suffix(file_name)}")
    else:
        print("application/octet-stream")

def suffix(new_name):
    new_name = new_name.split(".")[-1]
    return

main()