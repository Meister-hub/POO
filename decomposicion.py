class Automovil:

    def __init__ (self, modelo, marca, color):
        self.modelo = modelo
        self.marca = marca
        self.color = color
        # Variables privadas
        self.estado = 'en reposo'   
        self.motor = Motor(cilindros = 4)

    def acelerar(self, tipo = 'rapida'):

        if tipo == 'rapida':
            self.motor_inyecta_gasolina(10)
            print(f'La aceleración es tipo {tipo}') 

        else:
            self.motor_inyecta_gasolina(3)

        self.estado = 'movimiento'
         
class Motor:
    
    def __init__ (self, cilindros, tipo = 'gasolina'):    #tipo = default keyword

        self.cilindros = cilindros
        self.tipo = tipo
        #Variable interna
        self.temperatura = 0

    def inyecta_gasolina (self, cantidad):
        pass


  