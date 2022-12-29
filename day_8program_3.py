#factorial with exception handling
def fact(num):
    assert(isinstance(num,int)),'factorial not defined non integer'
    assert(num>=0),'factorial of negative number is not defined!'   
    if num==0:
        return 1
    else:
        return num*fact(num-1)
try:
    print(fact(-45))
except Exception as obj:
    print(obj)
try:
    print(fact(4.5))
except Exception as obj:
    print(obj)
try:
    print(fact(45))
except Exception as obj:
    print(obj)
try:
    print(fact('today'))
except Exception as obj:
    print(obj)
