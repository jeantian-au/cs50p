# In a file called coke.py, implement a program that prompts the user to insert a coin,
# one at a time, each time informing the user of the amount due.
# Once the user has inputted at least 50 cents,
# output how many cents in change the user is owed.
# only accepts coins: 25 cents, 10 cents, and 5 cents.

#
def main():
    coin_types = [5, 10, 25]
    due = 50

    while due > 0:
        print(f"Amount Due: {due}")
        coin_inserted = int(input("Insert Coin: "))
        if coin_inserted in coin_types:
            due = due - coin_inserted
    print(f"Change Owed: {abs(due)}")

main()

