#extract all vowels from an input string
#use list comprehension

string=input()

lst=[]
for i in string:
    if i in "aeiouAEIOU":
        lst.append(i)
print(*lst)


lst=[i for i in string if i in 'aeiouAEIOU']
print(*lst)
