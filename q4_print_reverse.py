#Reverse the digits in an integer recursively

n = int(input("Enter number:"))

def reverse_int(n):
    r = 0
    while n > 0:
        r = r*10
        r += n % 10
        n //= 10
    return r

print(reverse_int(n))
