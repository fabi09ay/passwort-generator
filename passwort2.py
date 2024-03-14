import tkinter as tk
from tkinter import ttk
import random
import string

def generate_password():
    password_length = length_var.get()
    if password_length:
        if use_symbols_var.get():
            characters = string.ascii_letters + string.digits + '!;?();/;&;%$§'
        else:
            characters = string.ascii_letters + string.digits
        password = ''.join(random.choices(characters, k=password_length))
        password_var.set(password)

def copy_password():
    password = password_var.get()
    root.clipboard_clear()
    root.clipboard_append(password)
    status_label.config(text="Passwort kopiert!")

# GUI erstellen
root = tk.Tk()
root.title("Passwortgenerator")
root.geometry("300x400")

style = ttk.Style()
style.theme_use('clam')

length_var = tk.IntVar()
use_symbols_var = tk.BooleanVar()

frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0)

length_label = ttk.Label(frame, text="Passwortlänge auswählen:")
length_label.grid(row=0, column=0, columnspan=2)

def select_length(value):
    length_var.set(value)

six_button = ttk.Radiobutton(frame, text="6", variable=length_var, value=6, command=lambda: select_length(6))
six_button.grid(row=1, column=0)

eight_button = ttk.Radiobutton(frame, text="8", variable=length_var, value=8, command=lambda: select_length(8))
eight_button.grid(row=1, column=1)

ten_button = ttk.Radiobutton(frame, text="10", variable=length_var, value=10, command=lambda: select_length(10))
ten_button.grid(row=2, column=0)

twelve_button = ttk.Radiobutton(frame, text="12", variable=length_var, value=12, command=lambda: select_length(12))
twelve_button.grid(row=2, column=1)

fourteen_button = ttk.Radiobutton(frame, text="14", variable=length_var, value=14, command=lambda: select_length(14))
fourteen_button.grid(row=3, column=0)

sixteen_button = ttk.Radiobutton(frame, text="16", variable=length_var, value=16, command=lambda: select_length(16))
sixteen_button.grid(row=3, column=1)

eighteen_button = ttk.Radiobutton(frame, text="18", variable=length_var, value=18, command=lambda: select_length(18))
eighteen_button.grid(row=4, column=0)

twenty_button = ttk.Radiobutton(frame, text="20", variable=length_var, value=20, command=lambda: select_length(20))
twenty_button.grid(row=4, column=1)

symbol_check = ttk.Checkbutton(frame, text="Symbole verwenden", variable=use_symbols_var)
symbol_check.grid(row=5, column=0, columnspan=2)

generate_button = ttk.Button(frame, text="Passwort generieren", command=generate_password)
generate_button.grid(row=6, column=0, columnspan=2, pady=10)

password_var = tk.StringVar()
password_entry = ttk.Entry(frame, textvariable=password_var, state='readonly', width=20)
password_entry.grid(row=7, column=0, columnspan=2, pady=10)

copy_button = ttk.Button(frame, text="Kopieren", command=copy_password)
copy_button.grid(row=8, column=0, columnspan=2)

status_label = ttk.Label(frame, text="")
status_label.grid(row=9, column=0, columnspan=2)

root.mainloop()
