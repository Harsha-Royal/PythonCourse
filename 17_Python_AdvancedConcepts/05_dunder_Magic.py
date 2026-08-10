#"dunder" refers to methods or attributes with double underscores at the beginning and end of their names, used to define special or "magic" behavior in objects.

class Employee:
    company = "Google"

    def __init__(self,name , salary):
        self.name = name
        self.salary = salary

    def __str__(self):
        return f"The name is {self.name} and the salary is {self.salary}"

    def __repr__(self):
        return f"The name is {self.name} and the salary is {self.salary}"

    def __len__(self):
        return len(self.name)

e = Employee("Harsha",100000)

print(str(e))

print(repr(e))

print(len(e))
