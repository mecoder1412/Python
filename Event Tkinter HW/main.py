from tkinter import*
from tkinter import messagebox
root=Tk()
root.title("length converter")
root.geometry("400x400")
frame=Frame(master=root,height=200,width=360,bg="#d0efff")
lbl1=Label(frame,text="enter number",bg="#3895D3",fg="white",width=12)
num=Entry(frame)

def handle_click(event=None):
    number=float(num.get())
    textbox.insert(END,str(number/30.48))
button1=Button(text="feet",bg="#3895D3",command=handle_click) 
button1.place(x=20,y=80)
def handle_click2(event=None):
    number1=float(num.get())
    textbox.insert(END,str(number1/100))
button2=Button(text="meters",bg="#3895D3",command=handle_click2) 
button2.place(x=150,y=80)
def clear(event=None):
    textbox.delete("1.0", END)
button3 = Button(text="Clear", bg="#3895D3", command=clear) 
button3.place(x=270, y=80)
textbox=Text(root,bg="#BEBEBE",fg="black")
frame.place(x=20,y=0)
lbl1.place(x=20,y=20)
num.place(x=150,y=20)
textbox.place(x=0,y=250)

root.mainloop()