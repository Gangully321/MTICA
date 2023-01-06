from math import sqrt
def check_prime(n):
    if n==1 or n==2 or n==3:
        return n
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return None
    return n
      


def findPrimeFactor(n):
    temp=[]
    for i in range (1,n+1):
        if n%i==0:
            if check_prime(i):
                temp.append(i)
    return temp

  
print("enter two numbers ")
a=int(input())
print(*findPrimeFactor(a))
