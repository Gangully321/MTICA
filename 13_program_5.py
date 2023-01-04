def printAdd(a,b):
    return a+b
def printSub(a,b):
    return a-b
def printMult(a,b):
    return a*b
def printDiv(a,b):
    return a/b
def choice():
    print("+:Adition");
    print("-:Subraction");
    print("*:Multiplication");
    print("/:Division");
    print("q:Quit")
    return
colorSelect={"+":printAdd,"-":printSub,"*":printMult,"/":printDiv}
while True:
    choice()
    selection=input("select Operator")
    if selection=='q' or selection=='Q':break
    if ((selection=='+') or (selection=='-') or (selection=='*') or (selection=='/')):
        n1=int(input("enter no:"))
        n2=int(input("enter no:"))
        z=colorSelect[selection](n1,n2)
        print(n1,selection,n2,'=',z)
        
