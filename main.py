import random
import sys
import time

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

def medir_memoria(estructura, tipo_estructura):
    memoria = sys.getsizeof(estructura)
    return memoria

def evaluar_busqueda(estructura, elemento, tipo_estructura):

    def buscar():
        if tipo_estructura == "lista":
            return elemento in estructura
        elif tipo_estructura == "set":
            return elemento in estructura
        elif tipo_estructura == "diccionario":
            return elemento in estructura

    inicio = time.time()
    memoria_utilizada = medir_memoria(buscar())
    fin = time.time()

    tiempo_ejecucion = fin - inicio
    return tiempo_ejecucion, memoria_utilizada


if __name__ == "__main__":
    tamanios = [10, 100, 500, 1000, 10000, 100000]
    for n in tamanios:
        lista, conjunto, diccionario, existente, no_existente = generar_estructuras(n)
        
        
