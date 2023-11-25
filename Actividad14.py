import tkinter as tk
from tkinter import ttk

class Calculadora:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora con Memoria")

        # Configuración del estilo
        self.style = ttk.Style()
        self.style.configure('TButton', font=('Arial', 14), padding=5)
        self.style.configure('TEntry', font=('Arial', 16))

        # Color principal azul
        self.style.configure('TButton', background='#3498db')
        self.style.configure('TEntry', background='#ecf0f1')

        # Color de fondo de la ventana
        master.configure(bg='#bdc3c7')

        self.entrada = ttk.Entry(master, width=16, font=('Arial', 16), justify='right', style='TEntry')
        self.entrada.grid(row=0, column=0, columnspan=4, pady=10)

        self.crear_botones()

        self.valor_memoria = 0

    def crear_botones(self):
        botones = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'C', 'MC', 'MR', 'M+', 'M-'
        ]

        fila = 1
        columna = 0

        for boton in botones:
            ttk.Button(self.master, text=boton, width=4, command=lambda b=boton: self.manipular_boton(b)).grid(row=fila, column=columna, pady=5)
            columna += 1
            if columna > 3:
                columna = 0
                fila += 1

    def manipular_boton(self, valor):
        if valor == 'C':
            self.borrar_entrada()
        elif valor == '=':
            self.realizar_calculo()
        elif valor == 'M+':
            self.memoria_sumar()
        elif valor == 'M-':
            self.memoria_restar()
        elif valor == 'MR':
            self.memoria_recordar()
        elif valor == 'MC':
            self.memoria_limpiar()
        else:
            actual = str(self.entrada.get())
            self.entrada.delete(0, tk.END)
            self.entrada.insert(tk.END, actual + str(valor))

    def borrar_entrada(self):
        self.entrada.delete(0, tk.END)

    def realizar_calculo(self):
        try:
            resultado = eval(self.entrada.get())
            self.entrada.delete(0, tk.END)
            self.entrada.insert(tk.END, str(resultado))
        except:
            self.entrada.delete(0, tk.END)
            self.entrada.insert(tk.END, "Error")

    def memoria_sumar(self):
        try:
            self.valor_memoria += float(self.entrada.get())
        except ValueError:
            self.entrada.delete(0, tk.END)
            self.entrada.insert(tk.END, "Error")

    def memoria_restar(self):
        try:
            self.valor_memoria -= float(self.entrada.get())
        except ValueError:
            self.entrada.delete(0, tk.END)
            self.entrada.insert(tk.END, "Error")

    def memoria_recordar(self):
        self.entrada.delete(0, tk.END)
        self.entrada.insert(tk.END, str(self.valor_memoria))

    def memoria_limpiar(self):
        self.valor_memoria = 0
        self.entrada.delete(0, tk.END)

if __name__ == "__main__":
    raiz = tk.Tk()
    calculadora = Calculadora(raiz)
    raiz.mainloop()