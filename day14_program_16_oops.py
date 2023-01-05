class Employee:
    empCount = 0
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
        Employee.empCount +=1 
    def displayCount (self):
               print("Total employee %d" % Employee.empCount)
    def displayEmployee(self):
        print("Name :",self.name,",salary:",self.salary)
        
emp1=Employee("Nikil",8888)
emp1.displayEmployee()
print("is salary an attribute:",hasattr(emp1,'salary'))
print(getattr(emp1,'salary'))
setattr(emp1,'salary',7000)
print("modify salary",getattr(emp1,'salary'))
print(hasattr(emp1,'desg'))
setattr(emp1,'desg','manager')
print(hasattr(emp1,'desg'))
print("Added Attribute",getattr(emp1,'desg'))
delattr(emp1,'salary')
print("is salary an attribute:",hasattr(emp1,'salary'))
      
