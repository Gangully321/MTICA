x=5;x=7
#Function definition is here
def changeme (mylist):
    "This function demostrates local and global variables"
    p=89
    global x,y
    x=y+2
    mylist=[1,2,3,4]#this would assign new reerence in mylist

    print("values inside the function:",mylist)
    print("local variables are:",local())
    print("global varables are:",globals())
    return
#now you can call changeme function
mylist_var =[10,20,30]
changeme(mylist_var)
print("variables outside the function:,mylist_var")
