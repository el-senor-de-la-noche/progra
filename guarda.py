#lo que necesito es buscar cuales son los numeros mas altos que sus numeros a los lados 
#necesito comparar si el numero es mayor que el anterior y es mayor o igual al siguiente


def encontrar_mayor_rep(lista): #me falta un if
    len_lis = len(lista)
    cimas = []
    contador = 1

    while contador < len_lis - 1:  #el menos 1 es para que las comparacion queden siempre dentro de la lista
        if lista[contador] > lista[contador - 1] and lista[contador] > lista[contador + 1]:
            cimas.append(lista[contador])
            contador = contador + 1
            
        elif lista[contador] > lista[contador - 1] and lista[contador] == lista[contador + 1]:
            while contador < len_lis - 1 and lista[contador] == lista[contador + 1]:
                contador = contador + 1
            cimas.append(lista[contador])
            contador = contador + 1
        else:
            contador = contador + 1

    return cimas


def buscar_pos(lista, cimas):
    contador_2 = 0
    pos = []
    while contador_2 < len(lista):
        omg = lista.index(cimas[contador_2])
        pos.append(omg)
        omg = 0
        contador_2 = contador_2 + 1
    return pos


def buscar_rep(lista, cimas):
    contador_2 = 0
    rep = []
    while contador_2 < len(lista):
        omg = lista.count(cimas[contador_2])
        rep.append(omg)
        omg = 0
        contador_2 = contador_2 + 1
    return rep
#me falta una funcion chica

if __name__ == "__main__":
    lista = [2, 6, 7, 9, 4, 2, 3, 5, 5, 4, 0]
    cimas = encontrar_mayor_rep(lista)
    rep = buscar_pos(lista, cimas)
    print(cimas)
    print(rep)