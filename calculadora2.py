import tkinter as tk
from sympy import symbols, diff, limit, sympify


# Función para mostrar el resultado y el procedimiento
def calculate(event):
    try:
        expr = sympify(expression_entry.get())
        operation = operation_var.get()

        if operation == "Derivada":
            derivative = diff(expr, x)
            procedure = f"La derivada de {expr} con respecto a x es:\n{derivative}"
            result_var.set(str(derivative))
            procedure_text.delete(1.0, tk.END)
            procedure_text.insert(tk.END, procedure)

        elif operation == "Límite":
            lim_point = sympify(limit_entry.get())
            limit_result = limit(expr, x, lim_point)
            procedure = f"El límite de {expr} cuando x tiende a {lim_point} es:\n{limit_result}"
            result_var.set(str(limit_result))
            procedure_text.delete(1.0, tk.END)
            procedure_text.insert(tk.END, procedure)

    except Exception as e:
        result_var.set("Error")
        procedure_text.delete(1.0, tk.END)
        procedure_text.insert(tk.END, str(e))

# Configuración de la ventana principal
root = tk.Tk()
root.title("Calculadora Avanzada")

x = symbols('x')

# Campo para ingresar la expresión
expression_label = tk.Label(root, text="Ingrese la expresión:")
expression_label.grid(row=0, column=0, padx=10, pady=10)
expression_entry = tk.Entry(root, font="lucida 15")
expression_entry.grid(row=0, column=1, padx=10, pady=10, columnspan=3)

# Selección de la operación
operation_var = tk.StringVar(root)
operation_var.set("Derivada")  # Valor predeterminado

operation_menu = tk.OptionMenu(root, operation_var, "Derivada", "Límite")
operation_menu.grid(row=1, column=0, padx=10, pady=10)

# Campo para ingresar el punto del límite (si se selecciona límite)
limit_label = tk.Label(root, text="Punto del límite (solo para límites):")
limit_label.grid(row=1, column=1, padx=10, pady=10)
limit_entry = tk.Entry(root, font="lucida 15")
limit_entry.grid(row=1, column=2, padx=10, pady=10)

# Botón para calcular
calculate_button = tk.Button(root, text="Calcular", font="lucida 15 bold")
calculate_button.grid(row=1, column=3, padx=10, pady=10)
calculate_button.bind("<Button-1>", calculate)

# Resultado
result_label = tk.Label(root, text="Resultado:")
result_label.grid(row=2, column=0, padx=10, pady=10)
result_var = tk.StringVar()
result_entry = tk.Entry(root, textvar=result_var, font="lucida 15", state='readonly')
result_entry.grid(row=2, column=1, padx=10, pady=10, columnspan=3)

# Procedimiento
procedure_label = tk.Label(root, text="Procedimiento:")
procedure_label.grid(row=3, column=0, padx=10, pady=10)
procedure_text = tk.Text(root, height=10, width=50, font="lucida 12")
procedure_text.grid(row=4, column=0, padx=10, pady=10, columnspan=4)

root.mainloop()
