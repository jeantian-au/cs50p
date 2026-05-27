results = ["A","B"]
results.append("C")
results.append("D")
results.append("E")
results.append(["F","G","H"])
# this will not add F, G H individually, but will adde [F G H] as one list parallel to C D E
results.remove(["F","G","H"])
#remove this list and below is the proper way to add: .extend()
results.extend(["F","G","H"])

# =============
results = ["A","B","C","D","E","F","G"]
results.remove("D")
# i want to make D which is currently in the 4th place in the list to he first one
results.insert(0,"D")

print(results)


# ======================

SHOWS = ["I Robot 2025", "  alaby", "avatar", "Blackshop", "Shawshenks redemptation", "Spongebob alone"]
def main():
    clean_show = []
    for movie in SHOWS:
        clean_show.append(movie.strip().title())

    print(", ".join(clean_show))


main()
