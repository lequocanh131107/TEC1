class Person:
    total = 0
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade
        Person.total += 1

n = int (input("Enter number of students"))

p = []
for i in range(n):
    name = input("enter student's name")
    age = input("enter student's age")
    grade = input("enter student's grade")
    p1 = Person(name, age, grade)
    p.append(p1)

total_grade = 0 
for i in range(n):
    total_grade += p[i].grade

av = total_grade / Person.tool

if(av < 0 or av > 10):
    print (" kcogi")
else:
    if(av > 9):
        print("sx")
    if(av > 8):
        print("gioi")
    if(av > 7):
        print("kha")
    if(av > 5):
        print("pass")
    else:
        print("fail")

print(av)