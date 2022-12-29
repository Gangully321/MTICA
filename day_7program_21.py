#reverse of a string by using map and lambda functions

#BY USING  MAP FUNCTION
inpL=['anu','anju','ayeesha','ahali']
def rev_str(a):
    return a[::-1]
outL=list(map(rev_str,inpL))
print(inpL)
print(outL)

#BY USING LAMBDA

inpL=['anu','anju','ayeesha','ahali']
outL=list(map(lambda x:x[::-1],inpL))
print(inpL)
print(outL)
