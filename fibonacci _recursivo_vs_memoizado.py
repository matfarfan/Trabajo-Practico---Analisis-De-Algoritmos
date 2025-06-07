import time

#Versión recursiva de Fibonacci (sin optimización)
def fibonacci_recursivo(n):
    if n <= 1:
        return n
    return fibonacci_recursivo(n - 1) + fibonacci_recursivo(n - 2)

#Versión optimizada con memoización (almacena resultados ya calculados)
memo = {}  	#Diccionario para guardar resultados
def fibonacci_memo(n):
    if n in memo:                         #Si ya está calculado, se retorna directamente
        return memo[n]
    if n <= 1:
        memo[n] = n
    else:
        memo[n] = fibonacci_memo(n - 1) + fibonacci_memo(n - 2)
    return memo[n]

#Valores de entrada para evaluar
valores = [10, 20, 25, 30, 35]

#Se mide una sola vez por cada valor
for n in valores:
    print(f"\nFibonacci de n = {n}")

    #Medición de tiempo para versión recursiva
    inicio = time.time()
    resultado_rec = fibonacci_recursivo(n)
    fin = time.time()
    tiempo_rec = fin - inicio
    print(f"  Recursivo:  {resultado_rec} | Tiempo: {tiempo_rec:.8f} segundos")

    #Medición de tiempo para versión memoizada
    inicio = time.time()
    resultado_memo = fibonacci_memo(n)
    fin = time.time()
    tiempo_mem = fin - inicio
    print(f"  Memoizado: {resultado_memo} | Tiempo: {tiempo_mem:.8f} segundos")
