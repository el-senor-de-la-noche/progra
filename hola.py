#autor
#Daniel Navarrete
import tkinter as tk 
from tkinter import messagebox
import math
import os

def limpiar():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")
def calcular(medida_placa, medida_pieza, cantidad_piezas):
    largo_placa, ancho_placa = medida_placa
    largo_pieza, ancho_pieza = medida_pieza

    area_placa = largo_placa * ancho_placa
    area_pieza = largo_pieza * ancho_pieza
    area_total_piezas = area_pieza * cantidad_piezas
    perdida_por_corte = 0.4 #cm
    area_total_piezas_con_perdida = area_total_piezas +(cantidad_piezas -1 )* perdida_por_corte * largo_pieza

    cantidad_placas = math.ceil(area_total_piezas / area_placa)

    area_total_usada =cantidad_placas * area_placa
    superficie_sobrante = area_total_usada - area_total_piezas_con_perdida
    superficie_perdida = (cantidad_piezas - 1)* perdida_por_corte* largo_pieza

    precio_placa = 29900
    costo_total = cantidad_placas*precio_placa

    return cantidad_placas, costo_total, superficie_sobrante, superficie_perdida

def  mostrar():
    try:
        largo_placa = float(entrada_largo_placa.get())
        ancho_placa = float(entrada_ancho_placa.get())
        largo_pieza = float(entrada_largo_pieza.get())
        ancho_pieza = float(entrada_ancho_pieza.get())
        cantidad_piezas = int(entrada_cantidad_piezas.get())

        medida_placa = (largo_placa, ancho_placa)
        medida_pieza = (largo_pieza, ancho_pieza)
        
        cantidad_placas, costo_total, superficie_sobrante, superficie_perdida = calcular(medida_placa,medida_pieza, cantidad_piezas)
        resultado = (
            f"Cantidad de placas necesarias: {cantidad_placas}\n"
            f"Costo total: ${costo_total}\n"
            f"Superficie sobrante en cm²: {superficie_sobrante}\n"
            f"Superficie perdida por cortes en cm²: {superficie_perdida}\n"
        )
        messagebox.showinfo("Resultados:", resultado)
    except ValueError:
        messagebox.showerror("Error", "Porfavor, ingrese valores válidos.")
def tkinter():
    ventana = tk.Tk()
    ventana.title("Calculadora de cortes de melamina")

    tk.Label(ventana, text= "Dimensiones de la placa de melamina(cm)").grid(row = 0, column = 0, padx = 10, pady = 5)
    tk.Label(ventana, text = "Largo").grid(row= 1, column = 0, padx = 10, pady = 5)
    tk.Label(ventana, text = "Ancho").grid(row = 2, column = 0,padx = 10, pady = 5)

    global entrada_largo_placa, entrada_ancho_placa
    entrada_largo_placa = tk.Entry(ventana)
    entrada_ancho_placa = tk.Entry(ventana)
    entrada_largo_placa.grid(row=1, column=1, padx=10, pady=5)
    entrada_ancho_placa.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(ventana,text = "Dimensiones de la piesa deseada a cortar(cm):").grid(row=3, column = 0, padx= 10, pady = 5)
    tk.Label(ventana,text = "Largo").grid(row=4, column=0, padx=10, pady=5)
    tk.Label(ventana,text = "Ancho").grid(row=5, column=0, padx=10, pady=5)
    
    global entrada_largo_pieza, entrada_ancho_pieza
    entrada_largo_pieza =tk.Entry(ventana)
    entrada_ancho_pieza =tk.Entry(ventana)
    entrada_largo_pieza.grid(row=4, column=1, padx=10, pady=5)
    entrada_ancho_pieza.grid(row=5, column=1, padx=10, pady=5)

    tk.Label(ventana, text = "Cantidad de piezas a cortar:").grid(row=6, column=0, padx=10, pady=5)
    global entrada_cantidad_piezas
    entrada_cantidad_piezas = tk.Entry(ventana)
    entrada_cantidad_piezas.grid(row=6, column=1, padx=10, pady=5)


    tk.Button(ventana, text = "Calcular", command = mostrar).grid(row=7, column=0, columnspan = 2, pady=5)

    ventana.mainloop()




if __name__ == '__main__':
    limpiar()
    tkinter()
