
def printseries(n):
    num=1
    for i in range(1,n+1):
        print()
        for j in range(i):
            print(num,end=' ')
            num+=1
    return None
inp=int(input())
printseries(inp)

