def findLcm(n1,n2):
    if n1<0 or n2<0:
        print('INVALID')
    if n1>n2:
        n1,n2=n2,n1
    greater=n2
    while True:
        if greater%n1==0 and greater%n2==0:
            return greater
        greater+=1

n1=int(input())
n2=int(input())
print(findLcm(n1,n2))
