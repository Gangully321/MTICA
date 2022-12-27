#extract all digits from an input string
#use list comperhense

#METHOD-1


##inp=input()
##lst=[]
##for i in inp:
##    if i in inp:
##        if i in'0123456789':
##            lst.append(i)
##print(*lst)
##

#method-2
inp=input()
print(*[i for i in inp if i in '0123456789'])

