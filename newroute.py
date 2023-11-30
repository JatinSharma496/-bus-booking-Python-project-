from tkinter import *
import subprocess
import bus_booking_system
from tkinter import messagebox


root=Tk()
root.title("New route")
root.geometry('%dx%d+0+0'%(root.winfo_screenwidth(),root.winfo_screenheight()))


def add_route():
    
    routeid=id_entry.get()
    station=station_entry.get()
    station=station.capitalize()
    
    id_stat=id_stat_entry.get()
    route_data=(routeid,station,id_stat)
    route_data=(routeid,station,id_stat)
    data=(routeid,station)

    if not (routeid and station and id_stat):

        messagebox.showwarning("Warning","All entries should be filled.")
   
        return

    if not (station.isalpha()):
        messagebox.showwarning("Warning","Station Name should be Alphabetical")
        return

    existing_route=bus_booking_system.read_route()
    
    for i in existing_route:
        if data ==i[:2]:
            messagebox.showerror("Error","Route Details already exists")
            return 
    
    bus_booking_system.add_route(route_data)

    
    messagebox.showinfo("successful",'''Route added successfully : Thank you''')

    show_details=Label(frame3,text=f"{routeid}  {station}  {id_stat} ")
    show_details.grid(row=2,column=5)

    id_entry.delete(0,END)
    station_entry.delete(0,END)
    id_stat_entry.delete(0,END)

def delete_route():
    
    

    routeid=id_entry.get()
    station=station_entry.get()
    station=station.capitalize()
    id_stat=id_stat_entry.get()
    route_data=(routeid,station,id_stat)

    if not (routeid and station and id_stat):

        messagebox.showwarning("Warning","All entries should be filled.")
   
        return

    existing_route=bus_booking_system.read_route()
    check=None
    for i in existing_route:
        if route_data ==i:
           
           check=i
    if check==None:
        messagebox.showerror("Error","route details does not exist.")
        return
    
    bus_booking_system.delete_route(routeid,station)
     
    messagebox.showinfo("successful",'''Route deleted  successfully : Thank you''')

    show_details=Label(frame3,text=f"{routeid}  {station}  {id_stat} ")
    show_details.grid(row=2,column=5)

    id_entry.delete(0,END)
    station_entry.delete(0,END)
    id_stat_entry.delete(0,END)
    



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

head=Label(frame2,text="Add Bus Route Details",relief="ridge",fg="green",font=('Poppins',15,'bold'),padx=50)
head.grid(row=1,column=3,pady=50)

frame3=LabelFrame(root,borderwidth=0)
frame3.pack(padx=5,pady=5)

routeid=Label(frame3,text="Route Id :",font=('Poppins',10,'bold'))
routeid.grid(row=0,column=0)

id_entry=Entry(frame3,width=7)
id_entry.grid(row=0,column=1)



station=Label(frame3,text="Station Name:",font=('Poppins',10,'bold'))
station.grid(row=0,column=2)

station_entry=Entry(frame3,width=10)
station_entry.grid(row=0,column=3)


id_stat=Label(frame3,text="Station Id:",font=('Poppins',10,'bold'))
id_stat.grid(row=0,column=4)

id_stat_entry=Entry(frame3,width=5)
id_stat_entry.grid(row=0,column=5)




add_button=Button(frame3,text="Add Route",bg="light green",font=('Poppins',10,'bold'),command=add_route)
add_button.grid(row=1,column=5,padx=10,pady=20)

delete_button=Button(frame3,text="Delete Route",bg="light blue",fg="red",font=('Poppins',10,'bold'),command=delete_route)
delete_button.grid(row=1,column=6,padx=10,pady=20)
 

homelogo=PhotoImage(file="homelogo.png")

home_button=Button(frame3,image=homelogo,command=home)
home_button.grid(row=3,column=10,padx=10,pady=20)
root.mainloop()
