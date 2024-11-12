#autor Daniel Navarrete
import tkinter as tk
from tkinter import messagebox

def identificar_triangulo():
    # Obtener los valores de los lados
    a_str = entry_a.get()
    b_str = entry_b.get()
    c_str = entry_c.get()

    # Verificar si las entradas son números válidos
    if a_str.replace('.', '', 1).isdigit() and b_str.replace('.', '', 1).isdigit() and c_str.replace('.', '', 1).isdigit():
        a = float(a_str)
        b = float(b_str)
        c = float(c_str)
        
        if a <= 0 or b <= 0 or c <= 0:
            messagebox.showerror("Error", "Las longitudes deben ser positivas.")
            return
        
        # Verificar si es un triángulo válido
        if a + b > c and a + c > b and b + c > a:
            if a == b == c:
                tipo = "Equilátero"
            elif a == b or a == c or b == c:
                tipo = "Isósceles"
            else:
                tipo = "Escaleno"
            messagebox.showinfo("Resultado", f"El triángulo es {tipo}.")
        else:
            messagebox.showerror("Error", "Las longitudes no forman un triángulo válido.")
    else:
        messagebox.showerror("Error", "Por favor, ingrese números válidos.")

# Configuración de la ventana principal
root = tk.Tk()
root.title("Identificador de Triángulos")

# Creación de los elementos de la interfaz
tk.Label(root, text="Lado A:").grid(row=0, column=0, padx=10, pady=10)
tk.Label(root, text="Lado B:").grid(row=1, column=0, padx=10, pady=10)
tk.Label(root, text="Lado C:").grid(row=2, column=0, padx=10, pady=10)

entry_a = tk.Entry(root)
entry_b = tk.Entry(root)
entry_c = tk.Entry(root)

entry_a.grid(row=0, column=1, padx=10, pady=10)
entry_b.grid(row=1, column=1, padx=10, pady=10)
entry_c.grid(row=2, column=1, padx=10, pady=10)

button_identificar = tk.Button(root, text="Identificar Triángulo", command=identificar_triangulo)
button_identificar.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

# Ejecutar la aplicación
root.mainloop()
