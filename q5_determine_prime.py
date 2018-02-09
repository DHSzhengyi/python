#Prime number

primecount = 0
linecount = 0
intcount = 1

def is_prime(n):
    if n > 1:
        a = n // 2
        for i in range(2, a + 1):
            if n % i == 0:
                return False
        return n             #if n cannot be divided by any no. < the half of itself
    else:
        return False

while (primecount < 1000):
    intcount += 1
    if is_prime(intcount):
        primecount += 1     # 0 < primecount < 1000
        linecount += 1
        
        if (linecount == 10):   #when reaches 10 numbers / line
            print(intcount)     #print the 10th no.
            linecount = 0       #restart the counting of no. in each line
        else:
            print(intcount, end='\t')   #when no. per line < 10, keep printing the no.
