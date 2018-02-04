#Computing the greatest common divisor

num1 = int(input("Enter the first number:"))
num2 = int(input("Enter the second number:"))

def gcd(a,b):
    if b > a:
        return gcd(b,a)
    r = a%b
    if r == 0:
        return b
    return gcd(r,b)

print("The greatest common divisor of {0} and {1} is {2}.".format(num1, num2, gcd(num1,num2)))
