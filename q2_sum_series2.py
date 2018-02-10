#Summing series
#1/3 + 2/5 + 3/7 + ... + i/(2i+1)

i = int(input("Enter number:"))

def sum_series2(i):
    if i == 1:
        return 1/3
    else:
        return i/(2*i + 1) + sum_series2(i - 1)

print("{0:.2f}".format(sum_series2(i)))
