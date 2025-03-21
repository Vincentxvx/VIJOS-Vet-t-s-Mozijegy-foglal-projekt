from adatbázis import AdatBazis
import mysql.connector
from tkinter import * 
import tkinter as tk
from tkinter import messagebox

nemtom = AdatBazis.cursor()

rows = 9
cols = 13
gomb_szamlalo = 1
kivalasztott_gomb = {}
foglalt_gomb = []

nemtom = AdatBazis.cursor(buffered=True)
nemtom.execute("SELECT Terem_Szam, Terem_ulohelyek, Terem_foglalt_ulohelyek FROM terem")


def beolvas_foglalt_gombokat():
    foglalt_gombok = []
    try:
        with open("foglalas.txt", "r") as file:
            for line in file:
                if "Foglalva" in line:
                    button_id = line.strip().split(": ")[1]
                    foglalt_gombok.append(button_id)
    except FileNotFoundError:
        pass
    return foglalt_gombok

def HIBA():
    global foglalt_gomb
    foglalt_gomb = beolvas_foglalt_gombokat()
    for row in range(rows):
        for col in range(cols):
            button_id = f"{row}_{col}"
            if button_id in foglalt_gomb:
                button = root.grid_slaves(row=row, column=col)[0]
                button.config(bg="red", state="disabled")

def Gomb_Szin(button, button_id):
    if button_id in foglalt_gomb:
        pass
    elif button_id in kivalasztott_gomb:
        button.config(bg="green")
        del kivalasztott_gomb[button_id]
    else:
        kivalasztott_gomb[button_id] = button
        button.config(bg="yellow")
def foglal():
    global foglalt_gomb
    try:
        terem_szam = 1
        film = 'Film1'
        adat = 'Adat1'
        filmID = 7
        
        total_seats = 180
        
        nemtom.execute("SELECT COUNT(*) FROM terem WHERE Terem_Szam = %s", (terem_szam,))
        booked_count = nemtom.fetchone()[0]
        
        if total_seats - booked_count < len(kivalasztott_gomb):
            messagebox.showerror("Hiba", "Nincs elég szék!")
            return

        for i, button_id in enumerate(kivalasztott_gomb):
            new_available = total_seats - (booked_count + i + 1)
            
            insert_query = """
            INSERT INTO terem (Terem_Szam, Teremben_vetittett_film, STB_filmes_adat, Terem_ulohelyek, Terem_foglalt_ulohelyek, filmID)
            VALUES (%s, %s, %s, %s, %s, %s)
            """
            nemtom.execute(insert_query, (terem_szam, film, adat, new_available, button_id, filmID))
        
        AdatBazis.commit()
        
        with open("foglalas.txt", "a") as file:
            for button_id in kivalasztott_gomb:
                file.write(f"Foglalva: {button_id}\n")
                button = kivalasztott_gomb[button_id]
                button.config(bg="red")
                foglalt_gomb.append(button_id)
        
        messagebox.showinfo("Foglalás", "Sikeresen lefoglaltad a kiválasztott gombokat!")
    
    except mysql.connector.Error as err:
        print(f"SQL hiba: {err}")
        messagebox.showerror("Hiba", "Hiba történt a foglalás során!")

def Gomb_Letrehozasa():
    global gomb_szamlalo
    for row in range(rows):
        for col in range(cols):
            button_id = f"{row}_{col}"  
            if col == 6:
                tk.Label(root, text=" ", width=5, height=2).grid(row=row, column=col)
            else:
                button = tk.Button(root, text=str(gomb_szamlalo), width=5, height=2, bg="green")
                button.config(command=lambda b=button, id=button_id: Gomb_Szin(b, id))  
                button.grid(row=row, column=col)
                gomb_szamlalo += 1

root = tk.Tk()
root.title("Mozi székek foglalása")

foglalas_button = tk.Button(root, text="Foglalás", width=5, height=2, command=foglal)
foglalas_button.grid(column=6, row=10)

Gomb_Letrehozasa()
HIBA()

root.mainloop()