from tkinter import *

root = Tk()
root.geometry("400x300")
root.title("main")

def topwin():
    top = Toplevel()
    top.geometry("180x100")
    top.title("top level")

    lable = Label(top, text="top level window")

    lable.pack()

    top.mainloop()

lable2 = Label(root, text="root level")

button = Button(root, text="clich here to open another window", command = topwin)

lable2.pack()
button.pack()

root.mainloop()