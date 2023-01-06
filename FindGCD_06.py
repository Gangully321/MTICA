def findFactors(n):
    temp=list()
    if n>=0:
        for i in range(1,n+1):
            if n%i==0:
                temp.append(i)
        print(temp)
        return temp
def findGCD(n1,n2):
    l1=findFactors(n1)
    l2=findFactors(n2)
    s1=set(l1)
    s2=set(l2)
    ans=list(s1.intersection(s2))
    ans.sort()
##    print(ans)
    return ans[-1]
n1=int(input())
n2=int(input())
print(findGCD(n1,n2))
