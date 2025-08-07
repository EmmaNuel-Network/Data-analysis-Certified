import tkinter as tk
from tkinter import messagebox

def suma():
    resultado = float(entry1.get()) + float(entry2.get())
    messagebox.showinfo("Resultado", f"La suma es: {resultado}")

def resta():
    resultado = float(entry1.get()) - float(entry2.get())
    messagebox.showinfo("Resultado", f"La resta es: {resultado}")

def multiplicacion():
    resultado = float(entry1.get()) * float(entry2.get())
    messagebox.showinfo("Resultado", f"La multiplicación es: {resultado}")

def division():
    try:
        resultado = float(entry1.get()) / float(entry2.get())
        messagebox.showinfo("Resultado", f"La división es: {resultado}")
    except ZeroDivisionError:
        messagebox.showerror("Error", "División por cero no permitida")

root = tk.Tk()
root.title("Calculadora")

# Configurar la cuadrícula para que se expanda
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)
root.rowconfigure(2, weight=1)
root.rowconfigure(3, weight=1)

tk.Label(root, text="Número 1:").grid(row=0, column=0, sticky="nsew")
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, sticky="nsew")

tk.Label(root, text="Número 2:").grid(row=1, column=0, sticky="nsew")
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1, sticky="nsew")

tk.Button(root, text="Sumar", command=suma).grid(row=2, column=0, sticky="nsew")
tk.Button(root, text="Restar", command=resta).grid(row=2, column=1, sticky="nsew")
tk.Button(root, text="Multiplicar", command=multiplicacion).grid(row=3, column=0, sticky="nsew")
tk.Button(root, text="Dividir", command=division).grid(row=3, column=1, sticky="nsew")

root.mainloop()





