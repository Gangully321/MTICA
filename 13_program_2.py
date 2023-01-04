##for i in range(2):
##    for j in range(i):
##        inp=input('enter the names:')
##        print(len(inp))

def new(s):
    lst=s.split()
    return [len (i) for i in lst]
ins=input()
print(new(ins))
