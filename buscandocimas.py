# autores: daniel navarrete, alvaro
import os

# función para limpiar la terminal en un sistema operativo windows
def limpiar():
    if os.name == "positx":
        os.system('clear') # para Mac, Linux
        
    else:    
        os.system('cls')  #  para Windows

# función para leer datos desde un archivo y retorna una lista de secuencias
# cada secuencia es una lista de enteros y termina con un 0
def leer_datos(ruta):
    ent = open(ruta, 'r')          # abrir archivo de entrada
    lineas = ent.readlines()        # leer todas las líneas del archivo
    ent.close()                     # cerrar archivo de entrada

    secuencias = []               # lista que almacenará todas las secuencias
    secuencia_actual = []          # secuencia temporal para recolectar números
    
    for linea in lineas:
        if linea.strip():           # saltar líneas en blanco
            numeros = linea.split()  # dividir la línea en partes
            for num in numeros:
                num = int(num)       # convertir cada número a entero
                if num == 0:
                    if secuencia_actual:           # si la secuencia no está vacía
                        secuencias.append(secuencia_actual)
                        secuencia_actual = []      # reiniciar secuencia
                else:
                    secuencia_actual.append(num)   # añadir número a secuencia actual

    if secuencia_actual:             # añadir última secuencia si no termina en 0
        secuencias.append(secuencia_actual)

    return secuencias

# función para encontrar las cimas en una lista de secuencias
# cada cima es un punto más alto que sus vecinos y cumple condiciones dadas
def cimas_seq(secuencias):
    resultados = []                 # lista de resultados para todas las secuencias

    for sec in secuencias:
        n = len(sec)                # longitud de la secuencia actual
        i = 0                       # índice para recorrer la secuencia
        while i < n:
            # verificar si el punto actual es el inicio de una cima
            if i > 0 and i < n - 1 and sec[i] > sec[i - 1] and sec[i] >= sec[i + 1]:
                inicio = i           # marcar el inicio de la cima
                # encontrar longitud de la cima
                while i < n - 1 and sec[i] == sec[i + 1]:
                    i += 1
                # confirmar si la cima cumple las condiciones
                if i < n - 1 and sec[inicio] > sec[i + 1]:
                    longitud = i - inicio + 1
                    resultados.append(f"{inicio + 1} {longitud}")  # formato de salida

            i += 1                   # incrementar índice
        resultados.append("***")      # marcar fin de la secuencia en el archivo de salida

    return resultados

# función para escribir las cimas encontradas en un archivo de salida en el formato adecuado
def escribir_cimas(salida, resultados):
    f = open(salida, 'w')            # abrir archivo de salida
    for resultado in resultados:
        f.write(resultado + '\n')     # escribir cada resultado en una nueva línea
    f.close()                         # cerrar archivo de salida

# ejecución del programa principal
if __name__ == '__main__':
    limpiar()                          # limpiar la terminal antes de ejecutar
    secuencias = leer_datos('datos.txt')  # leer secuencias desde archivo de entrada
    cimas = cimas_seq(secuencias)         # encontrar cimas en las secuencias leídas
    escribir_cimas('cimas.txt', cimas)    # escribir cimas en el archivo de salida
    