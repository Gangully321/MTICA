#cube of a number

def cube(a):
    return a*a*a
lst=[0,1,2,3,4,5,6,7]
res=list(map(cube,lst))
print(res)

res1=list(map(lambda x:x*x*x,lst))
print(res1)
