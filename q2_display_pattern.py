#display number pattern

num = int(input("Enter number smaller than 10:"))

for i in range(1, num + 1):
    for j in range(i, 0, -1): #numbers arranged from num to 1 in decreasing order
        space = ' '*(2*num - 2*i)
        line = str(j)
        if j == i:
            print(space + line, end = ' ')
        else:
            print(line, end = ' ')
        
    print('')
