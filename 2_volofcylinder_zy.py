radius = float(input("Enter radius of the cylinder:"))
length = float(input("Enter length of the cylinder:"))

pi = 3.1415926535897932384626433832795028841971693993751
area = radius*radius*pi
volume = area*length

print("The volume of the cylinder is {0:.2f} cubic metres.".format(volume))
