class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def __mul__(self,b):
        temp=(self.real*b.real-self.imag*b.imag,
              self.real*b.real+self.imag*b.imag)
        return temp
    def __str__(self):
        return(self.real,self.imag)
obj=Complex(3,5)
ob2=Complex(5,7)
o=obj*ob2
print(o)
