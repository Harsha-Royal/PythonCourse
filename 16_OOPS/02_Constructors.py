class Employee:
    def __init__(self, salary, name, bond):
        self.salary = salary # create an instance attribute of name salary and assign it with salary
        self.name = name
        self.bond = bond
        pass

    def get_salary(self):
        return self.salary

    def get_info(self):
        print(f"THe name of the employee is {self.name}. salary is {self.salary}. he bond is for {self.bond} years")


e1 = Employee(34000, "Harsha",4)

e1.get_info()
