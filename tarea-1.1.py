import os
#b
estudiantes = {
    "Ana": [8, 9, 7, 10],
    "Julia": [8, 9, 7, 10],
    "Adriana": [8, 9, 7, 10],
    "Benjamín": [8, 9, 7, 10],
    "Diego": [8, 9, 7, 10],
    "Juan": [8, 9, 7, 10],
    "María": [9, 10, 9, 8],
    "Pedro": [7, 8, 6, 9]
}
#funcion para limpiar
def limpiar():
    if os.name == "posix":
        os.system("clear")
    else:
        os.system("cls")
#funcion para calcular el promedio de los estudiantes
def promedios(calificaciones):
    return sum(calificaciones)/len(calificaciones)
#funcion para capturar la nota maxima
def nota_maxima(calificaciones):
    return max(calificaciones)
#funcion para capturar la nota minima
def nota_minima(calificaciones):
    return min(calificaciones)
#funcion para mostrar en orden los resultados
def mostrar(estudiantes):
    print("Estudiante                                             Promedio     Mínima     Máxima")
    print("_______________________________________________________________________________________")
    for estudiante, calificaciones in estudiantes.items():
        promedio = promedios(calificaciones)
        maxima = nota_maxima(calificaciones)
        minima = nota_minima(calificaciones)
        print(f"El promedio de {estudiante:<15} es:                       {promedio:.2f}         {minima}         {maxima}")
    print()



if __name__ == "__main__":
    limpiar()
    mostrar(estudiantes)
