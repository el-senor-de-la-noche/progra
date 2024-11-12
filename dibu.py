# Tamaño de la pantalla
TAMANIO = 16

# Pantalla inicializada completamente blanca ('o')
pantalla = [['o'] * TAMANIO for _ in range(TAMANIO)]

def lee_archivo(nombre_archivo):
    """Lee los comandos desde un archivo de entrada."""
    archivo = open(nombre_archivo, 'r')
    lineas = []
    while True:
        linea = archivo.readline()
        if linea == '':
            break
        lineas.append(linea.strip().split())
    archivo.close()
    return lineas

def pintar_area(x0, y0, x1, y1):
    """Pinta un área de la pantalla (x0, y0) a (x1, y1) con 'x'."""
    i = y0
    while i < y1:
        j = x0
        while j < x1:
            pantalla[i][j] = 'x'
            j += 1
        i += 1

def evalua(movi):
    if len(movi) >= 1 and len(movi)<= 5:
        return True
    else:
        return False

def mod_limites(movi, fi, ff, ci, cf):
    """Modifica los límites según el comando recibido para seleccionar el área adecuada."""
    df = (ff - fi + 1)//2
    dc = (cf - ci + 1)//2
    if movi == '1':
        ff = ff - df
        cf = cf - df
    elif movi == '2':
        ff = ff - df
        ci = ci + dc
    elif movi == '3':
        fi = fi + df
        ci = ci + dc
    else:
        fi = fi + df
        cf = cf - dc
    return [fi, ff, ci, cf]


def genera_archivo(nombre_archivo):
    """Guarda la pantalla en un archivo de salida."""
    archivo = open(nombre_archivo, 'w')
    i = 0
    while i < TAMANIO:
        j = 0
        linea = ''
        while j < TAMANIO:
            linea += pantalla[i][j]
            j += 1
        archivo.write(linea + '\n')
        i += 1
    archivo.close()

def proceso(movimientos):
    """Procesa una lista de comandos."""
    for comando in movimientos:
        evalua(comando)

if __name__ == '__main__':
    # Leer movimientos desde "dibu_ent.txt" y procesarlos
    movimientos = lee_archivo('dibu_ent.txt')
    proceso(movimientos)
    # Generar el archivo de salida "dibu_sal.txt"
    genera_archivo('dibu_sal.txt')
