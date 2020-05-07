#Definicion
class Persona:
    
    def __init__ (self, nombre, edad):  #Constructor Variables de instancia 
        self.nombre = nombre
        self.edad = edad
    
    def saluda (self, otra_persona):
        return f'Hola {otra_persona.nombre}, me llamo {self.nombre} y tengo {self.edad} años.'

#Uso

david = Persona ('David', 35)
ricardo = Persona ('Ricardo', 32)

nombre = int{input()}

print(david.saluda(ricardo))
'Hola Erika, me llamo David'