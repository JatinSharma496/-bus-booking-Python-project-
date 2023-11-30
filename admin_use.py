from tkinter import *
import subprocess


root=Tk()
root.geometry('%dx%d+0+0'%(root.winfo_screenwidth(),root.winfo_screenheight()))
def newop():
    subprocess.run(["python","newop.py"])
    root.destroy()


def newbus():
    subprocess.run(["python","newbus.py"])
    root.destroy()


def newroute():
    subprocess.run(["python","newroute.py"])
    root.destroy()


def newrun():
    subprocess.run(["python","newrun.py"])
    root.destroy()

root.title("checkbookedseat")

label_text = "221B467(Jatin Sharma)"
label = Label(root, text=label_text)
label.pack(side=TOP, anchor=E, padx=10, pady=10)


frame=LabelFrame(root,padx=10,pady=10,borderwidth=0)
frame.pack(padx=10)
image = PhotoImage(file="bus.png")
Label(frame,image=image).pack()


frame2=LabelFrame(root,padx=10,pady=10,borderwidth=0)
frame2.pack(padx=10)

title_project= Label(frame2,text="Online Bus Booking System",relief="ridge",bg="light blue",fg="red",font=('Poppins',25,'bold'),padx=50)
title_project.grid(row=0,column=3,pady=50)

frame3=LabelFrame(root,padx=10,pady=10,borderwidth=0)
frame3.pack(padx=10)

Label(frame2,text="Add New Details to Database",fg="green",font=('Helvetica 15 bold')).grid(row=1,column=3,pady=10)



Button(frame3,text="New Operator",bg="light green",relief="groove",font=('Helvetica 10 bold'),command=newop).grid(row=2,column=2,padx=20,pady=10)


Button(frame3,text="New Bus",bg="gold",font=('Helvetica 10 bold'),relief="sunken",command=newbus).grid(row=2,column=3,padx=20,pady=10)

Button(frame3,text="New Route",bg="khaki1",font=('Helvetica 10 bold'),relief="raised",command=newroute).grid(row=2,column=4,padx=20,pady=10)

Button(frame3,text="New Run",bg="cyan2",font=('Helvetica 10 bold'),relief="flat",command=newrun).grid(row=2,column=6,padx=20,pady=10)


root.mainloop()
