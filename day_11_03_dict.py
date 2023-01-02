def arrange(j):
    arrange=dict()
    for i in j:
        if i in arrange:
            arrange[i]+=1
        else:
            arrange[i]=1
    return arrange
def order(n):
    for i in sorted(n):
        print(i,n[i])
      
  

a=int(input())
for i in range(a):
    inp=input()
    order(arrange(inp))
    

    
