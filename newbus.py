from tkinter import *
import subprocess
import bus_booking_system
from tkinter import messagebox


root=Tk()
root.title("New Bus")

root.geometry('%dx%d+0+0'%(root.winfo_screenwidth(),root.winfo_screenheight()))

label_text = "221B467(Jatin Sharma)"
label = Label(root, text=label_text)
label.pack(side=TOP, anchor=E, padx=10, pady=10)

def add_bus():
    busid=id_entry.get()
    Bustype=click.get()
    capacity=capacity_entry.get()
    fare=fare_entry.get()
    opid=opid_entry.get()
    routeid=routeid_entry.get()

    existing_bus=bus_booking_system.read_bus()
    
    for i in existing_bus:
        if busid ==i[0]:
            messagebox.showerror("Error"," Bus_id  already exists")
            return 


    if not (busid and Bustype and capacity and fare and opid and routeid ):
        messagebox.showwarning("Warning","All entries should be filled.")
        return
    
    if(Bustype=="Bus Type"):
         messagebox.showwarning("Warning","Bus Type should be selected .")
         return

    
    if capacity.isalpha():
         messagebox.showwarning("Warning","Capacity  should be Integer.")
         return

    if int(capacity)<=10 :
         messagebox.showwarning("Warning","Capacity should be greater than 10.")
         return

    if int(capacity)>=60 :
         messagebox.showwarning("Warning","Capacity should be less than 60.")
         return
    
    if fare.isalpha():
         messagebox.showwarning("Warning","fare  should be Integer.")
         return

    if int(fare)<=0 :
         messagebox.showwarning("Warning","fare should be positive integer ")
         return
    
    bus_data=(busid,Bustype,capacity,fare,opid,routeid)
    if bus_booking_system.add_bus(bus_data)==None:
        return
    else:

        bus_booking_system.add_bus(bus_data)
    
        messagebox.showinfo("successful",'''Bus added successfully : Thank you''')

   
        show_details=Label(frame3,text=f"{busid}  {Bustype}  {capacity}  {fare}  {opid}  {routeid}")
        show_details.grid(row=2,column=5)

        id_entry.delete(0,END)
        click.set("Bus Type")
        capacity_entry.delete(0,END)
        fare_entry.delete(0,END)
        opid_entry.delete(0,END)
        routeid_entry.delete(0,END)



def edit_bus():
    busid=id_entry.get()
    Bustype=click.get()
    capacity=capacity_entry.get()
    fare=fare_entry.get()
    opid=opid_entry.get()
    routeid=routeid_entry.get()

    existing_bus=bus_booking_system.read_bus()
    bus_edit=None
    
    for bus in existing_bus:
        if bus[0]==busid:
            bus_edit=bus
            break

    if bus_edit is None:
        messagebox.showerror("Error",f" Bus with Id {busid} not found.")
        return 

    if not (busid and Bustype and capacity and fare and opid and routeid ):
        messagebox.showwarning("Warning","All entries should be filled.")
        return

    
    if(Bustype=="Bus Type"):
         messagebox.showwarning("Warning","Bus Type should be selected .")
         return

    
    if capacity.isalpha():
         messagebox.showwarning("Warning","Capacity  should be Integer.")
         return

    if int(capacity)<10 :
         messagebox.showwarning("Warning","Capacity should be greater than 10.")
         return

    if int(capacity)>60 :
         messagebox.showwarning("Warning","Capacity should be less than 60.")
         return
    
    if fare.isalpha():
         messagebox.showwarning("Warning","fare  should be Integer.")
         return

    if int(fare)<0 :
         messagebox.showwarning("Warning","fare should be positive integer ")
         return
    
    

    response=messagebox.askyesno("message","Are you Sure You want to edit ?")

    if response==1:
            bus_data=(busid,Bustype,capacity,fare,opid,routeid)
  
            bus_booking_system.edit_bus(busid,bus_data)

        
            messagebox.showinfo("successful",'''Bus Edited successfully : Thank you''')
            show_details=Label(frame3,text=f"{busid}  {Bustype}  {capacity}  {fare}  {opid}  {routeid}")
            show_details.grid(row=2,column=5)

            id_entry.delete(0,END)
            click.set("Bus Type")
            capacity_entry.delete(0,END)
            fare_entry.delete(0,END)
            opid_entry.delete(0,END)
            routeid_entry.delete(0,END)

    else:
        return 
    

    


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

head=Label(frame2,text="Add Bus Details",relief="ridge",fg="green",font=('Poppins',15,'bold'),padx=50)
head.grid(row=1,column=3,pady=50)

frame3=LabelFrame(root,borderwidth=0)
frame3.pack(padx=5,pady=5)

busid=Label(frame3,text="Bus Id :",font=('Poppins',10,'bold'))
busid.grid(row=0,column=0)

id_entry=Entry(frame3,width=7)
id_entry.grid(row=0,column=1)


Bustype=Label(frame3,text="Bus Type :",font=('Poppins',10,'bold'),padx=5)
Bustype.grid(row=0,column=2,padx=5)

# bus typesss
busoptions=["AC 2X2","AC 3X2","NON AC 2X2","NON AC 3X2","AC-Sleeper 2X1","NON AC-Sleeper 2X1"]

click=StringVar()
click.set("Bus Type")
option=OptionMenu(frame3,click,*busoptions)
option.grid(row=0,column=3,padx=5)


capacity=Label(frame3,text="Capacity:",font=('Poppins',10,'bold'))
capacity.grid(row=0,column=4)

capacity_entry=Entry(frame3,width=5)
capacity_entry.grid(row=0,column=5)


fare=Label(frame3,text="Fare(₹)",font=('Poppins',10,'bold'))
fare.grid(row=0,column=6)

fare_entry=Entry(frame3,width=5)
fare_entry.grid(row=0,column=7)


opid=Label(frame3,text="Operator Id:",font=('Poppins',10,'bold'))
opid.grid(row=0,column=8)

opid_entry=Entry(frame3,width=7)
opid_entry.grid(row=0,column=9)

routeid=Label(frame3,text="Route Id:",font=('Poppins',10,'bold'))
routeid.grid(row=0,column=10)

routeid_entry=Entry(frame3,width=7)
routeid_entry.grid(row=0,column=11)


add_button=Button(frame3,text="Add Bus",bg="light green",font=('Poppins',10,'bold'),command=add_bus)
add_button.grid(row=1,column=5,padx=10,pady=20)

edit_button=Button(frame3,text="Edit Bus",bg="red",font=('Poppins',10,'bold'),command=edit_bus)
edit_button.grid(row=1,column=6,padx=10,pady=20)
 

homelogo=PhotoImage(file="homelogo.png")

home_button=Button(frame3,image=homelogo,command=home)
home_button.grid(row=3,column=10,padx=10,pady=20)
root.mainloop()
