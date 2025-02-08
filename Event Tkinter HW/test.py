from tkinter import *
from tkinter import messagebox

# Initialize the main window
root = Tk()
root.title("Length Converter")
root.geometry("400x400")

# Create a frame
frame = Frame(master=root, height=200, width=360, bg="#d0efff")
frame.place(x=20, y=0)

# Create label and input entry
lbl1 = Label(frame, text="Enter number", bg="#3895D3", fg="white", width=12)
lbl1.place(x=20, y=20)

num = Entry(frame)
num.place(x=150, y=20)

# Create output textbox
textbox = Text(root, bg="#BEBEBE", fg="black", height=5, width=40)
textbox.place(x=20, y=250)

# Function to convert to feet
def convert_to_feet(event):
    try:
        value = float(num.get())  # Get user input and convert to float
        result = value / 30.48  # Convert cm to feet
        textbox.insert(END, f"{value} cm = {result:.2f} feet\n")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

# Function to convert to meters
def convert_to_meters(event):
    try:
        value = float(num.get())  # Get user input and convert to float
        result = value / 100  # Convert cm to meters
        textbox.insert(END, f"{value} cm = {result:.2f} meters\n")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number")

# Create buttons
feet_button = Button(root, text="Feet", bg="#3895D3")
feet_button.place(x=20, y=80)
feet_button.bind("<Button-1>", convert_to_feet)

meters_button = Button(root, text="Meters", bg="#3895D3")
meters_button.place(x=150, y=80)
meters_button.bind("<Button-1>", convert_to_meters)

# Run the application
root.mainloop()
