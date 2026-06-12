import random

cards = ["jack", "queen", "king"]

def main():
    # sample with replacement ie. will return ["jack", "jack"]
    print(random.choices (cards, k=2))
    # sample without replacement ie. will return two unique item ["jack", "queen"]
    print(random.sample(cards, k=2))


main()