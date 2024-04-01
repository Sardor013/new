#1
my_string = "Hello, World!"
print(my_string)


#2
n = int(input().strip())

if n % 2 != 0:
    print("Weird")
elif n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Weird")
elif n % 2 == 0 and n > 20:
    print("Not Weird")




#3
a = int(input())
b = int(input())

sum_ = a + b
ayirma = a - b
kopaytma = a * b

print(sum_)
print(ayirma)
print(kopaytma)




#4
a = int(input())
b = int(input())

c = a // b
d = a / b

print(c)
print(d)




#5
n = int(input())

for i in range(n):
    print(i * i)

#6
n = int(input())

for i in range(1, n + 1):
    print(i, end="")

print()



#7
x = int(input())
y = int(input())
z = int(input())
n = int(input())

coordinates = []

for i in range(x + 1):
    for j in range(y + 1):
        for k in range(z + 1):
            if i + j + k != n:
                coordinates.append([i, j, k])

print(coordinates)



#8
n = int(input())
arr = map(int, input().split())

all_s = sorted(set(arr), reverse=True)

print(all_s[1])



#9
n = int(input())
students = []

for i in range(n):
    name = input()
    score = float(input())
    students.append([name, score])

students.sort(key=lambda x: x[1])

second_grade = sorted(set(score for name, score in students))[1]

for name, score in sorted(students):
    if score == second_grade:
        print(name)



#10
n = int(input())

student = {}

for i in range(n):
    name, *marks = input().split()
    marks = list(map(float, marks))
    student[name] = marks

query_name = input()

average_marks = sum(student[query_name]) / len(student[query_name])

print("{:.2f}".format(average_marks))

