# Función para leer los datos desde un archivo
def leer_datos(ruta):
    # Abrir el archivo en modo lectura
    archivo = open(ruta, 'r')
    lineas = archivo.readlines()  # Leer todas las líneas del archivo
    archivo.close()  # Cerrar el archivo










    secuencias = []  # Lista para almacenar todas las secuencias
    secuencia_actual = []  # Lista para almacenar la secuencia actual

    # Iterar sobre cada línea del archivo
    for linea in lineas:
        linea = linea.strip()  # Eliminar espacios en blanco al inicio y al final
        if linea != "":  # Ignorar líneas vacías
            numeros = linea.split()  # Separar los números en la línea
            # Convertir cada número a entero
            for numero in numeros:
                numero = int(numero)
                if numero == 0:  # El 0 marca el final de una secuencia
                    if len(secuencia_actual) > 0:  # Evitar secuencias vacías
                        secuencias.append(secuencia_actual)  # Agregar la secuencia a la lista de secuencias
                    secuencia_actual = []  # Reiniciar la secuencia para la próxima
                else:
                    secuencia_actual.append(numero)  # Agregar número a la secuencia actual

    return secuencias  # Retornar la lista de secuencias

# Función para encontrar las cimas en una secuencia
def cimas_s(secuencia):
    cimas = []  # Lista para almacenar las cimas encontradas
    i = 1  # Iniciar desde el segundo elemento (índice 1)

    # Iterar a través de la secuencia hasta el penúltimo elemento
    while i < len(secuencia) - 1:
        j = i  # Inicializar j para buscar subsecuencias

        # Buscar subsecuencia con valores iguales
        while j < len(secuencia) - 1 and secuencia[j] == secuencia[j + 1]:
            j += 1  # Continuar mientras los valores sean iguales
        
        # Verificar si el elemento actual es una cima
        if secuencia[i - 1] < secuencia[i] and secuencia[j] > secuencia[j + 1]:
            # Almacenar la cima como (posición, longitud)
            cimas.append((i + 1, j - i + 1))
        
        i = j + 1  # Avanzar al siguiente número

    return cimas  # Retornar la lista de cimas encontradas

# Función para procesar todas las secuencias y encontrar las cimas
def p_secuencias(secuencias):
    todas_cimas = []  # Lista para almacenar cimas de todas las secuencias
    for secuencia in secuencias:
        cimas = cimas_s(secuencia)  # Encontrar cimas en la secuencia actual
        todas_cimas.append(cimas)  # Agregar las cimas encontradas a la lista
    return todas_cimas  # Retornar todas las cimas

# Función para escribir las cimas en un archivo
def escribir_cimas(cimas, ruta_salida):
    # Abrir el archivo en modo escritura
    archivo = open(ruta_salida, 'w')
    for secuencia in cimas:
        for cima in secuencia:
            # Escribir la posición y longitud de cada cima en el archivo
            archivo.write(str(cima[0]) + " " + str(cima[1]) + "\n")
        archivo.write("***\n")  # Escribir un separador entre secuencias
    archivo.close()  # Cerrar el archivo

# Bloque principal del programa
if __name__ == '__main__':
    secuencias = leer_datos('datos.txt')  # Leer las secuencias del archivo
    cimas = p_secuencias(secuencias)  # Encontrar las cimas
    escribir_cimas(cimas, 'cimas.txt')  # Escribir las cimas en el archivo de salida
