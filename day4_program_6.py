def replace3by5(n):
    n=str(n)
    n=n.replace('3','#')
    n=n.replace('5','3')
    n=n.replace('#','5')
    return n
inp=int(input())
print(replace3by5(inp))
    
