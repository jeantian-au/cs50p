print("#")
print("#")
print("#")

def print_square(size):

    #for each row in square
    for i in range(size):

        #for each brick in row:
        for j in range(size):

            #print brick
            print("#", end="")

        print()
        #notice this loop here is just iterating for each brick in the row

-=-----
#or this string multification trick...or the above loop function
def print_square(size):
    for i in range(size):
        print_row()

def print_row(width):
    print("#" * width)

main()
