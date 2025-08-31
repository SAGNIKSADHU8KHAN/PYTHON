from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("image")
root.geometry("400x400")

upload = Image.open("flowers.jpg")

image = ImageTk.PhotoImage(upload)

lable = Label(root,image=image, height=350, width=300)
lable.place(x=50, y=0)

lable2 = Label(root, text="This is how we add image to tkinter")
lable2.place(x=54, y=360)

root.mainloop()