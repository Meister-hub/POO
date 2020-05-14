#   -----  Clase -----
c =  7
t = 21

class Instrumento:
    def __init__(self, cuerdas, trastes):
        self.cuerdas = cuerdas
        self.trastes = trastes
      
    def tocar(self):
        print(f'Estos son los instrumentos de cuerdas que se tocar')

class Guitarra_Electrica(Instrumento):
    def __init__(self, cuerdas, trastes):
        super().__init__(cuerdas,trastes)

    def tocar(self):
        if self.cuerdas <= 8 and self.cuerdas >= 6 and self.trastes <=24 and self.trastes >= 21:
            print(f'Puedo tocar la guitarra eléctrica con {self.cuerdas} cuerdas y {self.trastes} trastes ')
        else:
            print('Pues la guitarra eléctrica no puedo tocar')

class Bajo(Instrumento):
    def __init__(self, cuerdas, trastes):
        super().__init__(cuerdas, trastes)

    def tocar(self):
        if self.cuerdas <= 6 and self.cuerdas >= 4 and self.trastes <=24 and self.trastes >= 21:
            print(f'Puedo tocar el bajo con {self.cuerdas} cuerdas y {self.trastes} trastes ')
        else:
            print('No hay bajos de más de 6 cuerdas')

class Guitarra_Acustica(Instrumento):
    def __init__(self, cuerdas, trastes):
        super().__init__(cuerdas, trastes)

    def tocar(self):
        if self.cuerdas >= 6 and self.trastes >= 12:
            print(f'Puedo tocar la guitarra acústica porque con más de 6 cuerdas y más de 12 trastes')
        else:
            print('La guitarra acústia de mínimo tiene 6 cuerdas')

def main():
    instrumento = Instrumento(6 , 24)
    instrumento.tocar()
    guitarra_electrica = Guitarra_Electrica(c, t)
    guitarra_electrica.tocar()
    bajo = Bajo (c , t)
    bajo.tocar()
    guitarra_acustica = Guitarra_Acustica (c , t)
    guitarra_acustica.tocar()

if __name__ == '__main__':
    main()