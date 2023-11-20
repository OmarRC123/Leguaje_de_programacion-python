import tkinter as tk
from tkinter import ttk

def click_sumar():
    try:
        cadena2.set("+")
        num1 = float(txt_num1.get())
        num2 = float(txt_num2.get())
        resultado = num1 + num2
        cadena.set(f"{resultado}")
    except ValueError:
        cadena.set("Ingrese números válidos")

def click_restar():
    try:
        cadena2.set("-")
        num1 = float(txt_num1.get())
        num2 = float(txt_num2.get())
        resultado = num1 - num2
        cadena.set(f"{resultado}")
    except ValueError:
        cadena.set("Ingrese números válidos")

def click_multiplicar():
    try:
        cadena2.set("*")
        num1 = float(txt_num1.get())
        num2 = float(txt_num2.get())
        resultado = num1 * num2
        cadena.set(f"{resultado}")
    except ValueError:
        cadena.set("Ingrese números válidos")

def click_dividir():
    try:
        cadena2.set("/")
        num1 = float(txt_num1.get())
        num2 = float(txt_num2.get())
        if num2 != 0:
            resultado = num1 / num2
            cadena.set(f"{resultado}")
        else:
            cadena.set("No se puede dividir por cero")
    except ValueError:
        cadena.set("Ingrese números válidos")


root = tk.Tk()
root.title("Calculadora")
root.geometry("1000x400")


style = ttk.Style()
btn_style = {'font': ('Arial', 12), 'bg': 'skyblue'} 
style.configure("TEntry", padding=10, font=('Arial', 12), background="blue")

root.configure(bg='paleturquoise')

cadena = tk.StringVar()
cadena2 = tk.StringVar()
lbl_msge = tk.Label(root, textvariable=cadena, font=('Arial', 14), bg='paleturquoise')
lbl_msge.place(x=550, y=55)
lbl_ope = tk.Label(root, textvariable=cadena2, font=('Arial', 18), bg='paleturquoise')
lbl_ope.place(x=270, y=55)
lbl_igual = tk.Label(root, text= "=", font=('Arial', 18), bg='paleturquoise')
lbl_igual.place(x=510, y=55)
lbl_num1 = tk.Label(root, text= "Numero 1", font=('Arial', 16), bg='paleturquoise')
lbl_num1.place(x=100, y=20)
lbl_num2 = tk.Label(root, text= "Numero 2", font=('Arial', 16), bg='paleturquoise')
lbl_num2.place(x=350, y=20)
lbl_resul = tk.Label(root, text= "Resultado", font=('Arial', 16), bg='paleturquoise')
lbl_resul.place(x=530, y=20)

txt_num1 = ttk.Entry(root, font=('Arial', 12))
txt_num1.place(x=50, y=50)

txt_num2 = ttk.Entry(root, font=('Arial', 12))
txt_num2.place(x=300, y=50)

btn_sumar = tk.Button(root, text="SUMAR", command=click_sumar, **btn_style)
btn_sumar.place(x=50, y=150)

btn_restar = tk.Button(root, text="RESTAR", command=click_restar, **btn_style)
btn_restar.place(x=250, y=150)

btn_multiplicar = tk.Button(root, text="MULTIPLICAR", command=click_multiplicar, **btn_style)
btn_multiplicar.place(x=450, y=150)

btn_dividir = tk.Button(root, text="DIVIDIR", command=click_dividir, **btn_style)
btn_dividir.place(x=650, y=150)

root.mainloop()