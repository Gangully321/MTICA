#dictonary 

dict={'hai': 17, 'hhk': 98, 'khd': 763}
ls=[]
for i in dict:
    if dict[i]<50:
        ls.append(i.upper())
print(ls)
