#Conversion between Miles and Kilometres

print("Miles\tKilometres\tKilometres\tMiles")

for i in range(10):
    A = i + 1
    B = (i+1)*1.609
    C = i*5 + 20
    D = C*0.621371
    print("{0}\t{1:.3f}\t\t{2}\t\t{3:.3f}".format(A, B, C, D))
