# with open("students.csv") as file:
#     for line in file:

#     # We can do this:
#         row = line.rstrip().split(",")
#         print(f"{row[0]} is in {row[1]}")

#     # OR an easeir compact/readable
#         name, house = line.rstrip().split(",")
#         print(f"{name} is in {house}.")


# =====================================#
# Or if we want to see all students-house situation in ordered way.

# students = []

# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student)

# for student in students:
#     print(f"{student['name']} is in {student['house']}")


# def get_house(student):
#     return student["house"]

# for student in sorted(students, key=get_house):
#     print(f"{student['name']} is in {student['house']}")

# if i want to save the trouble of define a function, just use lambda
# for student in sorted(students, key=lambda s: (s["name"], s["house"])):
#     print(f"{student['name']} is in {student['house']}")


# with open("students.csv") as file:
#     reader = csv.reader(file)
#     for name, house in reader:
#         students.append({"name":name, "house": house})
# for student in sorted(students, key=lambda s:(s["name"],s["house"])):
#     print(f"{student['name']} is in {student['house']}")

##

import csv

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "house": row["house"]})

# if i interpolate the values of some variables in using curly braces,
# and those variables were dictionaries
# in order to index into a dictionary, you use square brackets
for student in sorted(students, key=lambda s: (s["house"], s["name"])):
    print(f"{student['name']} is in {student['house']}")


## 如果我想要往 csv文件里面添加词条。
# 我可以用程序 promp user input， 打开 file (模式是“a" ==append)
# 然后用 csv.DicWriter 这个 method来添加。
#
import csv

name = input("What's your name? ")
house = input("What's your house? ")


with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "house"])
    writer.writerow({"house": house, "name": name})
