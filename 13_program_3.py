def blue():
    print('choose blue!\n')
    return
def green():
    print('choose green!\n')
def white():
    print('choose white!\n')
def yellow():
    print('choose yellow!\n')
def choose():
    print("0:blue")
    print("1:green")
    print("2:white")
    print("3:yellow")
    print("4:Quit")
    return
ColorSelect={0:'blue',1:'green',2:'white',3:'yellow'}
selection=0
while True:
    if selection==4:break
    choose()
    selection=int(input("select a color option:"))
    if (selection>=0) and (selection<4):
        ColorSelect[selection]()
        
