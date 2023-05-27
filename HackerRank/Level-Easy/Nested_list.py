"""
Given the names and grades for each student in a class of  students,
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade,
order their names alphabetically and print each name on a new line.

example:
recoreds = [['chi',20],['beta',50],['alpha',50]]

expected output:
    alpha
    beta
"""
# first solution

all_students = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    all_students.append([name, score])

grade = []

for i in range(len(all_students)):
    for j in range(i+1,len(all_students)):
        if all_students[i][1] > all_students[j][1]:
            sub = all_students[i]
            all_students[i] = all_students[j]
            all_students[j] = sub
    grade.append(all_students[i][1])

count_of_second_lowest_grade = grade.count(grade[1])  
second_lowest_grade = all_students[1:count_of_second_lowest_grade+1]
names_of_second_lowest_grade = []
for i in range(len(second_lowest_grade)):
    names_of_second_lowest_grade.append(second_lowest_grade[i][0])
names_of_second_lowest_grade.sort()
for name in names_of_second_lowest_grade:
    print(name)
        
print("-"*45)
## second solution 

all_students = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    all_students.append([name, score])

all_students = sorted(all_students, key = lambda x: x[1])
second_lowest_grade = sorted(set(x[1] for x in all_students))[1]
print(second_lowest_grade)

name_of_student = []
for student in all_students:
    if student[1] == second_lowest_grade:
        name_of_student.append(student[0])

print("\n".join(sorted(name_of_student)))