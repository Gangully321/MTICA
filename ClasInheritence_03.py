class Vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage
    def __str__(self):
        return 'Vehicle Name : '+self.name+'Speed : '+str(self.max_speed)+\
               ' Mileage : '+str(self.mileage)
    def seatingCapacity(self,capacity):
        self.capacity=capacity
        print(self.capacity)
        return f'Seating capacity of a bus is {capacity}'
class Bus(Vehicle):
    pass
##    def seatingCapacity(self,capacity=50):
##        return f'Seating capacity of a bus is {capacity}'
##    
ob=Bus('School volvo',180,12)
##print(ob.seatingCapacity())
ob.seatingCapacity(67)
    
