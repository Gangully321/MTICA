def removeSpecialchar(s):
    ans=[]
    for i in s:
        if i in '0123456789QWERTYUIOPLKJHGFDSAZXCVBNMmnbvcxzlkjhgfdsapoiuytrewq':
            ans.append(i)
    return ''.join(ans)


inp=input()
print(removeSpecialchar(inp))
