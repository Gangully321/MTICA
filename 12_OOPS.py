#classes are created using the keyword class and indented block,
#which contains class methods

class Cat:
   def __init__(self,color,legs):
      self.color=color
      self.legs=legs
   def __str__(self):
      temp="cat is"+self.color+' color' +'and has'+str(self.legs)+"legs"
      return temp

if __name__=="__main__":
   pet1=Cat("ginger",4)
   print(pet1.legs)
   print(pet1.color)
   print(pet1)

   pet2=Cat("white",3)
   print(pet2.legs)
   print(pet2.color)
   print(pet2)

