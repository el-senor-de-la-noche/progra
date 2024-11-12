# función para leer los datos del archivo "camino.txt"
def leer_datos():
    archivo = open("camino.txt", "r")
    # lee las dimensiones del tablero
    linea = archivo.readline().strip().split()
    M = int(linea[0])
    N = int(linea[1])
    
    # lee el contenido del tablero
    tablero = []
    for _ in range(M):
        tablero.append(archivo.readline().strip())
    
    # lee la palabra a buscar
    palabra = archivo.readline().strip()
    
    archivo.close()
    return M, N, tablero, palabra

# función para encontrar las coordenadas de cada letra de la palabra en el tablero
def encontrar_coordenadas(tablero, M, N, palabra):
    ruta = []
    for letra in palabra:
        for i in range(M):
            for j in range(N):
                if tablero[i][j] == letra:
                    # guarda la posición en el formato especificado
                    ruta.append(str(i + 1) + " " + str(j + 1))
                    break
            else:
                continue
            break
    return ruta

# función para escribir la ruta en el archivo "ruta.txt"
def escribir_ruta(ruta):
    archivo = open("ruta.txt", "w")
    for linea in ruta:
        archivo.write(linea + "\n")
    archivo.close()

# función principal
if __name__ == "__main__":
    M, N, tablero, palabra = leer_datos()
    ruta = encontrar_coordenadas(tablero, M, N, palabra)
    escribir_ruta(ruta)
