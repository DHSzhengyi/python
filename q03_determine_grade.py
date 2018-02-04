#Determine grades

g = int(input("Enter score:"))

if 0 < g <= 34:
    print("Grade obtained is U")

elif 35 < g <= 44:
    print("Grade obtained is S")

elif 45 < g <= 49:
    print("Grade obtained is E")

elif 50 < g <= 54:
    print("Grade obtained is D")

elif 55 < g <= 59:
    print("Grade obtained is C")

elif 60 < g <= 69:
    print("Grade obtained is B")

elif 70 < g <= 100:
    print("Grade obtained is A. Congratulations!")

else:
    print("Invalid score! Score has to be between 0 and 100!")
    
