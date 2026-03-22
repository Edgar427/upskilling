#includes examples for classes and instances, class variables, classmethods and staticmethods
import datetime
class Employee:

    num_of_emps = 0 #class variable
    raise_amt = 1.04 #class variable
    
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

    @classmethod
    def set_raise_amt(cls, amount ):#changing the class variable raise_amt
         cls.raise_amt = amount
    
    @classmethod
    def from_string(cls, emp_str):
         first, last, pay = emp_str.split("-")
         return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
         if day.weekday() == 5 or day.weekday() == 6:
              return False
         else:
              return True
         



emp_1 = Employee("Corey", "Schafer", 50000)  
emp_2 = Employee("Test", "User", 60000) 

my_date = datetime.date(2026, 3, 22)
 
print(Employee.is_workday(my_date))

#emp_str_1 = "John-Doe-70000"
#new_emp_1 = Employee.from_string(emp_str_1)
#print(emp_1)
#print(emp_2)

#print(emp_1.email)
#print(emp_2.fullname())
#Employee.fullname(emp_1) same as above if its def fullname() instead of def fullanme(self)
#print(emp_1.pay)
#emp_1.apply_raise()
#print(emp_1.pay)
#Employee.raise_amt=1.05 #changes overrides
#emp_1.raise_amt = 1.05 #changes overrides
#print(Employee.num_of_emps)
#Employee.set_raise_amt(1.05)
#print(new_emp_1.email)
#print(Employee.raise_amt)
#print(emp_1.raise_amt)
#print(emp_2.raise_amt)

