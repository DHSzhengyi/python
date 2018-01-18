n = int(input("Enter a number between 0 and 1000:"))

if 0 < n < 1000:
    def sum_digits(n):
        s = 0
        while n:
            s += n % 10 #add to total
            n //= 10
        return s
    print("The sum of digits is:", sum_digits(n))

else:
    print("Number must be between 0 and 1000!")
