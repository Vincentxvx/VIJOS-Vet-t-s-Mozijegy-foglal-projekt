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
        self.root.columnconfigure(1, weight=7)
        self.root.columnconfigure(2, weight=1)

        self.root.rowconfigure(0, weight=1)
        self.root.rowconfigure(1, weight=6)
        self.root.rowconfigure(2, weight=1)
        self.root.rowconfigure(3, weight=18)

        col1 = Frame(self.root, bg="red") 
        col1.grid(row=0, column=0, rowspan=4, sticky="nsew")  
        col1.columnconfigure(0, weight=1)
        col1.rowconfigure(0, weight=1)
        Label(col1, text="Col 1 - Full Width", bg="red", font=("Arial", 16)).grid(sticky="nsew")

        col2 = Frame(self.root, bg="green") 
        col2.grid(row=0, column=1, rowspan=4, sticky="nsew")  
        col2.columnconfigure(0, weight=1)
        col2.rowconfigure(0, weight=1)
        Label(col2, text="Col 2 - Full Width", bg="green", font=("Arial", 16)).grid(sticky="nsew")

        col3 = Frame(self.root, bg="red") 
        col3.grid(row=0, column=2, rowspan=4, sticky="nsew")  
        col3.columnconfigure(0, weight=1)
        col3.rowconfigure(0, weight=1)
        Label(col3, text="Col 3 - Full Width", bg="red", font=("Arial", 16)).grid(sticky="nsew")


    def futtat(self):
        self.root.mainloop()


def megnyitas():
    film_ablak = FilmAblak("VIJOS")
    film_ablak.futtat()


if __name__ == "__main__":
    megnyitas()
