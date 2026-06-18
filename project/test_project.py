from project import calculate_age
from project import read_data
from project import add_data
from project import default_file
from project import Cat
from datetime import date
import os
import csv


def test_calculate_age():
    fixed_today = date(2026, 6, 18)
    assert calculate_age("2025-08-06", fixed_today) == "It's currently 10 months old."
    assert calculate_age("1993-04-21", fixed_today) == "It's currently 33 years old."
    assert (
        calculate_age("2026-06-17", fixed_today)
        == "It's newly born and not even 1 month old."
    )
    assert calculate_age("2026-05-17", fixed_today) == "It's currently 1 month old."
    assert calculate_age("2025-06-17", fixed_today) == "It's currently 1 year old."
    assert calculate_age("2027-08-06", fixed_today) == "It's not born yet!"


def test_read_data():

    multiple_cats = [
        {
            "Name": "Dami",
            "Breed": "Domestic Shorthair",
            "Gender": "Desexed",
            "Color": "Tabby",
            "Weight": "5",
            "Birthday": "2018-02-22",
        },
        {
            "Name": "Xiaomi",
            "Breed": "Domestic Shorthair",
            "Gender": "Male",
            "Color": "Tabby",
            "Weight": "6",
            "Birthday": "2018-02-22",
        },
        {
            "Name": "Aowu",
            "Breed": "Ragdoll",
            "Gender": "Desexed",
            "Color": "Grey",
            "Weight": "4.5",
            "Birthday": "2022-12-18",
        },
    ]
    with open("test_read_cats.csv", "w", newline="") as file:
        writer = csv.DictWriter(
            file, fieldnames=["Name", "Breed", "Gender", "Color", "Weight", "Birthday"]
        )
        writer.writeheader()
        writer.writerows(multiple_cats)

    result = read_data("Dami", "test_read_cats.csv")
    assert result["Name"] == "Dami"
    assert result["Birthday"] == "2018-02-22"
    assert result["Color"] == "Tabby"

    result = read_data("Aowu", "test_read_cats.csv")
    assert result["Breed"] == "Ragdoll"
    assert result["Gender"] == "Desexed"
    assert result["Weight"] == "4.5"

    assert read_data("Mimi", "test_read_cats.csv") is None

    os.remove("test_read_cats.csv")


def test_add_data():
    cat1 = Cat("Xiaomi", "Domestic Shorthair", "Desexed", "Tabby", 6, "2018-02-22")
    cat2 = Cat("Aowu", "Ragdoll", "Desexed", "Grey", 4.5, "2022-12-18")
    default_file(filename="test_add_cats.csv")

    assert add_data(cat1, "test_add_cats.csv") is None
    result = read_data("Xiaomi", "test_add_cats.csv")
    assert result["Name"] == "Xiaomi"

    assert add_data(cat2, "test_add_cats.csv") is None
    result = read_data("Aowu", "test_add_cats.csv")
    assert result["Name"] == "Aowu"

    os.remove("test_add_cats.csv")
