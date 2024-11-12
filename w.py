#Autor: Daniel Navarrete
def potencia_t(consumo_pc, consumo_cafetera, consumo_hielera):
    return consumo_pc * 15 + consumo_cafetera + consumo_hielera

def funcion_imprime_consumo_amperes(potencia_total):
    tension = 220
    consumo_amperes = potencia_total / tension
    print(f"Consumo total en amperios: {consumo_amperes} A")

if __name__ == "__main__":
    consumo_computadoras = 800
    consumo_cafetera = 500
    consumo_hielera = 500
    potencia_total_consumida = potencia_t(consumo_computadoras, consumo_cafetera, consumo_hielera)
    print(f"Consumo total en watts: {potencia_total_consumida} W")
    funcion_imprime_consumo_amperes(potencia_total_consumida)
