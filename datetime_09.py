from tkinter import *
master=Tk()

l1=Label(master,text="First Name")
l1.grid(row=0,column=0)
l2=Label(master,text="Last Name")
l2.grid(row=1,column=0)
e1=Entry(master)
e2=Entry(master)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)

def show_entry_fields():
    print("First Name:",e1.get())
    print("Last Name:",e2.get())

b1=Button(master,text='show',command=show_entry_fields)
b1.grid(row=3,column=0)

b2=Button(master,text='show',command=show_entry_fields)
b2.grid(row=3,column=1)


mainloop()
