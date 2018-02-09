#Summing series

print("i\tm(i)")

n = []

for i in range(20):
    i = i + 1
    n.append(i/(i+1))
    m = sum(n)
    print("{0}\t{1:.4f}".format(i, m))
