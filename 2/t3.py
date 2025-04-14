class Employee():
    salary=30000
    def __init__(self,f_name,l_name):
        self.name=f_name
        self.family=l_name
    def Employees_salaries(self):
        print(f"firstname:{self.name}\n lastname:{self.family}\n salary:{self.salary}")




e1=Employee("hamoun","khatirzad")
e1.Employees_salaries()

        





