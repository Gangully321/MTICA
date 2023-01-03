class Student:
   College="MTICA"
   Course="MCA"
   def __init__(self,name,rollno):
      self.name=name
      self.rollno=rollno
   def display_student(self):
      print('Name:'+self.name.title()+'\nrollno:'+str(self.rollno))
      print('College:'+self.College+'\nCourse:'+(self.Course))

lstobj=[]
for i in range(2):
   n=input()
   inp=int(input())
   temp='obj'+str(i)
   temp=Student(n,inp)
   lstobj.append(temp)
for i in lstobj:
   i.display_student()
      
