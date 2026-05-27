students = ["Hermione", "Harry", "Ron"]
for i in students:
    print(i)

# 从这里引申
for i in [0, 1 ,2]:
    print ("meow")

# 到for i in range 用在int
for i in range(3):
    print("Meow")

# 引申到，把这个string用len来
for i in range(len(students)):
    print (i+1, students[i])
# 这样output就是：
# 1 Hermione
# 2 Harry
# 3 Ron

#Dictionary的用法
students = {
    "Hermione":"Gryffindor",
    "Harry": "Gryffindor",
    "Ron": "Gryffindor",
    "Draco": "Slytherin",
}

for ppl in students:
    print(ppl, students[ppl], sep=",")

# So the for loop does, just like it did with numbers before,
# set "ppl" equals to "Hermione", and then "Harry" ...
# very similar in spirit to iterating with a for loop over a list
# but rather than iterate over the numeric location,0.1.2...
# it iterates pver the keys in this representation here
# keys: "Hermione" "Harry"..
# Values: "Gryffindor","Gryffindor"..
---------------------

# If the keys have more values than just one
# here's a list [] of dictionaries {} with a bit more data into it:
students = [
    {"name":"Hermione", "house":"Gryffindor", "patronus":"otter"}
    {"name":"Harry", "house":"Gryffindor", "patronus":"stag"}
    {"name":"Ron", "house":"Gryffindor", "patronus":"Jack russel terrier"}
    {"name":"Draco", "house":"Slytherin", "patronus":None}
]
# how many keys does the first dictionay have?
# Three! name, house, patronus
# What are the defintion/values of those keys?
# Three! hermione, Gryffindor, otter
# So all the dictionaries have teh SAME keys, with different values

for student in students:
    print(student["name"],student["house"],student["patronus"],sep=".")


