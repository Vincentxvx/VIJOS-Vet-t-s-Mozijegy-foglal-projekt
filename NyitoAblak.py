from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
from tkinter.messagebox import showinfo
import tkinter.font as tkFont

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
        self.root.minsize(1500, 1000)
        self.root.maxsize(1500, 1000)
        self.root.geometry('1500x1000')

        test = Button(self.root)
        test.place(relx=0.5, rely=0.5)






    def futtat(self):
        self.root.mainloop()




def megnyitas():
    film_ablak = FilmAblak("VIJOS")
    film_ablak.futtat()


if __name__ == "__main__":
    megnyitas()