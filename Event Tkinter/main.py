from tkinter import*
#create window
window=Tk()
window.title("Event Handler")
window.geometry("100x100")
#event handler for key pressing
def handle_keypress(event):
    #print the charcter 
    print(event.char)
#bind key press with event
window.bind("<Key>",handle_keypress)    
#Event handler for button clicking
def handle_click(event):
    print("\nThe button was click")
button=Button(text="Click me") 
button.pack()
#bind clicking event to handle_click
button.bind("<Button-1>",handle_click)
window.mainloop() 
