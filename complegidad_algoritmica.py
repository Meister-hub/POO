# 1 Vamos a medir el tiempo en que tarda un algoritmo

import time 

# Factorial ITERATIVO
def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1

    return respuesta

# Factorial RECURSIVO
def factorial_r(n):
    if n == 1:
        return 1

    return n * factorial (n - 1)

# Punto de entrada

if __name__ == '__main__':
    n = 1000000000000

    comienzo = time.time()  #Estamos ejecutando el módulo time y adentro tiene una función que se llama time
    #print(factorial(n))
    final = time.time()
    print(final - comienzo)

    comienzo = time.time()
    #print(factorial_r(n))
    final = time.time()
    print(final - comienzo)