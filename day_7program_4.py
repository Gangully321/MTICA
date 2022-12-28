#for all the numbers 1-1000,use a nested
#list/dictionary  comprehension to find the highest
#single digit any of the numbers is divisible by
##
#method-1
lst=[]
for i in range(100,111):
    temp=[]
    for j in range(1,10):
        if i%j==0:
            temp.append(j)
        lst.append([i,max(temp)])
print(lst)

#method-2

lst=[]
for i in range(100,111):
    lst.append([i,max([j for j in range(1,11)if i%j==0])])
print(lst)
    

#method-3
lst=[[i,max([j for j in range(1,11)if i%j==0])]for i in range(100,110)]
print(lst)
