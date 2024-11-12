import tkinter as tk
from tkinter import messagebox
import json
import os

# Archivo JSON para guardar los datos de los clientes
archivo_json = 'clientes.json'

def cargar_datos():
    if os.path.exists(archivo_json):
        with open(archivo_json, 'r', encoding='utf-8') as archivo:
            contenido = archivo.read().strip()  # Leer y eliminar espacios en blanco
            if contenido:  # Si el archivo no está vacío
                return json.loads(contenido)
    return {}

# Guardar datos de clientes en archivo JSON
def guardar_datos():
    with open(archivo_json, 'w', encoding='utf-8') as archivo:
        json.dump(clientes, archivo, indent=4, ensure_ascii=False)
# Base de datos de clientes
clientes = cargar_datos()

# Funciones para gestionar clientes
def añadir_cliente():
    rut = entry_rut.get()
    nombre = entry_nombre.get()
    email = entry_email.get()
    telefono = entry_telefono.get()
    tipocli = int(entry_tipocli.get())
    estado = entry_estado.get().upper()

    if rut and nombre and email and telefono and estado in ['A', 'I']:
        clientes[rut] = {
            'nombre': nombre,
            'email': email,
            'teléfono': telefono,
            'tipocli': tipocli,
            'estado': estado
        }
        guardar_datos()
        messagebox.showinfo("Añadir Cliente", "Cliente añadido correctamente.")
    else:
        messagebox.showerror("Error", "Por favor ingrese todos los datos correctamente.")

def eliminar_cliente():
    rut = entry_rut.get()
    if rut in clientes:
        del clientes[rut]
        guardar_datos()
        messagebox.showinfo("Eliminar Cliente", f"Cliente con RUT {rut} eliminado correctamente.")
    else:
        messagebox.showerror("Error", "El cliente no existe.")

def mostrar_cliente():
    rut = entry_rut.get()
    if rut in clientes:
        cliente = clientes[rut]
        info_cliente = f"Nombre: {cliente['nombre']}\nEmail: {cliente['email']}\nTeléfono: {cliente['teléfono']}\nFrecuente: {'Sí' if cliente['tipocli'] == 1 else 'No'}\nEstado: {cliente['estado']}"
        messagebox.showinfo(f"Cliente {rut}", info_cliente)
    else:
        messagebox.showerror("Error", "El cliente no existe.")

def listar_clientes():
    filtro = combo_filtro.get()
    lista = ""
    for rut, datos in clientes.items():
        if (filtro == "Frecuentes" and datos['tipocli'] == 1) or \
           (filtro == "No frecuentes" and datos['tipocli'] == 0) or \
           (filtro == "Activos" and datos['estado'] == 'A') or \
           (filtro == "Inactivos" and datos['estado'] == 'I') or \
           (filtro == "Todos"):
            lista += f"{rut}: {datos['nombre']} - {datos['email']} - {datos['teléfono']} - {'Frecuente' if datos['tipocli'] == 1 else 'No frecuente'} - {datos['estado']}\n"

    messagebox.showinfo("Listado de Clientes", lista if lista else "No hay clientes que coincidan con el filtro.")

# Interfaz gráfica
app = tk.Tk()
app.title("Gestión de Clientes")

# Entradas de datos
tk.Label(app, text="RUT:").grid(row=0, column=0)
entry_rut = tk.Entry(app)
entry_rut.grid(row=0, column=1)

tk.Label(app, text="Nombre:").grid(row=1, column=0)
entry_nombre = tk.Entry(app)
entry_nombre.grid(row=1, column=1)

tk.Label(app, text="Email:").grid(row=2, column=0)
entry_email = tk.Entry(app)
entry_email.grid(row=2, column=1)

tk.Label(app, text="Teléfono:").grid(row=3, column=0)
entry_telefono = tk.Entry(app)
entry_telefono.grid(row=3, column=1)

tk.Label(app, text="Tipo Cliente (1=Frecuente, 0=No frecuente):").grid(row=4, column=0)
entry_tipocli = tk.Entry(app)
entry_tipocli.grid(row=4, column=1)

tk.Label(app, text="Estado (A=Activo, I=Inactivo):").grid(row=5, column=0)
entry_estado = tk.Entry(app)
entry_estado.grid(row=5, column=1)

# Botones para acciones
btn_añadir = tk.Button(app, text="Añadir Cliente", command=añadir_cliente)
btn_añadir.grid(row=6, column=0)

btn_eliminar = tk.Button(app, text="Eliminar Cliente", command=eliminar_cliente)
btn_eliminar.grid(row=6, column=1)

btn_mostrar = tk.Button(app, text="Mostrar Cliente", command=mostrar_cliente)
btn_mostrar.grid(row=7, column=0)

# Filtro para listar clientes
tk.Label(app, text="Filtrar por:").grid(row=8, column=0)
combo_filtro = tk.StringVar()
combo_filtro.set("Todos")
opciones_filtro = tk.OptionMenu(app, combo_filtro, "Frecuentes", "No frecuentes", "Activos", "Inactivos", "Todos")
opciones_filtro.grid(row=8, column=1)

btn_listar = tk.Button(app, text="Listar Clientes", command=listar_clientes)
btn_listar.grid(row=9, column=0)

# Botón para salir
btn_salir = tk.Button(app, text="Terminar", command=app.quit)
btn_salir.grid(row=9, column=1)

app.mainloop()
