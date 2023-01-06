def findFactor(n):
    temp=[]
    for i in range (1,n+1):
        if n%i==0:
            temp.append(i)
    return temp
            
c=int(input())
print(*findFactor(c))
