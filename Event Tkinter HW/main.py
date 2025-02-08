from tkinter import*
from tkinter import messagebox
root=Tk()
root.title("length converter")
root.geometry("400x400")
frame=Frame(master=root,height=200,width=360,bg="#d0efff")
lbl1=Label(frame,text="enter number",bg="#3895D3",fg="white",width=12)
num=int(Entry(frame))

def handle_click(event):
    textbox.insert(END,int(num/30.48))
button=Button(text="feet",bg="#3895D3") 
button.place(x=20,y=80)
button.bind("<Button-1>",handle_click)
def handle_click2(event):
    textbox.insert(END,float(num/100))
button=Button(text="meters",bg="#3895D3") 
button.place(x=150,y=80)
button.bind("<Button-2>",handle_click)

textbox=Text(bg="#BEBEBE",fg="black")
frame.place(x=20,y=0)
lbl1.place(x=20,y=20)
num.place(x=150,y=20)
textbox.place(x=0,y=250)

root.mainloop()