###question
##jj0jj
##j000j
##00000

def printSeries(ch,n):
    sp='  '
    for i in range(0,n):
        print(sp*(n-i-1)+ch*(2*i+1)+sp*(n-i-1))
    return None
inp=input()
inpnum=int(input())
printSeries(inp,inpnum)

