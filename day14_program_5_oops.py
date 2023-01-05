class Animal:       #super class
    def __init__(self,name,color):
        self.name=name
        self.color=color
#cat and dog are subclass.
class Cat(Animal):#to inherite a class from
    def mew(self):#put the super class name is
        print("cat meows")
class Dog(Animal):
    def bark(self):
        print('woof')

if __name__== "__main__":
    print(__name__)
    pet1=Dog("leo","brown")
    pet2=Cat("sqeez","white")
    pet1.bark()
    pet2.mew()
    print(pet1.name)
    print(pet1.name)
