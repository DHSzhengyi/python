#Displaying an integer reversed

num = int(input("Enter number:"))

def reverse(n):
    r = 0
    while n > 0:
        r = r * 10  
        r += n % 10 
        n //= 10    
    return r

print(reverse(num))
