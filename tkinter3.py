import random
import string 
import tkinter as tk
from tkinter import messagebox

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showerror("Error! Password length must be 4")
            return
        
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        digits = string.digits
        punctuations = string.punctuation

        all_chars = lower + upper + digits + punctuations

        
        password = [
            random.choice(lower),
            random.choice(upper),
            random.choice(digits),
            random.choice(punctuations)]
        
       
        password += random.choices(all_chars, k=length - 4)

        random.shuffle(password)

      
        password_entry.delete(0, tk.END)
        password_entry.insert(0, "".join(password))

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for length")

root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x200")
root.resizable(False, False)


tk.Label(root, text="Enter password length:", font=("Arial", 12)).pack(pady=5)
length_entry = tk.Entry(root, font=("Arial", 12))
length_entry.pack(pady=5)
length_entry.insert(0, "12")  


generate_btn = tk.Button(root, text="Generate Password", font=("Arial", 12, "bold"), command=generate_password)
generate_btn.pack(pady=10)

password_entry = tk.Entry(root, font=("Arial", 12), width=30, justify="center")
password_entry.pack(pady=5)


root.mainloop()