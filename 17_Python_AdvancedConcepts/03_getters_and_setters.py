class Employee:
    def __init__(self,name, salary):
            self.name = name
            self.salary = salary
    @property
    def first_name(self):
          n = self.name.split(" ")
          return n[0]
    
    @first_name.setter
    def first_name(self, newFirstName):
          n = self.name.split(" ")
          
          new_name = f"{newFirstName}  {n[1]}"
          self.name = new_name


e = Employee("Harsha Kalahasthi",100000)

print(e.name)
print(e.first_name)
e.first_name = "Harshaaaaa"
print(e.name)
print(e.first_name)
