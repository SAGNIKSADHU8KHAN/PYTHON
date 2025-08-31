from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("400x400")

def msg():
           messagebox.showwarning("alert!","Stop. Virus found.") 

button = Button(root, text="Scan for virus", command = msg)
button.place(x=50,y=60)

root.mainloop()     