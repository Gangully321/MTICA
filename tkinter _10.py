from tkinter import *
master=Tk()

l1=Label(master,text="First Number")
l1.grid(row=0,column=0)
l2=Label(master,text="Last Number")
l2.grid(row=1,column=0)
e1=Entry(master)
e2=Entry(master)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)

def show_entry_fields():
    print("First Number:",e1.get())
    print("Last Number:",e2.get())

def add():
    temp=int(e1.get())+int(e2.get())
    print(e1.get(),'+',e2.get(),'=',temp)

b1=Button(master,text='quit',command=master.quit)
b1.grid(row=3,column=0)

b2=Button(master,text='+',command=add)
b2.grid(row=3,column=1)


mainloop()
