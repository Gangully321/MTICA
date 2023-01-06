import math
n=int(input())
l=list()
pl=list()
if n>=0:
    for i in range(1,n+1):
        if n%i==0:
            l.append(i)
else:
    print('Invalid')
print(*l)

for i in l:
    if i==1 or i==2 or i==3 :
        pl.append(i)
    else:
        for j in range(2,int(math.sqrt(i)+1)):
            if i%j==0:
                break
        pl.append(i)       
print(*pl)
    
