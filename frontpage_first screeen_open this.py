 


from tkinter import *


import subprocess

'''
In Tkinter, subprocess is a Python module that allows you to spawn
new processes, connect to their input/output/error pipes, and obtain
their return codes. It's not directly related to Tkinter itself but
can be used in conjunction with it to perform tasks that involve
running external programs or scripts.
'''

root=Tk()
root.title("fontpage")

root.geometry('%dx%d+0+0'%(root.winfo_screenwidth(),root.winfo_screenheight()))
#to goto homepage

def homepage(event):
    subprocess.run(["python","homepage.py"])

label_text = "221B467(Jatin Sharma)"
label = Label(root, text=label_text)
label.pack(side=TOP, anchor=W)
#bus_image
    
image = PhotoImage(file="bus.png")
Label(root,image=image).pack()
#title
title_project= Label(root,text="Online Bus Booking System",bg="light blue",fg="red",font=('Poppins',25,'bold'),padx=50)
title_project.pack()

#name of student
name_student= Label(root,text="Student Name : Jatin Sharma ",fg="blue",font=('Poppins',15),pady=30)
name_student.pack()
#enrollment no.
enroll= Label(root,text="Enrollment No. : 221B467 ",fg="blue",pady=30,font=('Poppins',15))
enroll.pack()



#mobile number
mobile= Label(root,text="Mobile No. : 7976661201 ",fg="blue",pady=30,font=('Poppins',15))
mobile.pack()

#teacher name
teacher= Label(root,text="Submitted To : Dr. Mahesh Kumar ",bg="light blue",fg="red",pady=10,font=('Poppins',15))
teacher.pack()

learn= Label(root,text="Project Based Learning",fg="red",font=('Poppins',10))
learn.pack()

learn= Label(root,text="Press Any Key to Continue ",font=('Poppins',10))
learn.pack(pady=20)
#bind with key so that after pressing any key it would redirect to homepage

root.bind("<Key>",homepage)

root.mainloop()
