#Finding the largest number 

num = input("Enter a list of numbers (no commas!):")

num_list = list(map(int, num.split()))

num_list.sort()

print(num_list[-1])
