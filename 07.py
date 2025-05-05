# 7. Access Modifiers: Public, Private, and Protected

# Assignment:
# Create a class Employee with:
# a public variable name,
# a protected variable \_salary, and
# a private variable \_\_ssn.

# Try accessing all three variables from an object of the class and document what happens.


class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name             
        self._salary = salary        
        self.__ssn = ssn          

# Create an instance of Employee
employee = Employee("John Doe", 50000, "123-45-6789")

# Accessing the public variable 'name'
print(f"Name: {employee.name}")  # Public - Accessible directly

# Accessing the protected variable '_salary'
print(f"Salary: {employee._salary}")  # Protected - Can be accessed but not recommended

# Accessing the private variable '__ssn' (will raise an AttributeError)
try:
    print(f"SSN: {employee.__ssn}")  # Private - This will fail!
except AttributeError as e:
    print(f"Error: {e}")

# Accessing the private variable via name mangling (not recommended)
print(f"SSN (via name mangling): {employee._Employee__ssn}")  # Private - Accessible via name mangling
