l=(input()).split()
m=(input()).split()
print(*[int(i)+int(j)for i,j in zip(l,m)])
























##class Vector2D:
##    def __init__(self,x,y):
##        self.x=x
##        self.y=y
##    def __add__(self,ob):
##        return Vector2D(self.x+ob.x,self.y+ob.y)
##    def __sub__(self,other):
##        return Vector2D(self.x-other.x,self.y-other.y)
##first=Vector2D(5,6)
##second=Vector2D(3,4)
##result=first+second
##print(result.x)
##print(result.y)
##result=first-second
##print(result.x)
##print(result.y)
##                                                                      
