#Displaying matrix of 0s and 1s

import random

num = int(input("Enter number:"))

a = []
lines = 0

while lines < num:
    for i in range(num):
        if len(a) < num:
            a.append(random.randint(0,1))
        elif len(a) == num:
            break

    print(' '.join(map(str, a)))
    a = []
    lines += 1
    
