a={10,20,30,40,50}
n={50,60,50,90,100}

if a.isdisjoint(n):
   print('no common items')
else:
   print('common items')

print(a.intersection(n))
