##Aggregation VS Composition

#Aggregation
class Salary:
    def __init__(self,pay,bonus):
        self.pay = pay
        self.bonus = bonus
    
    def annual_salary(self):
        return (self.pay*12)+self.bonus
    
class Employee:
    def __init__(self,name,age, salary):
        self.name = name
        self.age = age
        self.obj_salary = salary
    
    def total_salary(self):
        return self.obj_salary.annual_salary()

salary=Salary(28904,50000)
emp = Employee('Manoj',25,salary)
co = emp.total_salary()
print(co)


#Composition
class Salary:
    def __init__(self,pay,bonus):
        self.pay = pay
        self.bonus = bonus
    
    def annual_salary(self):
        return (self.pay*12)+self.bonus
    
class Employee:
    def __init__(self,name,age, pay,bonus):
        self.name = name
        self.age = age
        self.obj_salary = Salary(pay,bonus)
    
    def total_salary(self):
        return self.obj_salary.annual_salary()

emp = Employee('Manoj',25,28904,50000)
co = emp.total_salary()
print(co)