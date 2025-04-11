import temp_data
from customtkinter import *
from tkinter import messagebox
import subprocess
import sys

set_appearance_mode("dark")

PrimaryColor = "#1E1E2F"
SecondaryColor = "#2C2C3C"
TertiaryColor = "#3C3C4F"
QuaternaryColor = "#E0E0E0"
QuinaryColor = "#00FFF5"


root = CTk()
root.title("Foglaló adatai")
root.geometry("400x300")
root.configure(fg_color=PrimaryColor)
root.resizable(False, False)


CTkLabel(root, text="Név", text_color=QuinaryColor, font=("Segoe UI", 14)).grid(row=0, column=0, padx=10, pady=10, sticky="e")
CTkLabel(root, text="Email", text_color=QuinaryColor, font=("Segoe UI", 14)).grid(row=1, column=0, padx=10, pady=10, sticky="e")
CTkLabel(root, text="Telefon", text_color=QuinaryColor, font=("Segoe UI", 14)).grid(row=2, column=0, padx=10, pady=10, sticky="e")

name_entry = CTkEntry(root, width=220, corner_radius=8, fg_color=TertiaryColor, text_color="white")
email_entry = CTkEntry(root, width=220, corner_radius=8, fg_color=TertiaryColor, text_color="white")
phone_entry = CTkEntry(root, width=220, corner_radius=8, fg_color=TertiaryColor, text_color="white")

name_entry.grid(row=0, column=1, padx=10, pady=10)
email_entry.grid(row=1, column=1, padx=10, pady=10)
phone_entry.grid(row=2, column=1, padx=10, pady=10)


def submit():
    name = name_entry.get().strip()
    email = email_entry.get().strip()
    phone = phone_entry.get().strip()

    if not name or not email or not phone:
        messagebox.showerror("Hiba", "Minden mező kitöltése kötelező!")
        return

    data = temp_data.load_data()
    data["customer_data"] = {
        "name": name,
        "email": email,
        "phone": phone
    }
    temp_data.save_data(data)

    root.destroy()
    subprocess.Popen([sys.executable, "jegy_keszito.py"])

CTkButton(root, text="Tovább", command=submit, width=200, height=40,
          fg_color=QuinaryColor, hover_color="#00D9C0", text_color="black",
          font=("Orbitron", 14), corner_radius=20).grid(row=3, column=0, columnspan=2, pady=25)

root.mainloop()
