class Cat:
    def __init__(self,color,legs):
        self.color=color
        self.legs=legs
    def __str__(self):
        temp= 'cat is ' +self.color+ ' color ' + 'and has ' +str(self.legs)+ ' legs'
        return temp

if __name__=="__main__":
    pet1=cat(" ginger ", 4 )
    print(pet1.legs)
    print(pet1.color)
    print(pet1)

    pet2=cat( "brown" , 4 )
    print(pet2.legs)
    print(pet2.color)
    print(pet2)
    
