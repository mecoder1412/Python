from tkinter import*

#create window
root=Tk()
root.title=("Login App")
root.geometry("400x400")

#creating a frame
frame=Frame(master=root,height=200,width=360,bg="#d0efff")

#Add widgets
#Add Label
lbl1=Label(frame,text="Full Name",bg="#3895D3",fg="white",width=12)
lbl2=Label(frame,text="Email Id",bg="#3895D3",fg="white",width=12)
lbl3=Label(frame,text="Enter Password",bg="#3895D3",fg="white",width=12)

#Use entry widget
name_entry=Entry(frame)
email_entry=Entry(frame)
pass_entry=Entry(frame,show="*")

#Function to display message
def display():
 name=name_entry.get()
 greet="Hey"+name
 message="\nCongratulations for your new account!"
 textbox.insert(END, greet)
 textbox.insert(END, message)

#Textbox to display message
textbox=Text(bg="#BEBEBE",fg="black")

#add button when pressed message is displayed
btn=Button(text="Create account",command=display,bg="red")

#arrange all widgets
frame.place(x=20,y=0)
lbl1.place(x=20,y=20)
lbl2.place(x=20,y=80)
lbl3.place(x=20,y=140)
name_entry.place(x=150,y=20)
email_entry.place(x=150,y=80)
pass_entry.place(x=150,y=140)
btn.place(x=130,y=210)
textbox.place(x=0,y=250)

root.mainloop()