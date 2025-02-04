from tkinter import*
window=Tk()
window.title=("age tracker")
window.geometry=('900x900')
frame=Frame(master=window,height=200,width=360,bg="#d0efff")
q=Label(frame,text="type your birth year",bg="#3895D3",fg="white",width=18)
A=Entry(frame)
def display():
    num1 =(A.get())
    num2 = 2024
    result = num2 - num1
    text=f"You are {result} years old"
textbox=Text(bg="#BEBEBE",fg="black")
btn=Button(text="See age",command=display,bg="red")    
frame.place(x=20,y=0)
q.place(x=20,y=20)
A.place(x=150,y=20)
btn.place(x=130,y=210)
textbox.place(x=0,y=250)
window.mainloop()