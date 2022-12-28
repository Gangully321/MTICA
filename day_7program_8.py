''' lst =[10,15,20,25,30,35,40,45]
use the list compreshesion to costruct a new list but add 6 to each item '''

#method-1
lst =[10,15,20,25,30,35,40,45]
jan=[]
for i in lst:
    jan.append(i+6)
print(jan)

#method-2

lst =[10,15,20,25,30,35,40,45]
jan=[(i+6)for i in lst]
print(jan)
