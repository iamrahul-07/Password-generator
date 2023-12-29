from tkinter import *
import random
import tkinter.messagebox as mm
import string

#CREATING MAIN WINDOW
root=Tk()
root.geometry("750x600")
root.resizable(False,False)
root.title("Random Password Generator")
a=StringVar()


#CREATING FUNCTION

def gen_pass():
    length=entry2.get()
    if len(length)<=0:
        a.set("")
        mm.showwarning("Warning","Enter length of password")
    length=int(length)
    password="".join(random.choice(string.ascii_letters+string.digits+string.punctuation)
                     for i in range(length))
    a.set(password)
        
def reset():
    a.set("")


#CREATING LABELS
label=Label(root,bg="lightblue",relief=SOLID,borderwidth=2)
label.place(x=0,y=0,height=600,width=750)

label1=Label(root,text="Password Generator",font=("algerian 30 underline"),padx=10,pady=10,bg="orange")
label1.place(x=190,y=30)

label2=Label(root,text="Enter user name : ",font=("liberation 20"))
label2.place(x=20,y=170)

label3=Label(root,text="Enter password length :",font=("liberation 20"))
label3.place(x=20,y=240)

label4=Label(root,text="Generated password :",font=("liberation 20"))
label4.place(x=20,y=310)


#CREATING ENTRY WIDGET

entry1=Entry(root,font=("liberation 20"),relief=SUNKEN,borderwidth=5)
entry1.place(x=400,y=170)

entry2=Entry(root,font=("liberation 20"),relief=SUNKEN,borderwidth=5)
entry2.place(x=400,y=240)

entry3=Entry(root,font=("liberation 20"),relief=SUNKEN,borderwidth=5,textvariable=a)
entry3.place(x=400,y=310)


#CREATING BUTTONS

button1=Button(root,text="Generate Password",font=("algerian 20"),bg="orange",activebackground="lightgrey",relief=RAISED,borderwidth=5,command=gen_pass)
button1.place(x=250,y=390)

button2=Button(root,text="Reset",font=("algerian 20"),bg="orange",activebackground="lightgrey",relief=RAISED,borderwidth=5,command=reset)
button2.place(x=350,y=470)

root.mainloop()