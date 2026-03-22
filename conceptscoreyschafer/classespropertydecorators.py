class Employee:

    num_of_emps = 0 #class variable
    raise_amt = 1.04 #class variable
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    @property
    def email(self):
            return (f"{self.first} {self.last}@email.com")

    @property
    def fullname(self):
            return (f"{self.first}{self.last}")
    
    @fullname.setter
    def fullname(self, name):
          first, last = name.split(" ")
          self.first = first
          self.last = last

    @fullname.deleter
    def fullname(self):
          print("Delete Name")
          self.first = None
          self.last = None
    
emp_1 = Employee("Corey", "Schafer")  
emp_2 = Employee("Test", "User") 

emp_1.first = "Jim"
emp_1.fullname = "COrey Schafer"
print(emp_1.first)
print(emp_1.email)
print(emp_1.fullname)

del emp_1.fullname

print(emp_1.fullname)

