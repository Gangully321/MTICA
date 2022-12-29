#Division by Zero problem using exception handling
def div(a,b):
    assert(isinstance(a,int)or isinstance(a,float)),\
        'argument should be either integer or float'
    assert(isinstance(b,int)or isinstance(b,float)),\
        'argument should be either integer or float'
    assert(b!=0),"Divison by zero is not defined"
    return a/b       
try:
    print(div(55,0))
except AssertionError as obj:
    print(obj)
try:
    print(div(20,3))
except AssertionError as obj:
    print(obj)
try:
    print(div(100,20))
except AssertionError as obj:
    print(obj)

