# Determining leap years

year = int(input("Enter year:"))

if year % 4 == 0 and year % 100 != 0:
    print("This is a leap year.")

elif year < 0:
    print("Invalid. Enter again.")

else:
    print("This is a non-leap year.")
