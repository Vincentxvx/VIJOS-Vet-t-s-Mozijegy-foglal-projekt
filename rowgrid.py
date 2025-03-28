from tkinter import *
from customtkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter.messagebox import showinfo
import tkinter.font as tkFont
import os
from PIL import Image, ImageTk
import threading
import time

PrimaryColor = "#104F55"
SecondaryColor = "#32746D"
TertiaryColor = "#9EC5AB"
QuaternaryColor = "#01200F"
QuinaryColor = "#011502" 


class FilmAblak:
    def __init__(self, cim):
        self.root = Tk()
        self.root.title(f"{cim}")
        self.root.config(bg=PrimaryColor)
        self.root.geometry('1250x1000')
        self.root.minsize(1250, 1000)

        self.kepek = ["./kep3.jpg", "./kep4.jpg", "./kep5.jpg"]
        self.kepekkesz = []
        
        for img_path in self.kepek:
            img = Image.open(img_path).resize((1000, 250))
            img = ImageTk.PhotoImage(img)
            self.kepekkesz.append(img)
        
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=7)
        self.root.columnconfigure(2, weight=1)

        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=6)
        self.root.rowconfigure(2, weight=1)
        self.root.rowconfigure(3, weight=18)

        row1 = Frame(self.root, bg="red") 
        row1.grid(row=0, column=0, columnspan=3, sticky="nsew")  
        row1.columnconfigure(0, weight=1)
        row1.rowconfigure(0, weight=1)
        Label(row1, text="LEGSIGMÁBB NAVBAR WAAAAAAAAAAAAAAAAAAAAAAAAA", bg="red", font=("Arial", 16)).grid(sticky="nsew")

        row2 = Frame(self.root, bg="green")
        row2.grid(row=1, column=0, columnspan=3, sticky="nsew")  
        row2.columnconfigure(0, weight=1)
        row2.rowconfigure(0, weight=1)
        self.hanyadik = 0
        self.mylable = Label(row2, image=self.kepekkesz[self.hanyadik], bd=0, bg="green")
        self.mylable.grid(row=0, column=0) 
        self.mylable.columnconfigure(0, weight=1)
        self.mylable.rowconfigure(0, weight=1)


        def kovetkezo(irany):
            if irany == 1:
                self.hanyadik = (self.hanyadik + 1) % len(self.kepekkesz)
            else:
                self.hanyadik = (self.hanyadik - 1) % len(self.kepekkesz)

            self.mylable.config(image=self.kepekkesz[self.hanyadik])

        
        def timer():
            while True:
                time.sleep(5)  
                self.root.after(0, lambda: kovetkezo(1)) 

        t = threading.Thread(target=timer, daemon=True)
        t.start()
        

        row3 = Frame(self.root, bg="red") 
        row3.grid(row=2, column=1, columnspan=1, sticky="nsew")  
        row3.columnconfigure(0, weight=1)
        row3.rowconfigure(0, weight=1)
        Label(row3, text="Row 3 - Full Width", bg="red", font=("Arial", 16)).grid(sticky="nsew")

        row4 = Frame(self.root, bg="green") 
        row4.grid(row=3, column=1, columnspan=1, sticky="nsew")  
        row4.columnconfigure(0, weight=1)
        row4.rowconfigure(0, weight=1)
        Label(row4, text="Row 4 - Full Width", bg="green", font=("Arial", 16)).grid(sticky="nsew")

        mozikartya = CTkFrame(row4,height=250, width=750, corner_radius=10)
        mozikartya.grid(row=0, column=0)



        col1 = Frame(self.root,bg="blue")
        col1.grid(column=0,row=3,rowspan=2)
        col1.rowconfigure(0, weight=1)
        col1.columnconfigure(0, weight=1)
        Label(col1,text="Col 1 - Full Width", bg="green", font=("Arial", 16)).grid(sticky="nsew")

        col2 = Frame(self.root,bg="blue")
        col2.grid(column=2,row=2,rowspan=2)
        col2.rowconfigure(0, weight=1)
        col2.columnconfigure(0, weight=1)
        Label(col2,text="Col 1 - Full Wiggggggggggggth", bg="green", font=("Arial", 16)).grid(sticky="nsew")

        row1.grid_propagate(False)
        row2.grid_propagate(False)
        row3.grid_propagate(False)
        col1.grid_propagate(False)
        col2.grid_propagate(False)

    def futtat(self):
        self.root.mainloop()


def megnyitas():
    film_ablak = FilmAblak("VIJOS")
    film_ablak.futtat()


if __name__ == "__main__":
    megnyitas()
