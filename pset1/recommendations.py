# This is to recommend games for the below four options:
# difficult / Casual
# Multiplayer / Single-player
# will return the four recommended games:
# Poker, Minecraft, Zelda, Rooms

def main():
    difficulty = input("Difficult of Casual? ")
    if not (difficulty == "Difficult" or difficulty == "Casual"):
        print("Please choose a valid difficulty level. ")
        return

    player = input("Multiplayer or Single-player: ")
    if not (player == "Multiplayer" or player == "Single-player"):
        print("Please enter a valid number of players. ")
        return

    if difficulty == "Difficult" and player == "Multiplayer":
        recommend("Poker")
    elif difficulty == "Difficult" and player == "Single-player":
        recommend("Minecraft")
    elif difficulty == "Casual" and player == "Multiplayer":
        recommend("Zelda")
    else:
        recommend("Rooms")

def recommend(game):
    print("you can play", game)

main()
