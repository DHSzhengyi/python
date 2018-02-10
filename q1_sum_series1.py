#Summing series
#1 + 1/2 + 1/3 + ... + 1/i

i = int(input("Enter number:"))

def sum_series(i):
    if i == 1:
        return 1
    else:
        return 1 / i + sum_series(i - 1)

print("{0:.2f}".format(sum_series(i)))

