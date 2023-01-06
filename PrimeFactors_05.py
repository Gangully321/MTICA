import math
n=int(input())
l=list()
p=list()
def prime(x):
    if x==1 or x==2 or x==3:
        return x
    else:
        for i in range(2,(x//2+1),1):
            if x%i==0:
                return 0
        return x
if n>=0:
    for i in range(1,n+1):
        if n%i==0:
            l.append(i)
    print(l)
    for i in l:
        if prime(i):
            p.append(i)
print(*p)

    
