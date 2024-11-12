import os
K = 273.15
P = 100000

def limpiar():
    if os.name == 'posix':
        os.system('clear')
    else:
        os.system('cls')

def temperaturas_en_c():
    print('Coloque 5 temperaturas distintas:', '\n')
    t1 = float(input('Temperatura °C: '))
    t2 = float(input('Temperatura °C: '))
    t3 = float(input('Temperatura °C: '))
    t4 = float(input('Temperatura °C: '))
    t5 = float(input('Temperatura °C: '))
    print('_____________________________________________')
    return [t1, t2, t3, t4, t5]

def presiones():
    print('Escriba 5 presiones distintas a continuación:', '\n')
    p1 = float(input('Presión Bar: '))
    p2 = float(input('Presión Bar: '))
    p3 = float(input('Presión Bar: '))
    p4 = float(input('Presión Bar: '))
    p5 = float(input('Presión Bar: '))
    print('_____________________________________________')
    return [p1, p2, p3, p4, p5]

def transformar_a_F(datos):
    f = [float(t * (9/5) + 32) for t in datos]
    return f

def transformar_a_K(datos):
    k = [float(t + K) for t in datos]
    print('_____________________________________________')
    return k

def pascal(presion):
    ps = [float(p * P) for p in presion]
    print('_____________________________________________')
    return ps

def Kpascal(presion):
    kpa = [float(p * 100) for p in presion]
    print('_____________________________________________')
    return kpa

def salida(datos, presion, datos_F, datos_K, presion_Pascal, presion_KPa):
    print("\n--- Resultados ---")
    print(f"Temperaturas (°C): {datos}")
    print(f"Temperaturas (°F): {datos_F}")
    print(f"Temperaturas (K): {datos_K}")
    print(f"Presiones (Bar): {presion}")
    print(f"Presiones (Pascal): {presion_Pascal}")
    print(f"Presiones (kPa): {presion_KPa}")

if __name__ == '__main__':
    limpiar()
    datos = temperaturas_en_c()
    presion = presiones()
    
    datos_F = transformar_a_F(datos)
    datos_K = transformar_a_K(datos)
    presion_Pascal = pascal(presion)
    presion_KPa = Kpascal(presion)
    
    salida(datos, presion, datos_F, datos_K, presion_Pascal, presion_KPa)
