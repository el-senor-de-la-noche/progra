#autor: Daniel Navarrete
def datos():
    lado_1 = int(input("ingrese su lado 1: "))
    lado_2 = int(input("ingrese su lado 2: "))
    lado_3 = int(input("ingrese su lado 3: "))
    return lado_1, lado_2, lado_3
def comprobar(l1, l2, l3):
    if l1 + l2 > l3 or l1 + l3 > l2 or l2+l3>l1:
        if l1==l2==l3:
            tipo = 'Equilatero'
        elif l1 == l2 or l2 == l3 or l3 == l1:
            tipo = 'Isosceles'
        else:
            tipo = 'escaleno'
    return tipo

if __name__ == '__main__':
    l1, l2,l3 = datos()
    comprobar()