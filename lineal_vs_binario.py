import time
import random

#Función de búsqueda lineal
def busqueda_lineal(lista, objetivo):
    for i in range(len(lista)):           #Recorre la lista desde el inicio hasta el final
        if lista[i] == objetivo:          #Si encuentra el objetivo, devuelve su índice
            return i
    return -1                             #Si no lo encuentra, devuelve -1

#Función de búsqueda binaria (requiere lista ordenada)
def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:                              #Mientras haya elementos para buscar
        medio = (inicio + fin) // 2                   #Calcula el punto medio
        if lista[medio] == objetivo:                  #Si lo encuentra, retorna su posición
            return medio
        elif lista[medio] < objetivo:                 #Si el valor medio es menor al objetivo
            inicio = medio + 1                        #Busca en la mitad derecha
        else:
            fin = medio - 1                           #Busca en la mitad izquierda
    return -1                                         #Si no lo encuentra, retorna -1

#Tamaños de entrada a evaluar
tamaños = [100, 500, 1000, 5000, 10000, 20000]

#Evaluamos una única vez por cada tamaño de lista
for n in tamaños:
    lista = list(range(n))                            #Lista ordenada de 0 a n-1
    objetivo = random.choice(lista)                   #Elegimos un número al azar dentro de la lista

    print(f"\nTamaño de entrada: {n}")

    #Medición de búsqueda lineal
    inicio = time.time()
    busqueda_lineal(lista, objetivo)
    fin = time.time()
    tiempo_lineal = fin - inicio
    print(f"  Tiempo búsqueda lineal:  {tiempo_lineal:.8f} segundos")

    #Medición de búsqueda binaria
    inicio = time.time()
    busqueda_binaria(lista, objetivo)
    fin = time.time()
    tiempo_binaria = fin - inicio
    print(f"  Tiempo búsqueda binaria: {tiempo_binaria:.8f} segundos")
