class Vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
    def __str__(self):
        return 'Vehicle Name : '+self.name+'Speed : '+str(self.max_speed)+\
               ' Mileage : '+str(self.mileage)
class Bus(Vehicle):
    pass
ob=Bus('School volvo',180,12)
print(ob)
    
