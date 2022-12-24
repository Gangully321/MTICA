def checkarmstrong(num):
    num=str(num)
    n=len(num)
    total=0
    for i in num:
        total+=int(i)**n
        if int(num)==total:
            return 1
    return 0
inp=int(input())
if checkarmstrong(inp):
        print("YES")
else:
    print("NO")

    
