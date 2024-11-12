TAMANIO = 16

# Pantalla inicializada completamente blanca ('o')
pantalla = [['o'] * TAMANIO for _ in pantalla]



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

def evalua(movi):
    if len(movi) >= 1 and len(movi)<= 5:
        return True
    else:
        return False

def mod_limites(movi, fi, ff, ci, cf):
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

def proceso(movimientos):
    """Procesa una lista de comandos."""
    i = 0
    while i < len(movimientos):
        evalua(movimientos[i])
        i += 1

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

if __name__ == '__main__':
    movimientos = lee_archivo('dibu_ent.txt')
    salida = proceso(movimientos)
    genera_archivo('dibu_sal.txt')