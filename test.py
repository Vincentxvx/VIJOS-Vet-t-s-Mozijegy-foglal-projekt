from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Sigam")
root.geometry("500x500")

test = Image.open("./logo.png").resize((100,100))
test = ImageTk.PhotoImage(test)

mylable = Label(root, image=test)
mylable.pack(pady=20)


root.mainloop()