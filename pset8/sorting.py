import random


class SortingHat:
    houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]

    @classmethod
    def sort(cls, name):
        return f"{name} you are sorted to {random.choice(cls.houses)}"


class Wand:
    def __init__(self, color, material, length):
        self.color = color
        self.material = material
        self.length = length

    def __str__(self):
        return f"This wand is {self.color} made of {self.material} and {self.length}"

    @classmethod
    def get(cls):
        color = input("What color would you like your wand to be: ")
        material = input("And what matrial? ")
        length = input("How long do you like it build? ")
        return cls(color, material, length)

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, color):
        colors = ["red", "orange", "brown", "black", "purple"]
        if color is None:
            self._color = random.choice(colors)
        elif color not in colors:
            raise ValueError("Not valid color")
        else:
            self._color = color

    @property
    def length(self):
        return self._length

    @length.setter
    def length(self, length):
        if length not in ["3inches", "2.5inches", "3.5inches", "4inches"]:
            raise ValueError
        self._length = length

    def effect(self):
        match self.material:
            case "elm":
                return "🧨"
            case "dragon tail":
                return "🐉"
            case "phenix feather":
                return "🎉"
            case _:
                return "🪄"


def main():

    print(SortingHat.sort("Harry"))
    wand = Wand.get()
    print(wand)
    print(wand.effect())


if __name__ == "__main__":
    main()
