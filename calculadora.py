import tkinter as tk

# Función que actualiza el input de la calculadora
def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(screen.get())
            screen_var.set(result)
        except Exception as e:
            screen_var.set("Error")
        screen.update()
    elif text == "C":
        screen_var.set("")
        screen.update()
    else:
        screen_var.set(screen_var.get() + text)
        screen.update()

# Configuración de la ventana principal
root = tk.Tk()
root.title("Calculadora")

screen_var = tk.StringVar()
screen_var.set("")

# Pantalla de la calculadora
screen = tk.Entry(root, textvar=screen_var, font="lucida 20 bold")
screen.grid(row=0, column=0, columnspan=4, padx=10, pady=10, ipadx=8, ipady=8)

# Botones de la calculadora
buttons = [
    '7', '8', '9', '+',
    '4', '5', '6', '-',
    '1', '2', '3', '*',
    'C', '0', '=', '/'
]

# Creando los botones en una grid
for i in range(4):
    for j in range(4):
        btn = tk.Button(root, text=buttons[i*4+j], font="lucida 15 bold")
        btn.grid(row=i+1, column=j, padx=5, pady=5, ipadx=10, ipady=10)
        btn.bind("<Button-1>", click)

root.mainloop()
