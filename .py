def calcular_media_mejores_tiempos(marcas):
    # Ordenar las marcas en orden ascendente y tomar las dos mejores
    mejores_marcas = sorted(marcas)[:2]
    # Calcular la media de las dos mejores marcas
    media = sum(mejores_marcas) / len(mejores_marcas)
    return media

def calcular_diferencias(media, record_mundial, record_olimpico):
    # Calcular diferencias entre la media y los récords
    diferencia_mundial = media - record_mundial
    diferencia_olimpico = media - record_olimpico
    return diferencia_mundial, diferencia_olimpico

def procesar_archivo(file_name, record_mundial, record_olimpico, output_file):
    with open(file_name, 'r') as file:
        lines = file.readlines()

    # Extraer las marcas de los atletas
    marcas = []
    for line in lines:
        if '2024' in line:
            marca = float(line.split('-')[1].strip())
            marcas.append(marca)
    
    # Calcular la media de las dos mejores marcas
    media = calcular_media_mejores_tiempos(marcas)
    
    # Calcular las diferencias
    diferencia_mundial, diferencia_olimpico = calcular_diferencias(media, record_mundial, record_olimpico)
    
    # Escribir los resultados en el archivo de salida
    with open(output_file, 'w') as output:
        output.write(f"Año  Atleta               Time(s)\n")
        output.write(f"2024 1 {sorted(marcas)[0]}\n")
        output.write(f"2024 2 {sorted(marcas)[1]}\n")
        output.write(f"2024 wr Diferencia media de tiempo con el récord mundial: {diferencia_mundial:.2f}\n")
        output.write(f"2024 wo Diferencia media de tiempo con el récord olímpico: {diferencia_olimpico:.2f}\n")

if __name__ == "__main__":
    # Datos para el archivo de 100m
    record_mundial_100 = 9.58
    record_olimpico_100 = 9.63
    procesar_archivo( 'wr100.txt')

    # Datos para el archivo de 200m
    record_mundial_200 = 19.19
    record_olimpico_200 = 19.30
    procesar_archivo( 'wr200.txt')
