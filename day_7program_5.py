# to find a matrix


m=[[1,2],[3,4],[5,6],[7,8]]
lst=[]
##for row in range(len(m[0])):
##    temp=[]
##    for col in range (len(m)):
##                      temp.append(m[col][row])
##    lst.append(temp)
##print(lst)
##                       

for row in range(len(m[0])):
    temp=[m[col][row] for col in range (len(m))]
    lst.append(temp)
print(lst)
