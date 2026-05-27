distances = {
    "earth": 163,
    "venus": 136,
    "moon": 80,
    "mars": 150,
    "saturn": 400,
    "jupiter": 300
}

# Scenario 1. (this will show all the plants:distance that were included in the dic)
def main():
    for planet in distances.keys():
        print(f"{planet} is {distances[planet]} AU from the Sun.")
main()
# this will print out:
# ...
# mars is 150 AU from the Sun.
# saturn is 400 AU from the Sun.
# jupiter is 300 AU from the Sun.
# ...

# Scenario 2.
def main():
    for how_far in distances.values():
        print(f"{how_far} AU is {convert(how_far)} meters.")

def convert(au):
    return au * 12345678965542

main()
# this will print out
