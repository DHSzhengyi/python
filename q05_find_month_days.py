#Finding the number of days in a month

import math

month = int(input("Enter month:"))
year = int(input("Enter year:"))

month_word = ["[Invalid]","January","February","March","April","May","June","July","August","September","October","November","December"]

try:
    
    if month == 2:
        if year % 4 == 0 and year % 100 != 0:
            print("February {} has 29 days.".format(year))
        else:
            print("February {} has 28 days.".format(year))

    elif (month == "1","3","5","7","8","10","12"):
        print("{0} {1} has 31 days.".format(month_word[month],year))

    elif (month == "4","6","9","11"):
        print("{0} {1} has 30 days.".format(month_word[month],year))

except IndexError:
    print("Invalid. Enter again.")
