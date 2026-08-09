# Class : Class is a blueprint or a template. Eg. From forr an Exam that contains name, age, electives, father's name etc

# Object : Specific instance created from the template (class.). Eg. From which contains data for Harsha

class Employee:
    company = "HP"

    def get_salary(self):  # self is important here self is way to reference the object of the class which is being created
        print(self)
        return 100000

    #self keyword will be the one for which the object is cretaed

e = Employee() # An Object of class Employee is created here.
print(e.get_salary()) #employee's get salary method is called

e2 = Employee()         
print(e2.get_salary())
print(e2.company)
