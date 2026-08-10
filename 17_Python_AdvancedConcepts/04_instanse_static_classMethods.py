class Employee:
    company = "Google"

    def __init__(self,name , salary):
        self.name = name
        self.salary = salary

    def printInfo(self):
        print(f"The name is {self.name} and the salary is {self.salary}")

    @staticmethod  #without self keyword and it will not depend on instance variables
    def sum(a , b):
        return a+b
    
    @classmethod
    def changeCompany(cls,new_Company):
        cls.company = new_Company




e1 = Employee("Harsha",100000)

e1.printInfo()

e2 = Employee("Teja",200000)

e2.printInfo()

print(e2.sum(23,32))

print(e2.company)

e2.changeCompany("Meta")

print(e2.company)

print(Employee.company)


