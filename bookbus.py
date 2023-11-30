

from tkinter import *
import subprocess
import bus_booking_system
from tkinter import messagebox
from datetime import datetime
import random


root=Tk()
root.title("bookBus")
root.geometry('%dx%d+0+0'%(root.winfo_screenwidth(),root.winfo_screenheight()))


#givin current date (to display booking date on ticket)
current_date=datetime.now().strftime("%d/%m/%Y")

#generates random booking reference no. between 1 to 100
def generate_booking_reference():
    while True:
        reference_number = random.randint(1, 100)  # Adjust the range as needed
        existing_bookings=bus_booking_system.read_booking()
        booking_edit=None
        for op in existing_bookings:
            if op[0]==reference_number:
                booking_edit=op[0]
                break
        if reference_number != booking_edit:
            return reference_number

        
label_text = "221B467(Jatin Sharma)"
label = Label(root, text=label_text)
label.pack(side=TOP, anchor=E, padx=10, pady=10)


def book_bus():

    
    if(selected_bus.get()=="None"):

        
        messagebox.showerror("error","bus is not selected ")
        return
    else:
        print("jatin")


    Label(frame3, text="Fill Passenger details to book the Bus ticket", fg="red", relief="ridge", bg="cyan3",
          font=('poppins 15 bold')).grid(row=0, column=1, padx=10, pady=20, columnspan=10)

    #name of passenger
    Label(frame3, text="Full Name : ", font=('Helvetica 10 bold')).grid(row=1, column=0)
    global name_entry
    name_entry = Entry(frame3)
    name_entry.grid(row=1, column=1)

    #drop down menu of gender
    Label(frame3, text="Gender : ", font=('Helvetica 10 bold')).grid(row=1, column=2)
    gender_options = ["Male", "Female", "Other"]
    global click
    click = StringVar()
    click.set("Select")
    OptionMenu(frame3, click, *gender_options).grid(row=1, column=3)


    # total seats booked by passenger
    Label(frame3, text="Total Seats: ", font=('Helvetica 10 bold')).grid(row=1, column=4)
    global seat_entry
    seat_entry = Entry(frame3)
    seat_entry.grid(row=1, column=5)


    #Mobile number of passenger
    Label(frame3, text="Mobile no. : ", font=('Helvetica 10 bold')).grid(row=1, column=6)
    global mobile_entry
    mobile_entry = Entry(frame3)
    mobile_entry.grid(row=1, column=7)

    #age 
    Label(frame3, text="Age : ", font=('Helvetica 10 bold')).grid(row=1, column=8)
    global age_entry
    age_entry = Entry(frame3)
    age_entry.grid(row=1, column=9, padx=10)


    Button(frame3, text="Book Seat", fg="red", bg="cyan3", font=('Helvetica 10 bold'),command=passenger_data).grid(row=10, column=10)



def passenger_data():
    #extracting all passenger data
    name = name_entry.get()
    gender = click.get()
    global total_seat
    total_seat = seat_entry.get()
    mobile_no = mobile_entry.get()
    age = age_entry.get()
    bus_id = selected_bus.get()
    
    
    if (not ( total_seat and mobile_no and age)):
            messagebox.showwarning("Warning", "All entries should be filled.")
            return
    if(name.isdigit()):
        messagebox.showwarning("Warning", " Name should  be Alphabatical .")
        return
        
    if(click.get()=="Select"):
        messagebox.showwarning("Warning", " Gender Should Be Selected .")
        return
        
    #check if mobile no is integer and of 10 digits
    if not ((len(mobile_no)==10)and mobile_no.isdigit()) :
                messagebox.showerror("Error","Mobile No. should be Ten digit Integer. ")
                return
    if  (age.isalpha()) :
        messagebox.showerror("error"," Age Should be Integer ")
        return
            
    if int(age)>110 :
        messagebox.showerror("error"," Age Should be less than 110")
        return

    if int(age)<18 :
        messagebox.showerror("error"," Age Should be aleast 18")
        return
    
    if not(total_seat.isdigit()) :
        messagebox.showerror("error"," seat should be Integer")
        return 
    if(int(total_seat)>7) :
        messagebox.showerror("error"," max seat 6 seat can be booked")
        return
    if(int(total_seat)<=0) :
        messagebox.showerror("error"," min seat 1 seat can be booked")
        return
        

    
    bus_fare=bus_booking_system.show_fare(bus_id)            
    total_fare=(int(total_seat)*int(bus_fare[0]))

   

    data=generate_booking_reference(), start_station, end_station, current_date, Journey_date,name, gender, total_seat, mobile_no, age, bus_id

    response=messagebox.askyesno("Seat Confirm",f'''Total amount to be paid is {total_fare}
                                                     Do you want to Book? ''')
    if response==1:
            messagebox.showinfo("congrats", "your bus booked successfully")
            #booking details added to database(booking_details table)
            bus_booking_system.add_booking_details(data)
            #bus seat availabilty of bus should be updated
            bus_booking_system.edit_avail(bus_id,total_seat,Journey_date)
            root.destroy()
            subprocess.run(["python", "show_ticket.py"])
                        
    else:

        return
                 

   
   

