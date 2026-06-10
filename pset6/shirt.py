import os
import sys
from PIL import Image
from PIL import ImageOps


def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")

    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    accepted_extensions = [".jpg", ".jpeg", ".png"]
    input_file = sys.argv[1]
    input_file_ext = os.path.splitext(input_file)[1].lower()
    output_file = sys.argv[2]
    output_file_ext = os.path.splitext(output_file)[1].lower()

    if input_file_ext not in accepted_extensions:
        sys.exit("Invalid input")

    if output_file_ext not in accepted_extensions:
        sys.exit("Invalid output")

    if input_file_ext != output_file_ext:
        sys.exit("Input and output have different extensions")

    try:
        user_image = Image.open(input_file)

    except FileNotFoundError:
        sys.exit("Input does not exist")

    else:
        shirt_image = Image.open("shirt.png")
        size = shirt_image.size
        user_image = ImageOps.fit(user_image, size=size)
        user_image.paste(shirt_image, (0, 0), mask=shirt_image)
        user_image.save(output_file)


if __name__ == "__main__":
    main()
