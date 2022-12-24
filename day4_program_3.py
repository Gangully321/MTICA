import math
def checkprime(num):
    if num<1:
        return 0
    if num==1 or num==2 or num==3:
        return 1
    for j in range(2,int(math.sqrt(num)+1)):
        if num%j==0:
            return 0
    return num
start=int(input())
stop=int(input())
lis=[]
for i in range(start,stop+1):
    if checkprime(i):
        lis.append(i)
print(*lis)
print(len(lis))
        
    

