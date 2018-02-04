#Finding the two highest scores

num_student = int(input("Enter number of students:"))

students = {}
scores = []

for i in range(num_student):
    name = input("Enter name: ")
    score = int(input("Enter score: "))
    if score in students:
        students[score].append(name)
    else:
        students[score] = []
        students[score].append(name)
    scores.append(score)

scores.sort()

maximum = students[scores[len(scores)-1]]

x = len(maximum)

smaximum = students[scores[len(scores)-(x+1)]]

print("Student with highest score is {0}".format(' and '.join(maximum)))
print("Student with second highest score is {0}".format(' and '.join(smaximum)))
