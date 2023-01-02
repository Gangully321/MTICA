def pattern(ch,n):
    assert(n>=0),'Invalid Input'
    for i in range(n+1):
        print(ch*i)  
ch=input()
n=int(input())
try:
    pattern(ch,n)
except AssertionError as g:
    print(g)
