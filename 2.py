# Función para calcular la media de las dos mejores marcas
def calcular_media(mejores_tiempos):
    return sum(mejores_tiempos[:2]) / 2

# Función para calcular las diferencias de tiempo con los récords
def calcular_diferencias(media, record_olimpico, record_mundial):
    diferencia_olimpico = media - record_olimpico
    diferencia_mundial = media - record_mundial
    return diferencia_olimpico, diferencia_mundial

# Función principal para procesar los archivos y generar las salidas
def procesar_marcas(archivo_entrada, archivo_salida, record_olimpico, record_mundial):
    with open(archivo_entrada, 'r') as archivo:
        lineas = archivo.readlines()
        tiempos = []

        for linea in lineas[3:]:  # Ignorar las primeras 3 líneas
            tiempo = float(linea.split('-')[1].strip())
            tiempos.append(tiempo)

        # Ordenar los tiempos de menor a mayor
        tiempos.sort()

        # Calcular la media de las dos mejores marcas
        media = calcular_media(tiempos)

        # Calcular las diferencias con los récords
        diferencia_olimpico, diferencia_mundial = calcular_diferencias(media, record_olimpico, record_mundial)

        # Escribir los resultados en el archivo de salida
        with open(archivo_salida, 'w') as salida:
            salida.write(f"Año  Atleta               Time(s)\n")
            salida.write(f"2009 wr {record_mundial:.2f}\n")
            salida.write(f"2012 wo {record_olimpico:.2f}\n")
            salida.write(f"2024 1 {tiempos[0]:.2f}\n")
            salida.write(f"2024 2 {tiempos[1]:.2f}\n")
            salida.write(f"2024 wr Diferencia media de tiempo {diferencia_mundial:.2f}\n")
            salida.write(f"2024 wo Diferencia media de tiempo {diferencia_olimpico:.2f}\n")

if __name__ == "__main__":
    # Procesar las marcas de 100m
    procesar_marcas('wr100.txt', 'record100.txt', 9.63, 9.58)

    # Procesar las marcas de 200m
    procesar_marcas('wr200.txt', 'record200.txt', 19.30, 19.19)
