class Student:
    year = 1999
    num_students = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1

Student1 = Student("Rob", 32)
Student2 = Student("Bin", 64)

print(Student1.age)
print(Student2.name)
print(Student2.year)
print(Student.num_students)