#create a vehicle class and bus class and inherit vehicle variables to bus class
class Vehicle:
    def __init__(self,name,max_speed,milage):
        self.name=name
        self.max_speed=max_speed
        self.milage=milage

class Bus(Vehicle):
    pass
school_bus=Bus("school Volvo",180,12)
print("Vehicle Name:",school_bus.name,"speed:",school_bus.max_speed,"milage:",school_bus.milage)
