#remove all the vowels in the given string

#method-1
string="""hai ra mawa nv sallagundu"""
lst=[]
for i in string:
    if i not in 'aeiouAEIOU':
        lst.append(i)
        
print(*lst)

#method-2

lst=[i for i in string if i not in 'aeiouAEIOU']
print(*lst)
