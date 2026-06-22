import csv
import sys
from datetime import date
from datetime import datetime


class Cat:
    def __init__(self, breed, name, gender, color, weight, birthday):
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
        gender = input("Gender:(Male/Female/Desexed)").lower()
        color = input("Color: ").title()
        weight = float(input("Weight(KG): "))
        birthday = input("Date of birth (YYYY-MM-DD): ")
        return cls(name, gender, color, weight, birthday)

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
        if gender not in ["Female", "Male", "Desexed"]:
            raise ValueError("Invalid gender")
        self._gender = gender

    @property
    def birthday(self):
        return self._birthday

    def birthday(self, birthday):
        if birthday not in rf"^\d{4}-\d{2}-\d{2}$":
            raise sys.exit("Invalid date")
        self._birthdat = birthday

    @property
    def weight(self):
        return self._weight

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
        input("Do you want to 1.Register / 2.Read / 3. Exit a cat's information? ")
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
        age = calculate_age(cat_to_read.birthday)
        print(f"And it's currently {age} years old.")

        if result is None:
            response = input(
                "This cat has not been registered yet, would you like to register? reply Y/N"
            )
            if response == "Y":
                cat_to_register = Cat.get()
                add_data(cat_to_register)
            else:
                sys.exit("Goodbye!")
        else:
            read_data(cat_to_read)

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
            if row["Name"].lower == cat.lower().strip():
                return str(cat)
    return None


def calculate_age():
    dob = Cat.birthday
    born_date = datetime.strptime(dob, "%Y-%m-%d")
    born = date.born_date()
    today = date.today()
    age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    return age


if __name__ == "__main__":
    main()
