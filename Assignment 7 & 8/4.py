'''Create a class "Employee" with attributes name and salary. Implement overloaded operators +
and - to combine and compare employees based on their salaries.'''

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __add__(self, other):
        return Employee(self.name + ' & ' + other.name, self.salary + other.salary)

    def __sub__(self, other):
        return self.salary - other.salary

    def __str__(self):
        return f"Employee: {self.name}, Salary: {self.salary}"

name1 = input("Enter first employee's name: ")
salary1 = int(input("Enter first employee's salary: "))
name2 = input("Enter second employee's name: ")
salary2 = int(input("Enter second employee's salary: "))

e1 = Employee(name1, salary1)
e2 = Employee(name2, salary2)

e3 = e1 + e2
salary_difference = e1 - e2

# Display results
print("Combined Employee:", e3)
print("Salary Difference:", salary_difference)
