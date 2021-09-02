class employee():
    def __init__(self,name,age):  
        self.name = name
        self.age = age
        
class Technical_PPL(employee):
    def __init__(self,name,age):
        employee.__init__(self,name,age)
        print('\nEnter details for',self.name)
        self.department = input('Department name: ')
        self.project    = input('Project: ')
        self.salary     = float(input('Salary: '))
    def disp(self):
        print(self.name,self.age,self.department,self.project,self.salary)
 
class NonTechnical_PPL(employee):
    def __init__(self, name, age):
        employee.__init__(self,name,age)
        print('Enter details for',self.name)
        self.workinghrs = int(input('Working Hours:'))
        self.perhrwage  = int(input('Wage per hour:'))
        self.salary=self.workinghrs * self.perhrwage
    def disp(self):
        print(self.name,self.age,self.salary) 

E1 = Technical_PPL ('Bob',30)
E1.disp()
print()
E2 = NonTechnical_PPL('Steve',35)
E2.disp()