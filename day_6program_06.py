#find all the numbers from 1-1000
#have a 6 in them

#method-1

##lst=[]
##for i in range(900,1001):
##    if '6' in str(i):
##        lst.append(i)
##print(lst)

#method-2

print([i for i in range(700,901) if '7' in str(i)])
