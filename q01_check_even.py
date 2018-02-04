#Check if an integer is odd or even.

number = int(input("Enter number:"))

if number % 2 == 0 and number != 0:
    print("{} is an even number.".format(number))

elif number == 0:
    print("0 is neither odd nor even.")

else:
    print("{} is an odd number.".format(number))
