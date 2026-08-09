class Employee:
    company = "Asus"

    def __init__(self, salary, name, bond, company):
        self.salary = salary # create an instance attribute of name salary and assign it with salary
        self.name = name
        self.bond = bond
        self.company = company
       
    def get_salary(self):
        return self.salary

    def get_info(self):
        print(f"THe name of the employee is {self.name}. salary is {self.salary}. he bond is for {self.bond} years")


e1 = Employee(34000, "Harsha",4,"Tesla")
print(e1.company) #output : Tesla will always print instance attribute whenever present
print(Employee.company)#output : Asus this will always print class attribute

#Object introspection

print(dir(e1))

