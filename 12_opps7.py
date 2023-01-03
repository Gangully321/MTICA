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
        
inp=int(input())
a=Number(inp)

print(inp,'is ',a.evenNumber())
print('Factorial of',inp,'is',a.calculateFactrial())
