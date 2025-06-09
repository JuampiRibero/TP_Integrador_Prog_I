import random
import sys
import time

sys.setrecursionlimit(2000)

def generar_estructuras(n):
    datos = list(range(n))

    estructura_lista = datos
    estructura_set = set(datos)
    estructura_diccionario = {i: datos[i] for i in range(n)}

    elemento_existente = random.choice(datos)
    elemento_no_existente = -1

    return estructura_lista, estructura_set, estructura_diccionario, elemento_existente, elemento_no_existente

def busqueda_recursiva(list, elemento, index=0):
    if index >= len(list):
        return False
    if list[index] == elemento:
        return True
    return busqueda_recursiva(list, elemento, index + 1)

def medir_memoria(estructura):
    return sys.getsizeof(estructura) / (1024 * 1024)

def evaluar_busqueda(estructura, elemento, tipo_estructura):
    def buscar():
        if tipo_estructura == "list":
            return elemento in estructura
        elif tipo_estructura == "set":
            return elemento in estructura
        elif tipo_estructura == "dict":
            return elemento in estructura

    inicio = time.time()
    resultado = buscar()
    fin = time.time()
    
    tiempo_ejecucion = fin - inicio
    memoria_utilizada = medir_memoria(estructura)
    
    return tiempo_ejecucion, memoria_utilizada

def evaluar_busqueda_recursiva(lista, elemento):
    inicio = time.time()
    resultado = busqueda_recursiva(lista, elemento)
    fin = time.time()
    
    tiempo = fin - inicio
    memoria = medir_memoria(lista)
    
    return tiempo, memoria

