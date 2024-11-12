#autor
#Daniel Navarrete Silva
import re
import os

def limpiar():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")

def leer(wr100, wr200):
    wr1 = []
    wr2 = []

    try:
        with open(wr100, 'r', encoding='UTF-8') as f:
            next(f)
            wr100 = [line.strip() for line in f if line.strip()]
        with open(wr200, 'r', encoding='UTF-8') as g:
            next(g)
            for line in g:
                try: 
                    datos =line.strip().split()
                    wr200.append(float(datos[1]))
                pass
        