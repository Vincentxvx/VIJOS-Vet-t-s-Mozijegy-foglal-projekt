from tkinter import *
import tkinter as tk
from tkinter import messagebox
import mysql.connector

root = tk.Tk()
root.title("Felhasználó adat bekérése")
root.geometry('500x400')

vezeteknev = Label(root, text="Vezetéknév")
vezeteknev.place(relx=0.1, rely=0.1)
vezeteknev_text = tk.Entry(root, width=40)
vezeteknev_text.place(relx=0.3, rely=0.1)

keresztnev = Label(root, text="Keresztnév")
keresztnev.place(relx=0.1, rely=0.2)
keresztnev_text = tk.Entry(root, width=40)
keresztnev_text.place(relx=0.3, rely=0.2)

lakcim = Label(root, text="Lak Cím")
lakcim.place(relx=0.1, rely=0.3)
lakcim_text = tk.Entry(root, width=40)
lakcim_text.place(relx=0.3, rely=0.3)

iranyitoszam = Label(root, text="Irányító szám")
iranyitoszam.place(relx=0.1, rely=0.4)
iranyitoszam_text = tk.Entry(root, width=40)
iranyitoszam_text.place(relx=0.3, rely=0.4)

gmail = Label(root, text="Email")
gmail.place(relx=0.1, rely=0.5)
gmail_text = tk.Entry(root, width=40)
gmail_text.place(relx=0.3, rely=0.5)

telefonszam = Label(root, text="Telefonszám")
telefonszam.place(relx=0.1, rely=0.6)
telefonszam_text = tk.Entry(root, width=40)
telefonszam_text.place(relx=0.3, rely=0.6)

def foglal():
    vezeteknev = vezeteknev_text.get().strip()
    keresztnev = keresztnev_text.get().strip()
    lakcim = lakcim_text.get().strip()
    iranyitoszam = iranyitoszam_text.get().strip()
    gmail = gmail_text.get().strip()
    telefonszam = telefonszam_text.get().strip()

    if not (vezeteknev and keresztnev and lakcim and iranyitoszam and gmail and telefonszam):
        messagebox.showerror("Hiba", "Minden mezőt ki kell tölteni!")
        return
    
    if "@" not in gmail:
        messagebox.showerror("Hiba", "Érvénytelen email cím!")
        return
    
    kapcsolat = None  # Alapértelmezett kapcsolat változó
    try:
        kapcsolat = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="mozijegy"
        )
        cursor = kapcsolat.cursor()

        cursor.execute("SELECT filmID FROM terem LIMIT 1")
        result = cursor.fetchone()
        if not result:
            messagebox.showerror("Hiba", "Nincs érvényes film az adatbázisban!")
            return
        
        filmID = result[0]  # filmID kiolvasása

        sql = """
        INSERT INTO foglalo (VezetekNev, KeresztNev, LakCim, IranyitoSzam, Gmail, Telefonszam, filmID)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        adatok = (vezeteknev, keresztnev, lakcim, iranyitoszam, gmail, telefonszam, filmID)
        cursor.execute(sql, adatok)
        kapcsolat.commit()

        messagebox.showinfo("Siker", "Foglalás sikeresen rögzítve!")
    except mysql.connector.Error as err:
        print(err)
        messagebox.showerror("Adatbázis hiba", f"Hiba: {err}")
    finally:
        if kapcsolat and kapcsolat.is_connected():
            cursor.close()
            kapcsolat.close()

foglalas = tk.Button(root, text="Foglalás", width=10, height=2, command=foglal)
foglalas.place(relx=0.4, rely=0.8)

root.mainloop()