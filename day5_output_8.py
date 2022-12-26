def count(g):
    j_vowel=''
    j_consnant=''
    j_digits=''
    j_special=''
    for i in g:
        if i in 'aeiou':
            j_vowel+=i
        elif i in 'bcdfghjklmnpqrstwxyz':
            j_consnant+=i
        elif i in '0123456789':
            j_digits+=i
        else:
            j_special+=i
    lst=[]
    lst.append((j_vowel))
    lst.append((j_consnant))
    lst.append((j_digits))
    lst.append((j_special))
    return lst
inp=input('enter:')
lst=count(inp)
print("vowles:",lst[0],"\nvowel count:",len(lst[0]),
      "\n\n consnants:",lst[1],"\nconsnants count:",len(lst[0]),
      "\n\n number are:",lst[2],"count of digits",len(lst[2]),
      "\n special:",lst[3],"\nspecial characters:",len(lst[3]))
            
            
            
