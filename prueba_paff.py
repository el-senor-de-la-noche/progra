#Autor = Daniel Eliseo Navarrete Silva --- seccion 2 ---- Prueba PAF
import os
def limpiar():
    #funcion que borra y/o limpia la pantalla dependiendo del sistema operativo
    if os.name == "positx":
        os.system("clear")
    else:
        
        os.system("cls")
    #retornamos a la biblioteca "os"
    return os
def lectura():
    #aqui estan los primeros puntos
    x1 = float(input("ingrese coordenada x del primer punto: "))
    y1 = float(input("ingrese coordenada y del primer punto: "))
    z1 = float(input("ingrese coordenada z del primer punto: "))
    #aqui estan los segundos puntos
    x2 = float(input("ingrese coordenada x del segundo punto: "))
    y2 = float(input("ingrese coordenada y del segundo punto: "))
    z2 = float(input("ingrese coordenada z del segundo punto: "))
    #retornamos a los puntos ordenados
    return [x1,y1,z1,x2,y2,z2]
def diferencia(datos):
    #se muestra el calculo de la diferencia entre los 2 puntos[(x1-x2),(y1-y2),(z1-z2)]
    diferencia = [(datos[0] - datos[3]), (datos[1]-datos[4]), (datos[2]-datos[5])]
    # se retorna a la diferencia de puntos
    return diferencia 
def vectorial(datos):
    #se muetra el calculo del vectorial [(x1,y1,z1)*(x2,y2,z2)]
    vectorial = [(datos[1]*datos[5])-(datos[2]*datos[4]), (datos[2]*datos[3])-(datos[0]*datos[5]), (datos[0]*datos[4])-(datos[1]*datos[3])]
    #retornamos a el calculo de vectoriales de los puntos
    return vectorial
    
def mostrar(datos, diferencia, vectorial):
    #aqui esta la salida que se pide
    print("resultados:")
    print(f"primer punto = {[datos[0],datos[1],datos[2]]}")
    print(f"segundo punto = {[datos[3], datos[4],datos[5]]}")
    print(f"diferencia = {diferencia}")
    print(f"vetorial = {vectorial}")
    pass
if __name__ == "__main__":
    limpiar()
    datos = lectura()
    diferencia = diferencia(datos)
    vectorial1 = vectorial(datos)
    mostrar(datos, diferencia, vectorial1)
    

