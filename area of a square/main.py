from tkinter import*
from tkinter import messagebox
root=Tk()
root.title("area convater")
root.geometry("400x400")
frame=Frame(master=root,height=200,width=360,bg="#d0efff")
lbl1=Label(frame,text="enter length/radious",bg="#3895D3",fg="white",width=15)
num=Entry(frame)
def handle_click(event=None):
    number=float(num.get())
    textbox.insert(END,str(number*number))
button1 = Button(text="Area of Square", bg="#3895D3", command=handle_click) 
button1.place(x=20,y=80)
def handle_click2(event=None):
    number1=float(num.get())
    textbox.insert(END,str(number1*3.14*2))
button2 = Button(text="Circumference", bg="#3895D3", command=handle_click2)
button2.place(x=150,y=80)
def clear(event=None):
    textbox.delete("1.0", END)
button3 = Button(text="Clear", bg="#3895D3", command=clear) 
button3.place(x=270, y=80)
textbox=Text(root,bg="#BEBEBE",fg="black")
textbox.place(x=0,y=250)
frame.place(x=20,y=0)
lbl1.place(x=20,y=20)
num.place(x=150,y=20)
root.mainloop()