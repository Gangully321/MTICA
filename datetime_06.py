from tkinter import*
        
master=Tk()
demo_text="this is a sample demo of message widget."
msg=Message(master,text=demo_text)
msg.config(bg='lightgreen',font=('times',24,'italic'))
msg.pack()
