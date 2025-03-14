from tkinter import *
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

        
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=5)
        self.root.columnconfigure(2, weight=1)
        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=5)

       
        self.kepek = ["./logo.png", "./kep3.jpg", "./kep4.jpg", "./kep5.jpg"]
        self.kepekkesz = []
        
        for img_path in self.kepek:
            img = Image.open(img_path).resize((1000, 250))
            img = ImageTk.PhotoImage(img)
            self.kepekkesz.append(img)

        self.hanyadik = 0
        self.mylable = Label(self.root, image=self.kepekkesz[self.hanyadik], bd=0)
        self.mylable.grid(row=0, column=1, pady=20, columnspan=1)

       
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


        hatra = Button(self.root, text="<-", command=lambda: kovetkezo(0), bg=SecondaryColor, fg="white")
        hatra.grid(row=0, column=0, padx=20, pady=10, sticky="w")

        elore = Button(self.root, text="->", command=lambda: kovetkezo(1), bg=SecondaryColor, fg="white")
        elore.grid(row=0, column=2, padx=20, pady=10, sticky="e")

    def futtat(self):
        self.root.mainloop()


def megnyitas():
    film_ablak = FilmAblak("VIJOS")
    film_ablak.futtat()


if __name__ == "__main__":
    megnyitas()
