# Autores: Daniel Navarrete, Alvaro
import os

def limpiar():
    """Limpia la terminal dependiendo del sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')

def leer_datos(ruta):
    secuencias = []
    secuencia_actual = []

    ent = open(ruta, 'r')  # Abre el archivo
    lineas = ent.readlines()  # Lee todas las líneas
    ent.close()  # Cierra el archivo

    for linea in lineas:
        if linea.strip():  # Ignorar líneas en blanco
            numeros = linea.split()  # Divide la línea en partes
            for num in numeros:
                num = int(num)  # Convierte cada número a entero
                if num == 0:
                    if secuencia_actual:
                        secuencias.append(secuencia_actual)
                        secuencia_actual = []
                else:
                    secuencia_actual.append(num)

    # Agregar la última secuencia si no termina en 0
    if secuencia_actual:
        secuencias.append(secuencia_actual)

    return secuencias

#funcion para encontrar las cimas en una lista de secuencias
def cimas_seq(secuencias):
    
    resultados = []
    for sec in secuencias:
        n = len(sec)
        i = 0
        while i < n:
            # Verificar si es el inicio de una cima
            if i > 0 and i < n - 1 and sec[i] > sec[i - 1] and sec[i] >= sec[i + 1]:
                inicio = i
                # Encontrar la longitud de la cima
                while i < n - 1 and sec[i] == sec[i + 1]:
                    i = i + 1
                # Verificar la condición de la cima
                if i < n - 1 and sec[inicio] > sec[i + 1]:
                    longitud = i - inicio + 1
                    resultados.append(f"{inicio + 1} {longitud}")
            i = i + 1
        resultados.append("***")
    return resultados

def escribir_cimas(salida, resultados):
    f = open(salida, 'w')  # Abre el archivo para escritura
    for resultado in resultados: 
        f.write(resultado + '\n')  # Escribe cada resultado
    f.close()  # Cierra el archivo

if __name__ == '__main__':
    limpiar()#limpiar la terminal
    secuencias = leer_datos('datos.txt') #datos de entrada
    cimas = cimas_seq(secuencias)
    escribir_cimas('cimas.txt', cimas)
