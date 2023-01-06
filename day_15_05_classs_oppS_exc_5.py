def findLCM(n1,n2):
    if n1<0 or n2<0:
        return "Invalid"
    if n1>n2:
        n1,n2=n2,n1
    i=n2
    while True:
        if i%n1==0 and i%n2==0:
            return i
        else:
            i+=1
    return None
            
print("enter  numbers")
n1=int(input())
n2=int(input())
print(findLCM(n1,n2))
