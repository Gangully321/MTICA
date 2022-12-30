def printMonth(dn):
    mn=''
    if(dn==1):
        mn='January'
    elif(dn==2):
        mn='February'
    elif(dn==3):
        mn= 'March'
    elif(dn==4):
        mn= 'April'
    elif(dn==5):
        mn= 'May'
    elif(dn==6):
        mn= 'June'
    elif(dn==7):
        mn= 'July'
    elif(dn==8):
        mn= 'August'
    elif(dn==9):
        mn= 'September'
    elif(dn==10):
        mn= 'october'
    elif(dn==11):
        mn= 'November'
    elif(dn==12):
        mn= 'December'
    else:
        mn= 'Invalid'
    return mn
for i in range(3):
    inp=int(input(
        ))
    print(printMonth(inp))

