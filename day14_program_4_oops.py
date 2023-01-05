class Wolf:
    price=500
    def __init__(self,name,color):
        self.name=name
        self.color=color
    def bark(self):
        print('Grr..')
class Dog(Wolf):

    def bark1(self):
        print("woof")

if __name__== "__main__":
    pet1=Dog("leo","brown")
    pet1.bark()
    pet1.bark1()
    print(pet1.name,"is of colour",pet1.color)
