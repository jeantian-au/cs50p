x = float (input ("What's X?"))
y = float (input ("What's Y?"))

# If we have 1000 +32265 large number, we can use the below to show the digits every 1000
# z = round (x+y)
# print (f"{z:,}")

# if we use divide, and the remains is undefinte, the below version will only show two digits after the decimal.
z = x/y
print (f"{z: .2f}")