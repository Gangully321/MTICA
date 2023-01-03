class Circle:
    def __init__(self,radius):
        self.radius=radius
    def perimeter(self):
        return 2*3.14159*(self.radius)
    def area(self):
        return 3.14159*(self.radius)**2
r=int(input())
a=Circle(r)
print('perimeter:',a.perimeter())
print('area:',a.area())    