def show_bus():

    global start_station
    global end_station
    global Journey_date

    start_station=start.get()
    end_station=finish.get()
    Journey_date=date.get()
    

    if not (start_station and end_station and Journey_date ):
        messagebox.showwarning("Warning","All entries should be filled.")
        return
    try:
        # Validate run date format
        datetime.strptime(Journey_date, "%d/%m/%Y")
    except ValueError:
        messagebox.showerror("Error", "Invalid date format. Please use dd/mm/yyyy.")
        return
    

    if start_station.isalpha() and end_station.isalpha():
        #if journey date in not empty
        if not Journey_date=="":
            #first letter capital

            start_station=start_station.capitalize()
            end_station=end_station.capitalize()
            # finding route id that is matching with above data
            route = bus_booking_system.show_route(start_station,end_station)

            #if no route is found
            if len(route)==0:
                messagebox.showerror("No route found","No route found")
                return
            else:
                #finding bus ids of that route id

                buses=bus_booking_system.show_bus(route[0])
                
                #if there is no buses available to that route
            if(len(buses)==0):
                messagebox.showerror("No Bus found","No Bus found")
                return

            else:
                #all the buses that are running in the journey date
                buses_running=[]
                for i in buses:
                    if(i in bus_booking_system.show_run(i[0],Journey_date)):
                        buses_running.append(i[0])
                if(len(buses_running)==0):
                        messagebox.showerror("NOT RUNNING",f'BUS is not running at {Journey_date} , Change Date ')
                        return
    
    Label(frame2,text="Select Bus",fg="green",font=('Helvetica 10 bold')).grid(row=4,column=1,padx=10)
    
    Label(frame2,text="Operator",fg="green",font=('Helvetica 10 bold')).grid(row=4,column=2,padx=10)
    
    Label(frame2,text="Bus Type",fg="green",font=('Helvetica 10 bold')).grid(row=4,column=3,padx=10)

    Label(frame2,text="Available/Capacity",fg="green",font=('Helvetica 10 bold')).grid(row=4,column=4,padx=10)

    Label(frame2,text="Fare",fg="green",font=('Helvetica 10 bold')).grid(row=4,column=5,padx=10)
    

    display_buses(buses_running)
    
    start.delete(0,END)
    finish.delete(0,END)
    date.delete(0,END)
    


selected_bus = StringVar()
selected_bus.set("None")
def display_buses(buses_running):
    k = 6
    l = 1

    def on_radio_click(bus_id):
        selected_bus.set(bus_id)
        

    for i in range(len(buses_running)):
        bus_id = buses_running[i]  # Assuming buses_running contains unique bus identifiers
        Radiobutton(frame2, text=f'Bus {i + 1}', bg="light blue", font=('Helvetica 10 bold'),
                    relief="ridge", variable=selected_bus, value=bus_id, command=lambda bus_id=bus_id: on_radio_click(bus_id)).grid(row=k,column=l,pady=10,padx=10)
        operator_name = bus_booking_system.show_operator(bus_id)
        l = l + 1
        Label(frame2, text=operator_name[0], fg="blue", font=('Helvetica 10 bold')).grid(row=k, column=l, padx=10)
        bus_type = bus_booking_system.show_bus_type(bus_id)
        l = l + 1
        Label(frame2, text=bus_type[0], fg="blue", font=('Helvetica 10 bold')).grid(row=k, column=l, padx=10)
        available = bus_booking_system.show_avail(bus_id,Journey_date)
        cap = bus_booking_system.show_cap(bus_id)
        l = l + 1
        Label(frame2, text=f'{available}/{cap[0]}', fg="blue", font=('Helvetica 10 bold')).grid(row=k, column=l,
                                                                                                       padx=10)
        l = l + 1
        fare = bus_booking_system.show_fare(bus_id)
        Label(frame2, text=fare[0], fg="blue", font=('Helvetica 10 bold')).grid(row=k, column=l, padx=10)
        k = k + 1
        l = 1
    

    Button(frame2, text="Proceed to Book", bg="red", font=('Helvetica 10 bold'), command=book_bus).grid(row=k-1, column=7)


def homepage():
    subprocess.run(["python","homepage.py"])




frame=LabelFrame(root,borderwidth=0)
frame.pack()
image = PhotoImage(file="bus.png")
Label(frame,image=image).pack()



frame2=LabelFrame(root,borderwidth=0)
frame2.pack()

frame3=LabelFrame(root,borderwidth=0)
frame3.pack()


title_project= Label(frame2,text="Online Bus Booking System",relief="ridge",bg="light blue",fg="red",font=('Helvetica 18 bold'))
title_project.grid(row=0,column=0,pady=20,columnspan=20)


Label(frame2,text="Enter Journey Details",bg="green",font=('Helvetica 15')).grid(row=1,column=0,pady=20,columnspan=20)

Label(frame2,text="From:",font=('Helvetica 10 bold')).grid(row=3,column=0)

start=Entry(frame2)
start.grid(row=3,column=1)
Label(frame2,text="To:",font=('Helvetica 10 bold')).grid(row=3,column=2,padx=10)
finish=Entry(frame2)
finish.grid(row=3,column=3)

Label(frame2,text='''Journey Date:(DD/MM/YYYY)''',font=('Helvetica 10 bold')).grid(row=3,column=4,padx=10)
date=Entry(frame2)
date.grid(row=3,column=5)
#show bus button
Button(frame2,text="Show Bus",bg="green",font=('Helvetica 10 bold'),command=show_bus).grid(row=3,column=6,padx=10)
# home button


home=PhotoImage(file="homelogo.png")
home_button=Button(frame2,image=home,command=homepage)
home_button.grid(row=3,column=7)


root.mainloop()
