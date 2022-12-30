def printMonth(dn):
    mn=''
    if(dn==0):
        mn='Sun'
    if(dn==1):
        mn='mon'
    if(dn==2):
        mn= 'tue'
    if(dn==3):
        mn= 'wed'
    if(dn==4):
        mn= 'thu'
    if(dn==5):
        mn= 'fri'
    if(dn==6):
        mn= 'sat'
    return mn
def printMonth1(dn):
    mn=''
    if(dn==0):
        mn='Sun'
    elif(dn==1):
        mn='mon'
    elif(dn==2):
        mn= 'tue'
    elif(dn==3):
        mn= 'wed'
    elif(dn==4):
        mn= 'thu'
    elif(dn==5):
        mn= 'fri'
    elif(dn==6):
        mn= 'sat'
    else:
        mn= 'Invalid'
    return mn
import time
for i in range(3):
    inp=int(input())
    start=time.time()
    print(printMonth(inp))
    print((time.time()-start)*1000000000000)
    start=time.time()
    print(printMonth1(inp))
    print((time.time()-start)*1000000000000)
    
    

