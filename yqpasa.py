# Definición de la matriz
M1 = [
    ["E", 0, 1, 1, 1],
    [1, 0, 0, 0, 1],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 0, 1],
    [1, 1, 1, 0, "S"]
]

# Función para verificar si una posición es válida
def es_valido(matriz, x, y):
    if x >= 0 and x < len(matriz):
        if y >= 0 and y < len(matriz[0]):
            if matriz[x][y] != 1 and matriz[x][y] != 2:  # 2 indica que la celda ha sido visitada
                return True
    return False

# Función recursiva para buscar el camino
def buscar_camino(matriz, x, y, camino):
    if es_valido(matriz, x, y) == False:  # Verifica si la posición es válida
        return False

    if matriz[x][y] == "S":  # Si se encuentra la salida
        camino.append([x, y])  # Agrega la salida al camino
        return True

    matriz[x][y] = 2  # Marca la celda como visitada
    camino.append([x, y])  # Agrega la celda al camino

    # Movimientos en las 4 direcciones: abajo, arriba, derecha, izquierda
    if buscar_camino(matriz, x + 1, y, camino):  # Abajo
        return True
    if buscar_camino(matriz, x - 1, y, camino):  # Arriba
        return True
    if buscar_camino(matriz, x, y + 1, camino):  # Derecha
        return True
    if buscar_camino(matriz, x, y - 1, camino):  # Izquierda
        return True

    camino.pop()  # Deshace el paso si no hay salida
    return False

# Función para crear la matriz solución
def crear_matriz_solucion(matriz, camino):
    MS = []
    for fila in matriz:
        nueva_fila = []
        for celda in fila:
            if celda == 0:
                nueva_fila.append(1)  # Marca los no-caminos como 1
            else:
                nueva_fila.append(celda)  # Copia el valor original (E, S o 1)
        MS.append(nueva_fila)

    for paso in camino:
        x = paso[0]
        y = paso[1]
        MS[x][y] = 0  # Marca el camino como 0
    return MS

# Función principal para resolver el laberinto
def resolver(matriz):
    camino = []
    entrada_x = -1
    entrada_y = -1

    # Busca la posición de la entrada 'E'
    fila = 0
    while fila < len(matriz):
        columna = 0
        while columna < len(matriz[0]):
            if matriz[fila][columna] == "E":
                entrada_x = fila
                entrada_y = columna
            columna = columna + 1
        fila = fila + 1

    # Verifica si se encontró la entrada
    if entrada_x == -1 or entrada_y == -1:
        print("No se encontró la entrada.")
        return

    # Intenta encontrar el camino desde la entrada
    if buscar_camino(matriz, entrada_x, entrada_y, camino):
        print("Camino encontrado:", camino)
        matriz_solucion = crear_matriz_solucion(matriz, camino)
        print("Matriz solución:")
        fila = 0
        while fila < len(matriz_solucion):
            print(matriz_solucion[fila])
            fila = fila + 1
    else:
        print("La matriz no presenta camino de salida.")

# Ejecutar el algoritmo
resolver(M1)
