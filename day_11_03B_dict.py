#MERGE TWO PYTHON DICTONARY INTO ONE
#method-1
fruits={'Mango':1,'Orange':2,'Banana':3,'apple':4}
cost={'Mango':1,'pineapple':2,'lemon':3,'apple':4}
ganguly={**fruits,**cost}

#method-2
ganguly=ganguly.copy()
ganguly.update(ganguly)
print(ganguly)
print(ganguly)
