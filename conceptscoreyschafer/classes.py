class Employee:
    num_of_emps = 0
    raise_amount = 1.04 #class variable
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
        Employee.num_of_emps += 1
    def fullname(self):
            return (f"{self.first}, {self.last}")
    
    def apply_raise(self):
         self.pay = int(self.pay * self.raise_amount)




emp_1 = Employee("Corey", "Schafer", 50000)  
emp_2 = Employee("Test", "User", 60000)       
 

#print(emp_1)
#print(emp_2)

#print(emp_1.email)
print(emp_2.fullname())

#Employee.fullname(emp_1) same as above if its def fullname() instead of def fullanme(self)

print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

#Employee.raise_amount=1.05 #changes overrides
#emp_1.raise_amount = 1.05 #changes overrides

print(Employee.num_of_emps)