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

class Electronica:

    def __init__ (self, luz_delantera, luz_trasera, dir_der, dir_izq):
        self.luz_delantera = luz_delantera
        self.luz_trasera = luz_trasera
        self.dir_der = dir_der
        self.dir_izq = dir_izq
        self.nivel_de_bateria = 80

    def luces(self, noche = True):
        if noche == True:
            self.luz_delantera = True
            self.luz_trasera = True
        else:
            self.luz_delantera = False
            self.luz_trasera = False







  