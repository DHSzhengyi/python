#Validating triangles and compute perimeter

num1 = float(input("Enter first length in cm:"))           
num2 = float(input("Enter second length in cm:"))
num3 = float(input("Enter last length in cm:"))

if num1 + num2 <= num3:
    print("This triangle is invalid")
elif num2 + num3 <= num1:
    print("This triangle is invalid")
elif num3 + num1 <= num2:
    print("This triangle is invalid")
else:
    result = num1 + num2 + num3
    print("Perimeter:{}cm".format(result))
    print("This triangle is valid.")

