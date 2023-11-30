from tkinter import *
from tkinter import messagebox

import subprocess
import bus_booking_system

root=Tk()
root.title("new operator")
root.geometry('%dx%d+0+0'%(root.winfo_screenwidth(),root.winfo_screenheight()))
from tkinter import messagebox

def add_op():
    op_id = id_entry.get()
    op_name = name_entry.get()
    op_address = address_entry.get()
    op_phone = phone.get()
    op_email = email_entry.get()

    if not (op_address and op_id and op_email and op_phone and op_name):
        messagebox.showwarning("Warning", "All entries should be filled.")
        return

    existing_operators = bus_booking_system.read_operators()
    
    if any(operator[0] == op_id for operator in existing_operators):
        messagebox.showerror("Error", f"Operator with ID {op_id} already exists.")
        return
    
    

    if len(op_phone) != 10 or op_phone.isalpha():
        messagebox.showerror("Error", "Mobile No. should be of ten digits Integer")
        return

    operator_data = (op_id, op_name, op_address, op_phone, op_email)

    bus_booking_system.add_operator(operator_data)

    messagebox.showinfo("Successful", "Operator added successfully: Thank you")

    show_details = Label(frame4, text=f"{op_id}  {op_name}  {op_address}  {op_phone}  {op_email}")
    show_details.grid(row=2, column=5)


    id_entry.delete(0,END)
    name_entry.delete(0,END)
    address_entry.delete(0,END)
    phone.delete(0,END)
    email_entry.delete(0,END)






def edit_op():
    op_id_edit=id_entry.get()
    op_name=name_entry.get()
    op_address=address_entry.get()
    op_phone=phone.get()
    op_email=email_entry.get()

    existing_operators=bus_booking_system.read_operators()
    operator_edit=None
    
    for op in existing_operators:
        if op[0]==op_id_edit:
            operator_edit=op
            break

    if operator_edit is None:
        messagebox.showerror("Error",f" Operator with Id { op_id_edit} not found.")
        return 

    if not (op_address and op_id_edit and op_email and op_phone and op_name):
        messagebox.showwarning("Warning","All entries should be filled.")
        return
    
    
    if len(op_phone) != 10 or op_phone.isalpha():
        messagebox.showerror("Error", "Mobile No. should be of ten digits Integer")
        return

    

    response=messagebox.askyesno("message","Are you Sure You want to edit ?")

    if response==1:
        operator_data=(op_id_edit,op_name,op_address,op_phone,op_email)
        bus_booking_system.edit_operator(op_id_edit,operator_data)
        messagebox.showinfo("successful",'''Operator Edited successfully : Thank you''')

    else:

        return 
    
   

    show_details=Label(frame4,text=f"{op_id_edit}  {op_name}  {op_address}  {op_phone}  {op_email}")
    show_details.grid(row=2,column=5)

    id_entry.delete(0,END)
    name_entry.delete(0,END)
    address_entry.delete(0,END)
    phone.delete(0,END)
    email_entry.delete(0,END)
 


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

head=Label(frame2,text="Add Bus Operator Details",relief="ridge",fg="green",font=('Poppins',15,'bold'),padx=50)
head.grid(row=1,column=3,pady=50)

frame3=LabelFrame(root,borderwidth=0)
frame3.pack(padx=5,pady=5)

frame4=LabelFrame(root,borderwidth=0)
frame4.pack(padx=5,pady=5)

opid=Label(frame3,text="Operator id :",font=('Poppins',10,'bold'))
opid.grid(row=0,column=0)

id_entry=Entry(frame3)
id_entry.grid(row=0,column=1)


name=Label(frame3,text="Name:",font=('Poppins',10,'bold'),padx=5)
name.grid(row=0,column=2,padx=5)

name_entry=Entry(frame3)
name_entry.grid(row=0,column=3)


address=Label(frame3,text="Address:",font=('Poppins',10,'bold'),padx=5)
address.grid(row=0,column=4,padx=5)

address_entry=Entry(frame3)
address_entry.grid(row=0,column=5)


phn=Label(frame3,text="Phone No. :",font=('Poppins',10,'bold'),padx=5)
phn.grid(row=0,column=6,padx=5)

phone=Entry(frame3)
phone.grid(row=0,column=7)


email=Label(frame3,text="Email:",font=('Poppins',10,'bold'),padx=5)
email.grid(row=0,column=8,padx=5)

email_entry=Entry(frame3)
email_entry.grid(row=0,column=9)

add_button=Button(frame3,text="Add",command=add_op,bg="light green",font=('Poppins',10,'bold'))
add_button.grid(row=0,column=10,padx=10)

edit_button=Button(frame3,text="Edit",command=edit_op,bg="red",font=('Poppins',10,'bold'))
edit_button.grid(row=0,column=11,padx=10)


homelogo=PhotoImage(file="homelogo.png")

home_button=Button(frame3,image=homelogo,command=home)
home_button.grid(row=3,column=5,padx=10,pady=20)
root.mainloop()
