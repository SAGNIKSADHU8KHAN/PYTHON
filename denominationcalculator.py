from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk

root = Tk()
root.title("Denomination counter")
root.configure(bg = 'light blue')
root.geometry('650x400')

upload = Image.open('tally.png')
upload = upload.resize((300,300))
image = ImageTk.PhotoImage(upload)

label = Label(root, image=image, bg = "light blue")
label.place(x=180,y=100)
label1 = Label(root, 
               text = "Hey ! user welcome to denomination counter",
               bg = "light blue"
)

label1.place(relx=0.5,y=340, anchor= CENTER)

def msg():
    MsgBox = messagebox.showinfo("Alert! Do you want to count the denomination count?")
    if MsgBox == "ok":
        topWin()

button1 = Button(root,
                 text = "Let's get started",
                 command=msg,
                 bg= "brown",
                 fg="white"
)

button1.place(x=260,y=360)

def topWin():
    top = Toplevel()
    top.title("Denomination Counter")
    top.configure(bg= "light gray")
    top.geometry("600x350+50+50")

    lable = Label(top, text="Enter total amount", bg="light gray")
    entry = Entry(top)
    lbl = Label(top, text= "here are the number of notes for each denomination")

    l1 = Label(top, text= "2000", bg= "light gray")
    l2 = Label(top, text= "500", bg = "light gray")
    l3 = Label(top, text= "200", bg= "light gray")

    t1 = Entry(top)
    t2 = Entry(top)
    t3 = Entry(top)

    def calculate():
        try:
            global amount
            amount = int(entry.get())
            note2000 = amount // 2000
            amount%= 2000
            note500 = amount // 500
            amount%= 500
            note200 = amount // 200
            amount%= 200

            t1.delete(0,END)
            t2.delete(0,END)
            t3.delete(0,END)

            t1.insert(END, str(note2000))
            t2.insert(END, str(note500))
            t3.insert(END, str(note200))
        except ValueError:
            messagebox.showerror("Please, enter a valid number")

    btn = Button(top, text = "Calculate", command=calculate,bg="brown", fg= "white")

    lable.place(x=230, y=50)
    entry.place(x=200, y=80)
    btn.place(x=240, y=120)
    lbl.place(x=140, y=70)

    l1.place(x=180, y=200)
    l2.place(x=100, y=230)
    l3.place(x=180, y=260)

    t1.place(x=270, y=200)
    t2.place(x=270, y=230)
    t3.place(x=270, y=260)

    top.mainloop()

root.mainloop()



