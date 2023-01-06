class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed=max_speed
        self.mileage=mileage
    def __str__(self):
        return 'MaxSpeed : '+str(self.max_speed)+'\nMilage : '+str(self.mileage)

ob=Vehicle(180,40)
print(ob)
