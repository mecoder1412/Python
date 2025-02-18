from tkinter import *
from tkinter import messagebox
import string

root = Tk()
root.title("Password Strength Checker")
root.geometry("400x400")

# Frame setup
frame = Frame(root, height=250, width=360, bg="#defff")
frame.pack(pady=20)

# Label and Entry field
lbl1 = Label(frame, text="Enter password", bg="#3895D3", fg="white", width=12)
lbl1.place(x=20, y=20)

pass_entry = Entry(frame, show="*")
pass_entry.place(x=150, y=20)

# Function to check password strength
def click():
    password = pass_entry.get()
    st = 0  # Reset strength score

    # Length check
    if len(password) > 7:
        st += 2  # Stronger for longer passwords

    # Character type checks
    if any(char.isdigit() for char in password):
        st += 2  # Contains a number

    if any(char.isalpha() for char in password):
        st += 2  # Contains letters

    if any(char.isupper() for char in password):
        st += 2  # Contains uppercase letters

    if any(char in string.punctuation for char in password):
        st += 2  # Contains special characters

    # Password strength message
    if st <= 4:
        messagebox.showwarning("Weak Password", "Your password is weak. Try adding numbers, uppercase letters, and special characters.",fg="red")
    elif 4 < st < 8:
        messagebox.showinfo("Medium Password", "Your password is okay, but could be stronger.",fg="orange")
    else:
        messagebox.showinfo("Strong Password", "Your password is strong!",fg="green")

# Submit button
submit = Button(frame, text="Submit", bg="#3895D3", fg="white", width=12, command=click)
submit.place(x=130, y=70)

root.mainloop()



