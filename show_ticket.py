from tkinter import *
import subprocess
import bus_booking_system
from tkinter import messagebox



root=Tk()
root.title("Show_Ticket")
root.geometry('%dx%d+0+0'%(root.winfo_screenwidth(),root.winfo_screenheight()))

def on_close():
    result = messagebox.askyesnocancel("Confirmation", '''TO Close : Click YES

                                                    TO' Go to HOME: Click No''')
   
   
    if result ==True :
        messagebox.showinfo("thank you","thank you")
        root.destroy()
    elif result==False:
        subprocess.run(["python","homepage.py"])
        root.destroy()
    else:
        return

label_text = "221B467(Jatin Sharma)"
label = Label(root, text=label_text)
label.pack(side=TOP, anchor=E, padx=10, pady=10)
        
frame=LabelFrame(root,padx=5,borderwidth=0)
frame.pack(padx=5)
image = PhotoImage(file="bus.png")
Label(frame,image=image).pack()


frame2=LabelFrame(root,padx=5,pady=5,borderwidth=0)
frame2.pack(padx=5,pady=5)

title_project= Label(frame2,text="Online Bus Booking System",relief="ridge",bg="light blue",fg="red",font=('Poppins',25,'bold'),padx=50)
title_project.grid(row=0,column=3,pady=10)

Label(frame2,text="Bus Ticket", bg="cyan3",font=('Poppins',15,'bold')).grid(row=1,column=3,pady=10)

frame3=LabelFrame(root,padx=5,pady=5,borderwidth=5,relief="sunken")
frame3.pack(padx=5,pady=5)

pass_detail=bus_booking_system.read_booking()
details=pass_detail[-1]

Label(frame3,text=f'passenger:  {details[5]}',font=('Poppins',10,'bold')).grid(row=0,column=0,padx=2,pady=2)
Label(frame3,text=f'Gender:  {details[6]}',font=('Poppins',10,'bold')).grid(row=0,column=1,padx=2,pady=2)
Label(frame3,text=f'Total Seats :  {details[7]}',font=('Poppins',10,'bold')).grid(row=1,column=0,padx=2,pady=2)
Label(frame3,text=f'Phone No:  {details[8]}',font=('Poppins',10,'bold')).grid(row=1,column=1,padx=2,pady=2)
Label(frame3,text=f'Age:  {details[9]}',font=('Poppins',10,'bold')).grid(row=2,column=0,padx=2,pady=2)
Label(frame3,text=f'Booking Ref.:  {details[0]}',font=('Poppins',10,'bold')).grid(row=2,column=1,padx=2,pady=2)
Label(frame3,text=f'Traveling Date :  {details[4]}',font=('Poppins',10,'bold')).grid(row=3,column=0,padx=2,pady=2)
Label(frame3,text=f'Booked On:  {details[3]}',font=('Poppins',10,'bold')).grid(row=3,column=1,padx=2,pady=2)
Label(frame3,text=f'Boarding point :  {details[1]}',font=('Poppins',10,'bold')).grid(row=4,column=0,padx=2,pady=2)
Label(frame3,text=f'Dropping point :  {details[2]}',font=('Poppins',10,'bold')).grid(row=4,column=1,padx=2,pady=2)
bus_fare=bus_booking_system.show_bus_fare(details[10])

total_fare=(int(bus_fare[0])*int(details[7]))


Label(frame3,text=f'Total_Fare:  Rs {total_fare}',font=('Poppins',10,'bold'),fg="blue").grid(row=5,column=0,padx=2,pady=2)
bus_name=bus_booking_system.show_operator(details[10])
Label(frame3,text=f"Bus Details:  {bus_name[0]}",font=('Poppins',10,'bold')).grid(row=5,column=1,padx=2,pady=2)
Label(frame3,text=f" ** Total amount of RS {total_fare}  to be paid at the time of boarding the bus ",font=('Times New Roman',8)).grid(row=6,column=0,padx=2,pady=2)


root.protocol("WM_DELETE_WINDOW", on_close)

root.mainloop()
