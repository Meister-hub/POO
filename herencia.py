 # Esta es mi súper clase
class Rectangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

# Esta es mi clase, en python usas como super clase metiendolo en los parentesis
#La clase cuadrado, extiende al rectanulo

class Cuadrado(Rectangulo):   
    def __init__ (self, lado):
        super().__init__(lado, lado )     #Super: Obtiene una referencia directa de la superclase


# ---------- Creo otra clase    -----

class Triangulo(Rectangulo):
    def __init__ (self, base, altura): 
        super().__init__(base, altura)

if __name__ == '__main__':
    rectangulo = Rectangulo(base = 3, altura = 4)
    print(f'El área del rectángulo es {rectangulo.area()}')

    cuadrado = Cuadrado(lado = 5)
    print(f'El área del cuadrado es: {cuadrado.area()}')

    triangulo = Triangulo(base =2, altura = 2)
    print(f'El área del triangulo es : {triangulo.area() // 2}')