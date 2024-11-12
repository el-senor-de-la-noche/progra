class persona: 
    def  __init__(self, nom):
        self.nombre = nom
    def imprimir(self):
        print('nombre:', self.nombre)

persona1 = persona('hugo')
persona1.imprimir()

persona2 = persona('araya')
persona2.imprimir()



