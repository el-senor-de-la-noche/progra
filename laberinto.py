m1 = [
    ['E', 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 'S']
]

# 1. Función para verificar si una posición es válida
def es_valido(matriz, x, y):
    if x >= 0 and x < len(matriz):
        if y >= 0 and y < len(matriz[0]):
            if matriz[x][y] != 1 and matriz[x][y] != 2:
                return True
    return False

# 2. Función recursiva para buscar el camino
def buscar_camino(matriz, x, y, camino):
    if es_valido(matriz, x, y) == False:
        return False

    if matriz[x][y] == 'S':
        camino.append([x, y])
        return True

    matriz[x][y] = 2  # Marca como visitado
    camino.append([x, y])

    # Movimientos en las 4 direcciones
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

# 3. Función para crear una matriz de solución marcando el camino encontrado
def crear_matriz_solucion(matriz, camino):
    MS = []
    fila = 0
    while fila < len(matriz):
        nueva_fila = []
        columna = 0
        while columna < len(matriz[0]):
            if matriz[fila][columna] == 0:
                nueva_fila.append(1)
            else:
                nueva_fila.append(matriz[fila][columna])
            columna = columna + 1
        MS.append(nueva_fila)
        fila = fila + 1

    for paso in camino:
        x = paso[0]
        y = paso[1]
        MS[x][y] = 0
    return MS

# 4. Función principal para resolver el laberinto
def resolver(matriz):
    camino = []
    entrada_x = -1
    entrada_y = -1

    fila = 0
    while fila < len(matriz):
        columna = 0
        while columna < len(matriz[0]):
            if matriz[fila][columna] == 'E':
                entrada_x = fila
                entrada_y = columna
            columna = columna + 1
        fila = fila + 1

    if entrada_x == -1 or entrada_y == -1:
        print("No se encontró la entrada.")
        return

    if buscar_camino(matriz, entrada_x, entrada_y, camino):
        print("Camino encontrado:", camino)
        matriz_solucion = crear_matriz_solucion(matriz, camino)
        
        fila = 0
        while fila < len(matriz_solucion):
            print(matriz_solucion[fila])
            fila = fila + 1
    else:
        print("No hay camino de salida.")

resolver(m1)
