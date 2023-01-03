class Rectangle:
    def __init__(self,length,width):
        assert(length>=0 and width>=0),"Invalid"
        self.length=length
        self.width=width
        
    def calculatePerimeter(self):
        return (self.length+self.width)*2
    def calculateArea(self):
        return self.length*self.width
    
length=int(input())
width=int(input())
try:
    m=Rectangle(length,width)
    print('perimeter of a rectangle:',m.calculatePerimeter())       
    print('area of a rectangle:',m.calculateArea())
except AssertionError as ob:
    print(ob)
