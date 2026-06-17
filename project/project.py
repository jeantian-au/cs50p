import csv
import re
import sys
import os
from datetime import datetime
from datetime import date


class Cat:
    def __init__(self, name, breed, gender, color, weight, birthday):
        self.name = name
        self.breed = breed
        self.gender = gender
        self.color = color
        self.weight = weight
        self.birthday = birthday

    def __str__(self):
        return f"{self.name} is a {self.gender} {self.breed} cat with {self.color} color, and weigh {self.weight}kg, it was born on {self.birthday}."

    @classmethod
    def get(cls):
        # 1. Whatever the name is, no restrictions.
        name = input("Name: ").strip().title()

        # 2. User could put whatever breed the cat is for their cat.
        breed = input("What breed is this cat? \n")

        # 3. User has to comply with the below three options.
        gender_dict = {
            "1": "Male",
            "2": "Female",
            "3": "Desexed",
        }
        gender_choice = input(
            "Gender:\n 1.Male \n 2.Female\n 3.Desexed \n Your choice: "
        ).strip()
        gender = gender_dict.get(gender_choice)

        # 4. Cat's color are definitely versatile.
        color = input("Color: ").title()

        # 5. Need user to give back a valid positive weight.
        while True:
            try:
                weight = float(input("Weight(KG): \n"))
                if weight <= 0:
                    raise ValueError
                break
            except ValueError:
                print("Please enter a positive number.")

        # 6. Only accept the date in YYYY-MM-DD format.
        birthday = input("Date of birth (YYYY-MM-DD): \n")

        return cls(name, breed, gender, color, weight, birthday)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Not valid name")
        self._name = name

    @property
    def gender(self):
        return self._gender

    @gender.setter
    def gender(self, gender):
        if gender not in ["Male", "Female", "Desexed"]:
            raise ValueError("Invalid gender")
        self._gender = gender

    @property
    def birthday(self):
        return self._birthday

    @birthday.setter
    def birthday(self, birthday):
        matches = re.search(r"^\d{4}-\d{2}-\d{2}$", birthday)
        if matches:
            self._birthday = birthday
        else:
            raise ValueError("Invalid date")

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, weight):
        if not weight > 0:
            raise ValueError("Please insert a positive number for weight.")
        self._weight = weight


# The above is the Cat class
# =====================================================================================
# The below will be main followed by four functions altogether


def main():
    default_file()
    while True:
        print("=====This is Cats information Center========")
        print("Please select the below options to proceed:")
        print("1. Register a new cat")
        print("2. Lookup an existing cat's information")
        print("3. Exit the program")
        user_choice = input("Your choice: ").strip().lower()

        if user_choice == "1":
            print("Please provide the below information.")
            cat_to_register = Cat.get()
            add_data(cat_to_register)

        elif user_choice == "2":
            cat_to_read = (
                input("Please enter the cat name you want to check out:\n")
                .lower()
                .strip()
            )
            result = read_data(cat_to_read)

            if result is None:
                response = input(
                    "This cat has not been registered yet.\nWould you like to register?\nReply Y/N: "
                )
                if response.strip().upper() == "Y":
                    cat_to_register = Cat.get()
                    add_data(cat_to_register)
                else:
                    sys.exit("Goodbye!")
            else:
                age = calculate_age(result["Birthday"])
                cat = Cat(
                    result["Name"],
                    result["Breed"],
                    result["Gender"],
                    result["Color"],
                    result["Weight"],
                    result["Birthday"],
                )
                print(cat)
                print(age)

        elif user_choice == "3":
            sys.exit("Goodbye!")

        else:
            print("Invalid input. Please choose 1, 2, 3.")


def default_file(filename="cats.csv"):
    try:
        with open(filename, "r") as file:
            return
    except FileNotFoundError:
        with open(filename, "w") as file:
            title_head = ["Name", "Breed", "Gender", "Color", "Weight", "Birthday"]
            writer = csv.DictWriter(file, fieldnames=title_head)
            writer.writeheader()


def add_data(cat, filename="cats.csv"):
    with open(filename, "a", newline="") as file:
        writer = csv.DictWriter(
            file, fieldnames=["Name", "Breed", "Gender", "Color", "Weight", "Birthday"]
        )
        writer.writerow(
            {
                "Name": cat.name,
                "Breed": cat.breed,
                "Gender": cat.gender,
                "Color": cat.color,
                "Weight": cat.weight,
                "Birthday": cat.birthday,
            }
        )
        print(f"{cat.name.title()} has been registered!")


def read_data(cat, filename="cats.csv"):
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row["Name"].lower().strip() == cat.strip().lower():
                return row
        return None


def calculate_age(born_date):
    dob = datetime.strptime(born_date, "%Y-%m-%d").date()
    today = date.today()
    total_months = (today.year - dob.year) * 12 + (today.month - dob.month)

    if today < dob:
        return "It's not born yet!"

    if today.day < dob.day:
        total_months -= 1

    if total_months < 12:
        age = f"It's currently {total_months} months old."

    elif total_months >= 12:
        years = total_months // 12
        if years == 1:
            age = f"It's currently {years} year old."
        else:
            age = f"It's currently {years} years old."

    return age


if __name__ == "__main__":
    main()
