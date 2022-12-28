# construct the list from the squars of each elements in the list ,if the squares is greater than 50.

lst=[12,3,5,7,10,7,6,16]
ans=[]
for i in lst:
    if i*i>50:
        ans.append(i*i)
    
print(ans)
