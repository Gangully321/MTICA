#Intersection
#union
#difference

a={1,2,3,4,5,6}
b={5,6,7,8,9,10}
c={5,6,7,8,9,10}

print('Intersection')
print(a.intersection(b))
print('union(unique elements)')
print(a.union(b))
print('union(removing duplicates')
print(a^b)
print('difference')
a.difference(b)
print(a)
b.difference(c)
print(b)
