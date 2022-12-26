def removeDuplicates(g):
    g1=''
    for i in g:
        if i not in g1:
            g1+=i
    return g1
inp=input("enter a string:")
print("string without duplicates:",removeDuplicates(inp))





    
