import csv
import sys
import re
from datetime import date
from datetime import datetime


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
        name = input("Name: ").strip().title()
        breed = input("What breed is this cat? ")
        gender = input("Gender:(Male/Female/Desexed)").lower()
        color = input("Color: ").title()
        weight = float(input("Weight(KG): "))
        birthday = input("Date of birth (YYYY-MM-DD): ")
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
        if gender not in ["female", "male", "desexed"]:
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
        if not float(weight) > 0:
            raise ValueError("Please insert a positive number for weight.")
        self._weight = weight


# The above is the class
# =====================================================================================
# The below will be main followed by four functions altogether


def main():
    default_file()

    user_choice = (
        input("Do you want to 1.Register / 2.Read a cat's information? ")
        .strip()
        .lower()
    )
    if user_choice in ["register", "1"]:
        print("Please provide the below information.")
        cat_to_register = Cat.get()
        add_data(cat_to_register)

    elif user_choice in ["read", "2"]:
        cat_to_read = (
            input("Please enter the cat name you want to check out:").lower().strip()
        )
        result = read_data(cat_to_read)
        cat_info = Cat(result["name"])

        if result is None:
            response = input(
                "This cat has not been registered yet, would you like to register? reply Y/N"
            )
            if response.strip().upper() == "Y":
                cat_to_register = Cat.get()
                add_data(cat_to_register)
            else:
                sys.exit("Goodbye!")
        else:
            age = calculate_age(result["Birthday"])
            print(cat_info)
            print(f"And it's currently {age} years old.")

    else:
        sys.exit(
            "Please choose either '1'(Register) or '2'(Read), you only need to input the number: "
        )


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
            if row["Name"].lower().strip() == cat:
                return row
        return None


def calculate_age(dob):
    born_date = datetime.strptime(dob, "%Y-%m-%d")
    born = born_date.date()
    today = datetime.today().date()
    age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    return age


if __name__ == "__main__":
    main()
