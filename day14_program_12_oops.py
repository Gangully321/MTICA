class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    def __add__(self,ob):
        temp=self.real+ob.real ,self.imag+ob.imag
        return temp
    def __sub__(self,a):
        temp=self.real-a.real ,self.imag-a.imag
        return temp
    def __mul__(self,b):
        temp=self.real*b.real ,self.imag*b.imag
        return temp
##    def __div__(self,c):
##        temp=self.real%c.real ,self.imag%c.imag
##        return temp
    def __str__(self):
        return(self.real,self.imag)


obj=Complex(3,4)
ob2=Complex(5,8)
o=obj+ob2
o=obj-ob2
o=obj*ob2
#o=obj%ob2
print(o)
