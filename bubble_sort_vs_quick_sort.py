import time
import random

#Algoritmo de ordenamiento Bubble Sort
def bubble_sort(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):                    #Recorre la lista desde el inicio hasta el penúltimo elemento no ordenado
            if lista[j] > lista[j + 1]:                  #Si el elemento actual es mayor que el siguiente
                lista[j], lista[j + 1] = lista[j + 1], lista[j]  #Intercambia los elementos
    return lista

#Algoritmo de ordenamiento Quick Sort (versión recursiva)
def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    pivote = lista[0]                                    #Se elige el primer elemento como pivote
    menores = [x for x in lista[1:] if x <= pivote]      #Lista de elementos menores o iguales al pivote
    mayores = [x for x in lista[1:] if x > pivote]       #Lista de elementos mayores al pivote
    return quick_sort(menores) + [pivote] + quick_sort(mayores)  #Ordena recursivamente y combina

#Tamaños de entrada a evaluar
tamaños = [100, 500, 1000, 2000, 3000]

#Se mide una sola vez por cada tamaño
for n in tamaños:
    lista_original = random.sample(range(n * 10), n)     #Lista aleatoria de n elementos sin repetir

    lista1 = lista_original.copy()                        #Copia para Bubble Sort
    lista2 = lista_original.copy()                        #Copia para Quick Sort

    print(f"\nTamaño de entrada: {n}")

    #Medición de tiempo para Bubble Sort
    inicio = time.time()
    bubble_sort(lista1)
    fin = time.time()
    tiempo_bubble = fin - inicio
    print(f"  Tiempo Bubble Sort: {tiempo_bubble:.8f} segundos")

    #Medición de tiempo para Quick Sort
    inicio = time.time()
    quick_sort(lista2)
    fin = time.time()
    tiempo_quick = fin - inicio
    print(f"  Tiempo Quick Sort:  {tiempo_quick:.8f} segundos")
