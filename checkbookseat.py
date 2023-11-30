from tkinter import *
import subprocess
import bus_booking_system
from tkinter import messagebox


root=Tk()
root.title("checkbookedseat")

root.geometry('%dx%d+0+0'%(root.winfo_screenwidth(),root.winfo_screenheight()))


def homepage():
    subprocess.run(["python","homepage.py"])
    root.destroy()

label_text = "221B467(Jatin Sharma)"
label = Label(root, text=label_text)
label.pack(side=TOP, anchor=E, padx=10, pady=10)


def checkticket():
    mobile = mobile_no.get()

    if not mobile:
        messagebox.showwarning("Warning", "All entries should be filled.")
        return
    if (len(mobile) != 10) or not mobile.isdigit():
        messagebox.showerror("Error", "Mobile No. should be of ten digit Integer")
        return

    bookings = bus_booking_system.show_tickets_from_mobile(mobile)

    if not bookings:
        response = messagebox.askyesno("No Records Found", "Do you want to Book a Seat?")
        if response == 1:
            subprocess.run(["python", "bookbus.py"])
        return
    k=0
    l=0
    for i, booking in enumerate(bookings):
        new_frame = LabelFrame(frame3, padx=10, pady=10, borderwidth=3, relief="sunken")
        new_frame.grid(row=k,column=l,padx=10, pady=10)

        Label(new_frame, text=f'Passenger:  {booking[5]}', font=('Poppins', 10, 'bold')).grid(row=0, column=0, padx=2,
                                                                                                pady=2)
        Label(new_frame, text=f'Gender:  {booking[6]}', font=('Poppins', 10, 'bold')).grid(row=0, column=1, padx=2,
                                                                                             pady=2)
        Label(new_frame, text=f'Total Seats :  {booking[7]}', font=('Poppins', 10, 'bold')).grid(row=1, column=0, padx=2,
                                                                                                  pady=2)
        Label(new_frame, text=f'Phone No:  {booking[8]}', font=('Poppins', 10, 'bold')).grid(row=1, column=1, padx=2,
                                                                                              pady=2)
        Label(new_frame, text=f'Age:  {booking[9]}', font=('Poppins', 10, 'bold')).grid(row=2, column=0, padx=2,
                                                                                        pady=2)
        Label(new_frame, text=f'Booking Ref.:  {booking[0]}', font=('Poppins', 10, 'bold')).grid(row=2, column=1,
                                                                                                padx=2, pady=2)
        Label(new_frame, text=f'Traveling Date :  {booking[4]}', font=('Poppins', 10, 'bold')).grid(row=3, column=0,
                                                                                                    padx=2, pady=2)
        Label(new_frame, text=f'Booked On:  {booking[3]}', font=('Poppins', 10, 'bold')).grid(row=3, column=1, padx=2,
                                                                                            pady=2)
        Label(new_frame, text=f'Boarding point :  {booking[1]}', font=('Poppins', 10, 'bold')).grid(row=4, column=0,
                                                                                                    padx=2, pady=2)
        Label(new_frame, text=f'Dropping point :  {booking[2]}', font=('Poppins', 10, 'bold')).grid(row=4, column=1,
                                                                                                    padx=2, pady=2)
        bus_fare = bus_booking_system.show_bus_fare(booking[10])
        total_fare = int(bus_fare[0]) * int(booking[7])
        Label(new_frame, text=f'Total_Fare:  Rs {total_fare}', font=('Poppins', 10, 'bold'), fg="blue").grid(row=5,
                                                                                                             column=0,
                                                                                                             padx=2,
                                                                                                             pady=2)
        bus_name = bus_booking_system.show_operator(booking[10])
        Label(new_frame, text=f"Bus Details:  {bus_name[0]}", font=('Poppins', 10, 'bold')).grid(row=5, column=1,
                                                                                                  padx=2, pady=2)
        l+=1


frame=LabelFrame(root,borderwidth=0)
frame.pack()
image = PhotoImage(file="bus.png")
Label(frame,image=image).pack()


frame2=LabelFrame(root,padx=10,pady=10,borderwidth=0)
frame2.pack()
frame3=LabelFrame(root,padx=10,pady=10,borderwidth=3,relief="sunken")
frame3.pack()

title_project= Label(frame2,text="Online Bus Booking System",relief="ridge",bg="light blue",fg="red",font=('Poppins',25,'bold'),padx=50)
title_project.grid(row=0,column=3)

Label(frame2,text="Check Your Booking",bg="green",font=('Helvetica 15 bold')).grid(row=1,column=3)

Label(frame2,text="Enter Your Mobile No. :",font=('Helvetica 10 bold')).grid(row=2,column=2)

mobile_no=Entry(frame2)
mobile_no.grid(row=2,column=3)

Button(frame2,text="Check Booking",fg="green",font=('Helvetica 12 bold'),command=checkticket).grid(row=2,column=5)



home=PhotoImage(file="homelogo.png")
home_button=Button(frame2,image=home,command=homepage)
home_button.grid(row=3,column=5,pady=10)

root.mainloop()


