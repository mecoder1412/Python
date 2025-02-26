import tkinter as tk
import random

def play(user_choice):
    choices = ['Rock', 'Paper', 'Scissors']
    computer_choice = random.choice(choices)
    
    result = ""
    if user_choice == computer_choice:
        result = "It's a tie!"
    elif (user_choice == 'Rock' and computer_choice == 'Scissors') or (user_choice == 'Paper' and computer_choice == 'Rock') or (user_choice == 'Scissors' and computer_choice == 'Paper'):
        result = "You win!"
    else:
        result = "You lose!"
    
    result_label.config(text=f'Computer chose {computer_choice}.\n{result}')

# Setting up the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors")

# Labels
label = tk.Label(root, text="Choose your move:", font=("Helvetica", 14))
label.pack()

# Buttons
rock_button = tk.Button(root, text="Rock", width=15, command=lambda: play('Rock'))
rock_button.pack(pady=5)

paper_button = tk.Button(root, text="Paper", width=15, command=lambda: play('Paper'))
paper_button.pack(pady=5)

scissors_button = tk.Button(root, text="Scissors", width=15, command=lambda: play('Scissors'))
scissors_button.pack(pady=5)

# Result label
result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.pack(pady=20)

# Start the application
root.mainloop()