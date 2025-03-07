from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter.messagebox import showinfo
import tkinter.font as tkFont
import os
from PIL import Image, ImageTk

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
        self.root.minsize(1250, 1000)
        self.root.maxsize(1250, 1000)
        self.root.geometry('1250x1000')

        # Ablak teteji carousel
        self.kepek = ["./logo.png","./kep3.jpg","./kep4.jpg","./kep5.jpg"]
        self.kepekkesz = []
        for i in range(0,len(self.kepek)):
            self.name = f"kep{i+1}"
            print(self.name)
            self.name = Image.open(self.kepek[i]).resize((1000,250))
            self.name = ImageTk.PhotoImage(self.name)
            self.kepekkesz.append(self.name)

        

        self.kep1 = Image.open("./demo_image.jpg").resize((1000,250))
        self.kep1 = ImageTk.PhotoImage(self.kep1)
        self.hanyadik = 0


        self.mylable = Label(self.root, image=self.kep1,bd=0,width=1000, height=250)
        self.mylable.place(anchor=N, relx=0.5, rely=0.04)

        def kovetkezo():
            if self.hanyadik == len(self.kepekkesz):

                self.hanyadik = 0
            else:
                self.hanyadik += 1

            self.mylable.config(image=self.kepekkesz[self.hanyadik])
        
        
        gomb = Button(self.root, text="->", command=kovetkezo)
        gomb.place(anchor=N, relx=0.95,rely=0.1)


    def futtat(self):
        self.root.mainloop()




def megnyitas():
    film_ablak = FilmAblak("VIJOS")
    film_ablak.futtat()


if __name__ == "__main__":
    megnyitas()