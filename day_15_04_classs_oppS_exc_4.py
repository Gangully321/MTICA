# 
#create bus class that inherits from the vehicles class'
#Give the


class Vehicle:
    def __init__(self,name,max_speed,maileage):
        self.name=name
        self.max_speed=max_speed
        self.maileage=maileage

    def seating_capacity(self,capacity):
        return f"the seating capacity if a {self.name}\
is {capacity} passengers"

class Bus(Vehicle):
    
#assign default value to capacity
    def seating_capacity(self,capacity=50):
        return super().seating_capacity(capacity=50)

School_bus=Bus("school volvo",180,100)
print(School_bus.seating_capacity())
