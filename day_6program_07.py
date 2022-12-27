#count the number of space in a given string,
#do not use string function count
#use list compereshion

##$1
##
string='''practice problems for list compreshion in  python.'''
##
##lst=[]
##for i in string:
##    if i== ' ':
##        lst.append(i)
##print(len(lst))

#$2

print(len([i for i in string if i==" "]))
