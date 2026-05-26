name = input("what's you name?")

if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")


match name:
    case "Harry":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Hermione":
        print("Griffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who")


match name:
    case "Harry" | "Ron" | "Hermione":
        print("Gryfifindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who")