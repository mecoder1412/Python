from tkinter import*
from tkinter import messagebox
root=Tk()
root.geometry("200x200")
# Function for Displaying Warning Message
# This will be called once the button is clicked
# messagebox.showwarning("Window Name", "Text to be displayed")
def msg():
    messagebox.showwarning("Alert","Stop!Virus Found")
#adding button wiget to window
button=Button(root,text="scan for Virus",command=msg)
button.place(x=40,y=80)
root.mainloop()
