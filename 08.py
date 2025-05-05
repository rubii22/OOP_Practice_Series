# 8. The super() Function

# Assignment:
# Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.


class Person:
    def __init__(self, name):
        self.name = name    

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  
        self.subject = subject  

    def display_info(self):
        print(f"Teacher's Name: {self.name}")
        print(f"Subject: {self.subject}")

teacher = Teacher("John Doe", "Mathematics")

teacher.display_info()
