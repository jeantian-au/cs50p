expression = input("Expression: " )
x, y, z = expression.split(" ")

if y == "+":
    n = int(x) + int(z)
elif y == "-":
    n = int(x) - int(z)
elif y == "*":
    n = int(x) * int(z)
elif y == "/":
    n = int(x) / int(z)

print(f"{n:.1f}")
