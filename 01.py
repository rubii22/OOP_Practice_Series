# 1. Using self

# Assignment:
# Create a class Student with attributes name and marks. Use the self keyword to initialize these values via a constructor. Add a method display() that prints student details.

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("🎓 Student Name:", self.name)
        print("📊 Marks:", self.marks)
        print("—" * 30)


student1 = Student("Luna Sky", 95)
student2 = Student("Zayn Code", 88)
student3 = Student("Echo Ray", 76)

student1.display()
student2.display()
student3.display()
