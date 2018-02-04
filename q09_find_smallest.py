#Finding the smallest n such that n2 > 12000

import math

while True:
    n = math.sqrt(12000)
    print("{0:.3f} is the smallest number that is larger than 12000.".format(n))
    if n*n > 12000:
        break
