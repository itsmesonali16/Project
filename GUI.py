from tkinter import*
master=Tk()
Label(master,text="Client").grid(row=0)
Label(master,text="Enter Messsage").grid(row=1)
e1=Entry(master)
e2=Entry(master)
e2.grid(row=1,column=1)
mainloop()
