class Vehicle:
    def __init__(self,max_speed,maileage):
        self.max_speed=max_speed
        self.maileage=maileage

model=Vehicle(542,1990)
print(model.max_speed,model.maileage)
