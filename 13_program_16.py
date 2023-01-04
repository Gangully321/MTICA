def add(n1,n2):
    temp=n1+n2
    global a,b
    a+=10
    print("output of globals:",globals())
    print("output of locals:",locals())
    return temp
a=int(input())
b=int(input())
c=add(a,b)
print(a,'+',b,'=',c)



##output:
##
##    output of globals: {'__name__': '__main__', '__doc__': None, '__package__': None, '__loader__': <class '_frozen_importlib.BuiltinImporter'>, '__spec__': None, '__annotations__': {}, '__builtins__': <module 'builtins' (built-in)>, '__file__': 'C:/Users/User/Desktop/python practice _2721113/day13/13_program_15.py', 'add': <function add at 0x000001B6A42FD120>, 'a': 12, 'b': 3}
##output of locals: {'n1': 2, 'n2': 3, 'temp': 5}
##12 + 3 = 5
