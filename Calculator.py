from tkinter import*
import math
root=Tk()
root.title("Calculator")
e =Entry(root)
e.grid(row=0,column=0, columnspan=6)
e.focus_set()

def clearall():
    e.delete(0,END)
def clear1():
    txt=e.get()[:-1]
    e.delete(0,END)
    e.insert(0,txt)
def fund7():
    txt=e.get()
    txt=txt +'7'
    e.delete(0,END)
    e.insert(0,txt)
def fund8():
    txt=e.get()
    txt=txt +'8'
    e.delete(0,END)
    e.insert(0,txt)
def fund9():
    txt=e.get()
    txt=txt +'9'
    e.delete(0,END)
    e.insert(0,txt)
def fund4():
    txt=e.get()
    txt=txt +'4'
    e.delete(0,END)
    e.insert(0,txt)
def fund5():
    txt=e.get()
    txt=txt +'5'
    e.delete(0,END)
    e.insert(0,txt)
def fund6():
    txt=e.get()
    txt=txt +'6'
    e.delete(0,END)
    e.insert(0,txt)
def fund1():
    txt=e.get()
    txt=txt +'1'
    e.delete(0,END)
    e.insert(0,txt)
def fund2():
    txt=e.get()
    txt=txt +'2'
    e.delete(0,END)
    e.insert(0,txt)
def fund3():
    txt=e.get()
    txt=txt +'3'
    e.delete(0,END)
    e.insert(0,txt)
def fund0():
    txt=e.get()
    txt=txt +'0'
    e.delete(0,END)
    e.insert(0,txt)
def fundp():
    txt=e.get()
    txt=txt +'.'
    e.delete(0,END)
    e.insert(0,txt)
def fundadd():
    txt=e.get()
    txt=txt +'+'
    e.delete(0,END)
    e.insert(0,txt)
def fundmult():
    txt=e.get()
    txt=txt +'*'
    e.delete(0,END)
    e.insert(0,txt)
def fundsub():
    txt=e.get()
    txt=txt +'-'
    e.delete(0,END)
    e.insert(0,txt)
def funddiv():
    txt=e.get()
    txt=txt +'/'
    e.delete(0,END)
    e.insert(0,txt)
def fundpow():
    txt=e.get()
    txt=txt +'**'
    e.delete(0,END)
    e.insert(0,txt)
def fundparenthopen():
    txt=e.get()
    txt=txt +'('
    e.delete(0,END)
    e.insert(0,txt)
def fundparenthclose():
    txt=e.get()
    txt=txt +')'
    e.delete(0,END)
    e.insert(0,txt)
def answer():
    txt=e.get()
    e.delete(0,END)
    ans=eval(txt)
    e.insert(0,ans)
def squareroot():
    ans=math.sqrt(float(e.get()))
    e.insert(0,ans)
def percentage():
    txt=e.get()
    e.delete(0,END)
    ans=eval(txt)
    ans=ans/100
    e.insert(0,ans)
b1=Button(root,text="=",width=8,command=answer)
b1.grid(row=4, column=4,columnspan=2)
#b1.config(bg="lightgreen", font=("impact",24,"normal"))
b2=Button(root,text="ac",width=3,command=clearall,bg="lightslategray")
b2.grid(row=1, column=4)
b3=Button(root,text="c",width=3,command=clear1)
b3.grid(row=1, column=5)
b4=Button(root,text="+",width=3,command=fundadd)
b4.grid(row=4, column=3)
b5=Button(root,text="X",width=3,command=fundmult)
b5.grid(row=2, column=3)
b6=Button(root,text="-",width=3,command=fundsub)
b6.grid(row=3, column=3)
b7=Button(root,text="/",width=3,command=funddiv)
b7.grid(row=1, column=3)
b8=Button(root,text="%",width=3,command=percentage)
b8.grid(row=4, column=2)
b9=Button(root,text="7",width=3,command=fund7)
b9.grid(row=1, column=0)
b10=Button(root,text="8",width=3,command=fund8)
b10.grid(row=1, column=1)
b11=Button(root,text="9",width=3,command=fund9)
b11.grid(row=1, column=2)
b12=Button(root,text="4",width=3,command=fund4)
b12.grid(row=2, column=0)
b13=Button(root,text="5",width=3,command=fund5)
b13.grid(row=2, column=1)
b14=Button(root,text="6",width=3,command=fund6)
b14.grid(row=2, column=2)
b15=Button(root,text="1",width=3,command=fund1)
b15.grid(row=3, column=0)
b16=Button(root,text="2",width=3,command=fund2)
b16.grid(row=3, column=1)
b17=Button(root,text="3",width=3,command=fund3)
b17.grid(row=3, column=2)
b18=Button(root,text="0",width=3,command=fund0)
b18.grid(row=4, column=0)
b19=Button(root,text="." ,width=3,command=fundp)
b19.grid(row=4, column=1)
b20=Button(root,text="(",width=3,command=fundparenthopen)
b20.grid(row=2, column=4)
b21=Button(root,text=")",width=3,command=fundparenthclose)
b21.grid(row=2, column=5)
b22=Button(root,text="sqrt",width=3,command=squareroot)
b22.grid(row=3, column=4)
b23=Button(root,text="pow",width=3,command=fundpow)
b23.grid(row=3,column=5)
root.mainloop()
