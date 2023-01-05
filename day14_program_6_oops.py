#Dog class inherits from Wolf class with the same attribute or methods,it overrides them.

class Wolf:
    def __init__(self,name,color):
        self.name=name
        self.color=name
    def bark(self):
        print("Grr")

class Dog(Wolf):
    def bark(self):
        print("woof")

pet1=Dog("leo","brown")

pet1.bark()
pet2=Wolf("jimmy","grey")
pet2.bark()
Dog("abc","xyz").bark()

#redefining a method of base class in deveried class is overriding.
