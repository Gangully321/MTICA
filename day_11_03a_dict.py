#ADDING TWO LISTS INTO ONE DICTONARY

fruits=['Mango','Orange','Banana','apple']
cost=[25,50,20,100]
g=dict()
for i,j in zip(fruits,cost):
    g[i]=j

print(g)
