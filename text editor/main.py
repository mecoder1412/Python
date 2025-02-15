from tkinter import*
from tkinter.filedialog import askopenfilename,asksaveasfilename

#window set up
window=Tk()
window.title("Text editor")
window.geometry("600x600")
window.rowconfigure(0,minsize=800,weight=1)
window.columnconfigure(1,minsize=800,weight=1)

def open_file():
    #Open a file for editing
  filepath=askopenfilename(filetypes=[("Text files","*.txt"),("All files","*.*")]) 
  if not filepath:
    return
  txt_edit.delete(1.0,END) 

   #opening file
  with open(filepath,"r") as input_file:
    #Read contents of file
    text=input_file.read()
    txt_edit.insert(END,text)
    input_file.close()
    window.title(f"Codingal text editor-{filepath}")
      
def save_file():
    #Open a file for editing
  filepath=asksaveasfilename(defaultextension=".txt",filetypes=[("Text files","*.txt"),("All files","*.*")]) 
  if not filepath:
    return
   #opening file
  with open(filepath,"w") as output_file:
    #write contents of file
    text=txt_edit.get(1.0,END)
    output_file.write(text)
    output_file.close()
    window.title(f"Codingal text editor-{filepath}") 

txt_edit = Text(window)

fr_buttons = Frame(window, relief=RAISED, bd=2)

btn_open = Button(fr_buttons, text="Open", command=open_file)

btn_save = Button(fr_buttons, text="Save As...", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)

btn_save.grid(row=1, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")

txt_edit.grid(row=0, column=1, sticky="nsew")

window.mainloop()   