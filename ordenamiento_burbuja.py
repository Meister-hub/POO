import random 

def ordenamiento_de_burbuja(lista):
    n = len(lista)

    for i in range(n):
        for j in range(0, n - 1):
        
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista [j + 1], lista[j] 
                print(f'Ordenamiento burbuja de lista:     {lista}')
    return lista


if __name__ == '__main__':

    tamano_de_lista = int(input('De que tamaño es la lista? '))

    lista = [random.randint(0, 15) for i  in range(tamano_de_lista)]
    print(f'Lista inicial:   {lista}')

    lista_ordenada = ordenamiento_de_burbuja(lista)
    print(f'Lista ordenada: {lista_ordenada}')