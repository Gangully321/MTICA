#printing all the numbers which are divisible by 8 in range 1-1000!
#method-1
##lst=[]
##for i in range(1,1001):
##    if i%8==0:
##        lst.append(i)
##print(*lst)

#method-2

#print([i for i in range(1,1001)if i%8==0 ])

#method-3

lst=[i for i in range(1,1001) if i%8==0]
print(lst)
