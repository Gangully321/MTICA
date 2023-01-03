class Number:
    def __init__(self,num):
        self.num=num
    def evenNumber(self):
        if self.num%2==0:
            return 'even'
        else:
            return 'odd'
    def calculateFactrial(self):
        if self.num==0:
            return 1
        res=1
        for i in range(1,self.num+1):
            res *=i
        return res
    def checkArmstrong(self):
        assert self.num>=0,'The number should be >=0'
        temp=str(self.num)
        t=0
        for i in temp:
            t+=int(i)**len(temp)
        if t==self.num:
            return 'armstrong'
        else:
            return 'Not Armstrong'
    def checkPrime(self):
        assert(self.num>=0),"Not valid"
        if (self.num==1 or self.num==2 or self.num==3):
            return "prime"
        for i in range(2,self.num):
            if self.num% i==0:
                return "Not prime"
            return "prime"

inp=int(input())
a=Number(inp)

print(inp,'is ',a.evenNumber())
print('Factorial of',inp,'is',a.calculateFactrial())

try:
    print(inp,'is',a.checkArmstrong())
except AssertionError as aa:
    print(aa)
try:
    prime=a.checkPrime()
    print(prime)
except AssertionError as bb:
        print(bb)
