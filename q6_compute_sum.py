#Summing the digits in an integer using recursion

n = int(input("Enter number:"))

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

print("The sum of digits is:", sum_digits(n))
