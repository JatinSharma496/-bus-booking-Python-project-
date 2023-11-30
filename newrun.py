from tkinter import *
import subprocess
import bus_booking_system
from tkinter import messagebox
from datetime import datetime


root=Tk()
root.title("New run")

root.geometry('%dx%d+0+0'%(root.winfo_screenwidth(),root.winfo_screenheight()))



def add_newrun():
    busid = id_entry.get()
    rundate = date_entry.get()
    seat = seat_entry.get()



    existing_bus=bus_booking_system.read_bus()
    busid_edit=None
    for i in existing_bus:
        if busid ==i[0]:
            busid_edit=busid
            break
    if busid_edit==None:
        messagebox.showerror("Warning", "bus id does not exist .")
        return


    if not (busid and rundate and seat):
        messagebox.showwarning("Warning", "All entries should be filled.")
        return

    try:
        # Validate run date format
        datetime.strptime(rundate, "%d/%m/%Y")
    except ValueError:
        messagebox.showerror("Error", "Invalid date format. Please use dd/mm/yyyy.")
        return

    if seat.isalpha() and int(seat) <0:
        messagebox.showwarning("Warning", "seat should be  positive Integer")
        return

    capacity=bus_booking_system.show_cap(busid)
    
    if int(seat) > int(capacity[0]):
        messagebox.showwarning("Warning", "seat availbilty cannot be greater than capacity of bus")
        return
  

    
    

    

    newrun_data = (busid, rundate, seat)
    bus_booking_system.add_newrun(newrun_data)

    messagebox.showinfo("Successful", "Route added successfully. Thank you.")

    show_details = Label(frame3, text=f"{busid}  {rundate}  {seat}")
    show_details.grid(row=2, column=5)
    id_entry.delete(0, END)
    date_entry.delete(0, END)
    seat_entry.delete(0, END)


def delete_newrun():
    
    busid=(id_entry.get())
    rundate = date_entry.get()
    seat = seat_entry.get()

    
    newrun_data = (busid, rundate, seat)
    existing_bus=bus_booking_system.read_bus()
    busid_edit=None
    for i in existing_bus:
        if busid ==i[0]:
            busid_edit=busid
            break
    if busid_edit==None:
        messagebox.showerror("Warning", "bus id does not exist .")
        return

    if not (busid and rundate and seat):
        messagebox.showwarning("Warning", "All entries should be filled.")
        return

    try:
        # Validate run date format
        datetime.strptime(rundate, "%d/%m/%Y")
    except ValueError:
        messagebox.showerror("Error", "Invalid date format. Please use dd/mm/yyyy.")
        return

    if seat.isalpha() and int(seat) <0:
        messagebox.showwarning("Warning", "seat should be  positive Integer")
        return


    capacity=bus_booking_system.show_cap(busid)
    
    if int(seat) > int(capacity[0]):
        messagebox.showwarning("Warning", "seat availbilty cannot be greater than capacity of bus")
        return
     
    existing_run=bus_booking_system.read_newrun()
    edit=None
    for i in existing_run:
        if newrun_data ==i[0]:
            edit=i[0]
            break
    if busid_edit==None:
        messagebox.showerror("Error", "record not found.")
        return
    
    bus_booking_system.delete_newrun(busid,rundate)

    messagebox.showinfo("successful",'''Run deleted successfully : Thank you''')

    show_details = Label(frame3, text=f"{busid}  {rundate}  {seat}")
    show_details.grid(row=2, column=5)
    id_entry.delete(0, END)
    date_entry.delete(0, END)
    seat_entry.delete(0, END)






def home():
    subprocess.run(["python","homepage.py"])
    root.destroy()

frame=LabelFrame(root,padx=5,borderwidth=0)
frame.pack(padx=5)
image = PhotoImage(file="bus.png")
Label(frame,image=image).pack()


frame2=LabelFrame(root,padx=5,pady=5,borderwidth=0)
frame2.pack(padx=5,pady=5)

title_project= Label(frame2,text="Online Bus Booking System",relief="ridge",bg="light blue",fg="red",font=('Poppins',25,'bold'),padx=50)
title_project.grid(row=0,column=3,pady=10)

head=Label(frame2,text="Add Bus Running Details",relief="ridge",fg="green",font=('Poppins',15,'bold'),padx=50)
head.grid(row=1,column=3,pady=50)

frame3=LabelFrame(root,borderwidth=0)
frame3.pack(padx=5,pady=5)

busid=Label(frame3,text="Bus Id :",font=('Poppins',10,'bold'))
busid.grid(row=0,column=0)

id_entry=Entry(frame3,width=7)
id_entry.grid(row=0,column=1)



rundate=Label(frame3,text="Running Date(dd/mm/yyyy) :",font=('Poppins',10,'bold'))
rundate.grid(row=0,column=2)

date_entry=Entry(frame3,width=10)
date_entry.grid(row=0,column=3)


seat=Label(frame3,text="Seat Available :",font=('Poppins',10,'bold'))
seat.grid(row=0,column=4)

seat_entry=Entry(frame3,width=5)
seat_entry.grid(row=0,column=5)




add_button=Button(frame3,text="Add Run",bg="light green",font=('Poppins',10,'bold'),command=add_newrun)
add_button.grid(row=1,column=5,padx=10,pady=20)

delete_button=Button(frame3,text="Delete Run",bg="light blue",fg="red",font=('Poppins',10,'bold'),command=delete_newrun)
delete_button.grid(row=1,column=6,padx=10,pady=20)
 

homelogo=PhotoImage(file="homelogo.png")

home_button=Button(frame3,image=homelogo,command=home)
home_button.grid(row=3,column=10,padx=10,pady=20)


root.mainloop()
