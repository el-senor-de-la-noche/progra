#autor: Daniel Navarrete
import tkinter as tk
import os
def limpiar():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def potencia_t(consumo_computadora, consumo_cafetera, consumo_hielera):
    return (consumo_computadora*15) + consumo_cafetera + consumo_hielera

def funciom_imprime_consumo_amperes(potencia_total):
    tension = 220
    consumo_amperes = potencia_total/tension
    return consumo_amperes

def calcular():
    consumo_computadoras = int(entrar_computadora.get())
    consumo_cafetera = int(entrar_cafetera.get())
    consumo_hielera = int(entrar_hielera.get())

    potencia_total_consumida =potencia_t(consumo_computadoras, consumo_cafetera, consumo_hielera)
    consumo_amperes = funciom_imprime_consumo_amperes(potencia_total_consumida)

    label_watts.config(text=f"consumo total en watts:{potencia_total_consumida} W")
    label_amperios.config(text = f"consumo total en amperios: {consumo_amperes}A")

root = tk.Tk()
root.title("calculo de consumo efectrico")

tk.Label(root, text= "consumo por computadora (Watts):").grid(row=0, column=0)
entrar_computadora = tk.Entry(root)
entrar_computadora.grid(row=0, column=1)

tk.Label(root, text="consumo de la cafetera (Watts):").grid(row=1, column=0)
entrar_cafetera = tk.Entry(root)
entrar_cafetera.grid(row=1,column=1)

tk.Label(root, text= "cosnumo de la hielera (Watts):").grid(row=2, column=0)
entrar_hielera = tk.Entry(root)
entrar_hielera.grid(row=2, column=1)

button_calcular = tk.Button(root, text="calcular", command=calcular)
button_calcular.grid(row=3, column=0, columnspan=2)

label_watts =tk.Label(root,text="cosumo total en watts: ")
label_watts.grid(row=4, column=0, columnspan=2)

label_amperios = tk.Label(root, text="comnsumo en amperios: ")
label_amperios.grid(row=5, column=0, columnspan= 2)

root.mainloop()
