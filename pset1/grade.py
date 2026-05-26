score = int(input("Score:"))
if score >= 90 or score <= 100:
    print("Grade: A")
elif score >= 80 or score < 90:
    print("Grade:B")
elif score >= 70 or score < 80:
    print("Grade:C")
elif score >= 60 or score < 70:
    print("Grade:D")
else:
    print("Grade:F")