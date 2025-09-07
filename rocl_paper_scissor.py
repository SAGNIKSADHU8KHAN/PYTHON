import tkinter as tk
import random

def play(user_choice):
    options = ["Rock", "Paper", "Scissor"]
    computer_choice = random.choice(options)

    if user_choice == computer_choice:
        result = "It's a tie"

    elif(user_choice == "Rock" and computer_choice == "Scissor") or \
        (user_choice == "Paper" and computer_choice == "Rock") or \
        (user_choice == "Scissor" and computer_choice == "Paper"):
        result = 'You Win!'

    else:
        reault = "Computer Wins!"

    result_label.config(text = f"You(user_choice)\nComputer: {computer_choice}\n\n{result}")

root = tk.Tk()
root.title("Rock Paper Scissor")
root.geometry("400x300")
root.resizable(False, False)

title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 16, "bold"))
title_label.pack(pady=10)


instr_label = tk.Label(root, text="Choose your option:", font=("Arial", 12))
instr_label.pack(pady=5)


button_frame = tk.Frame(root)
button_frame.pack(pady=10)

rock_btn = tk.Button(button_frame, text="Rock", width=10, font=("Arial", 12), command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(button_frame, text="Paper", width=10, font=("Arial", 12), command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=5)

scissor_btn = tk.Button(button_frame, text="Scissor", width=10, font=("Arial", 12), command=lambda: play("Scissor"))
scissor_btn.grid(row=0, column=2, padx=5)

result_label = tk.Label(root, text="", font=("Arial", 12), fg="blue", justify="center")
result_label.pack(pady=20)


root.mainloop()

