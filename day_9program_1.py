def printseriesINC(ch,n):
    assert isinstance(ch,str),"first number should be string"
    assert isinstance(n,int),"second number should be integer"
    for i in range(1,n+1):
        print(ch*i)

inpCh=input("enter a character:")
inpNum=int(input("enter a no:"))
try:
    printseriesINC(inpCh,inpNum)
except AssertionError as a:
    print(a)

