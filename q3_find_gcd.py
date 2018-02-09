##Computing the greatest common divisor

def gcd(a,b):
    if b > a:
        return gcd(b,a)
    r = a%b
    if r == 0:
        return b
    return gcd(r,b)

print("GCD of 24 and 16 is {}".format(gcd(24,16)))
print("GCD of 255 and 25 is {}".format(gcd(255,25)))
