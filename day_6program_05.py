#even numbers


lst=[]
for i in range(1,1001):
    if i%2==0:
        lst.append(i)
print(*lst)

#odd numbers
lst=[]
for i in range(1,1001):
    if i%2!=0:
        lst.append(i)
print(*lst)

