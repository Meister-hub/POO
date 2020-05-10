# ABstraccion
#
# Hace enfocarnos en la información reelevante
# En un elevador no te preocupas por como funcionan las poleas
# Podemos usar varios métodos privados y públicos
# 
# No tenemos que preoucparnos de la estructura interea 

# Clase que genera abstracciones


class Lavadora:
    def __init__(self):
        pass

    def lavar(self, temperatura = 'fria'):
        self._llenar_tanque_de_agua(temperatura)
        self._anadir_jabon()
        self._lavar()
        self._centrifugar()

    def _llenar_tanque_de_agua(self, temperatura):
        print(f'Llenar el tanque con algua {temperatura}')

    def _anadir_jabon(self):
        print('Añadiendo jabon')

    def _lavar(self):
        print('Lavando la ropa')

    def _centrifugar(self):
        print('Centrifugando la ropa')

if __name__ == '__main__':
    lavadora = Lavadora()
    lavadora.lavar()


