from adatbázis import AdatBazis
import mysql
import mysql.connector
from tkinter import * 
import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("Felhasználó adat bekérése")
root.geometry('400x200')

vezeteknev = Label(root, text="Vezeteknév")
vezeteknev.place(relx=0, rely=0.1)

vezeteknev_text = tk.Text(root, height = 1, width = 15) 
vezeteknev_text.place(relx=0.2, rely=0.1) 
  

root.mainloop()
