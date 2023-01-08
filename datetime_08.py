from tkinter import *
master=Tk()

##Lable=(master,text="first Name").grid(row=0)
##Lable=(master,text="LastName").grid(row=1)

l1=Label(master,text="First Name")
l1.grid(row=0,column=0)

l2=Label(master,text="Last Name")
l2.grid(row=1,column=0)

e1=Entry(master)
e2=Entry(master)

e1.grid(row=0,column=1)
e2.grid(row=1,column=1)

mainloop()
