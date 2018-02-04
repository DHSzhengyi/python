#Finding the largest n such that n3 < 12000

import math

while True:
    n = 12000 ** (1./3.)
    print("{0:.3f} is the largest number that is smaller than 12000.".format(n))
    if n ** 3 < 12000:
        break
