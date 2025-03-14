from adatbázis import AdatBazis
import mysql
import mysql.connector
from tkinter import * 
import tkinter as tk
from tkinter import messagebox


nemtom = AdatBazis.cursor()




# DELETE
# sigma = "DELETE FROM terem WHERE Terem_Szam = 1"

# nemtom.execute(sigma)

# AdatBazis.commit()
# AdatBazis.close()

root = tk.Tk()
root.title("Mozi székek foglalása")

rows = 9
cols = 13


gomb_szamlalo = 1
kivalasztott_gomb = {}
foglalt_gomb = []

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
    nemtom.execute("SELECT Terem_Szam, Terem_ulohelyek FROM Terem")
    termek = nemtom.fetchall()

    for terem in termek:
        terem_szam = terem[0]
        teremben_ulohelyek = terem[1]

        print(f"Terem {terem_szam} - Ülőhelyek: {teremben_ulohelyek}")

        if teremben_ulohelyek > 0:
            uj_ulohelyek = teremben_ulohelyek - 1
        else:
            uj_ulohelyek = 180

        nemtom.execute(
            "UPDATE Terem SET Terem_ulohelyek = %s WHERE Terem_Szam = %s",
            (uj_ulohelyek, terem_szam)
        )

    nemtom.execute("SELECT Terem_Szam, Terem_ulohelyek FROM Terem")
    termek = nemtom.fetchall()
    for terem in termek:
        print(f"Utolsó frissítés - Terem {terem[0]}: Ülőhelyek: {terem[1]}")

    AdatBazis.commit()

    nemtom.execute("DROP EVENT IF EXISTS csokkeno_ulohelyek")

    szamlalo = """    """

    nemtom.execute(szamlalo)
    AdatBazis.commit()

    with open("foglalas.txt", "a") as file:
        for button_id in kivalasztott_gomb:
            file.write(f"Foglalva: {button_id}\n")
            button = kivalasztott_gomb[button_id]
            button.config(bg="red") 
            foglalt_gomb.append(button_id)
            
            mozi = """
            INSERT INTO terem (Terem_Szam, Teremben_vetittett_film, STB_filmes_adat, Terem_ulohelyek, Terem_foglalt_ulohelyek) 
            VALUES (%s, %s, %s, %s, %s)
            """
            mozik = (1, "asdf", "as", 180, button_id)  
            nemtom.execute(mozi, mozik)
            AdatBazis.commit()

    messagebox.showinfo("Foglalás", "Sikeresen lefoglaltad a kiválasztott gombokat!")
    
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

foglalas_button = tk.Button(root, text="Foglalás", width=5, height=2, command=foglal)
foglalas_button.grid(column=6, row=10)

Gomb_Letrehozasa()
HIBA()

root.mainloop()
