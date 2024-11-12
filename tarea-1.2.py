def leer(productos_file, precios_file, ajustes_file):
    """Carga los datos de los archivos de productos, precios y ajustes."""
    productos = []
    precios = []
    ajustes = []
    
    try:
        with open(productos_file, 'r', encoding='UTF-8') as f:
            next(f)  # Ignorar la primera línea si es un encabezado
            productos = [line.strip() for line in f if line.strip()]

        with open(precios_file, 'r', encoding='UTF-8') as g:
            next(g)  # Ignorar la primera línea si es un encabezado
            for line in g:
                try:
                    datos = line.strip().split()
                    precios.append(float(datos[1]))  # El segundo valor es el precio
                except (ValueError, IndexError):
                    print(f"Advertencia: No se pudo convertir la línea '{line.strip()}' a float en precios.txt")

        with open(ajustes_file, 'r', encoding='UTF-8') as h:
            next(h)  # Ignorar la primera línea si es un encabezado
            for line in h:
                try:
                    datos = line.strip().split()
                    ajuste = datos[1].replace('(', '').replace(')', '')  # Remover paréntesis
                    ajustes.append(float(ajuste))
                except (ValueError, IndexError):
                    print(f"Advertencia: No se pudo convertir la línea '{line.strip()}' a float en ajuste.txt")

    except FileNotFoundError as e:
        print(f"Error: {e}")
        return None, None, None

    return productos, precios, ajustes

def calcular_pventa(precio, ajuste):
    """Calcula el precio de venta final."""
    return precio * (1 - ajuste / 100)

def mostrar_resultados(productos, precios, ajustes, output_file):
    """Procesa y guarda los resultados en un archivo de texto."""
    if not productos or not precios or not ajustes:
        print("No se pudieron cargar los datos correctamente.")
        return

    if len(productos) != len(precios) or len(productos) != len(ajustes):
        print("Error: El número de productos, precios y ajustes no coincide.")
        return

    total = 0
    
    with open(output_file, 'w', encoding='UTF-8') as f:
        f.write(f"{'Código':<14}{'Producto':<25}{'Precio':<10}{'Ajuste':<10}{'Pventa':<10}\n")
        f.write("-" * 63 + "\n")
        
        for i in range(len(productos)):
            producto = productos[i]
            precio = precios[i]
            ajuste = ajustes[i]
            pventa = calcular_pventa(precio, ajuste)
            
            f.write(f"{i+1:<8}{producto:<25}{precio:<10.2f}{ajuste:<10.2f}{pventa:<10.2f}\n")
            total += pventa
        
        f.write("-" * 63 + "\n")
        f.write(f"{'Total:':<53}{total:.2f}\n")

if __name__ == "__main__":
    productos_file = r'C:\Users\navar\OneDrive\Escritorio\materias\programas\laboratorio\python\PROGRAMACION\a\productos.txt'
    precios_file = r'C:\Users\navar\OneDrive\Escritorio\materias\programas\laboratorio\python\PROGRAMACION\a\precios.txt'
    ajustes_file = r'C:\Users\navar\OneDrive\Escritorio\materias\programas\laboratorio\python\PROGRAMACION\a\ajuste.txt'
    output_file = r'C:\Users\navar\OneDrive\Escritorio\materias\programas\laboratorio\python\PROGRAMACION\a\resultados.txt'

    productos, precios, ajustes = leer(productos_file, precios_file, ajustes_file)
    mostrar_resultados(productos, precios, ajustes, output_file)
