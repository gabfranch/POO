# 

class Student:

    class_year = 2024
    num_students = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1
    

student1 = Student('Pablo', '164')
student2 = Student('Jorge', 24)
student3 = Student('Pato', 12)
student4 = Student('Foca', 12)

print(student2.name, student2.age, Student.class_year, Student.num_students)
print(f"My graduating class of {Student.class_year} has {Student.num_students} students")
print(student1.name, student2.name, student3.name, student4.name)