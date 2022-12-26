def replacedigits(n,i,j):
    n=n.replace('i','#')
    n=n.replace('j','i')
    n=n.replace('#','j')
    return n
inp=input()
i=input()
j=input()
print(replacedigits(inp,i,j))
    
