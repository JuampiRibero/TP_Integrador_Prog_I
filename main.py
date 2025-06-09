# Importamos los módulos que vamos a utilizar.
import random
import sys
import time

# Limitamos la recursión a 2000, porque una recursión muy profunda puede generar un "stack overflow".
sys.setrecursionlimit(2000)

# Generamos diferentes estructuras de datos con 'n' elementos.    
def generar_estructuras(n):
    datos = list(range(n))

    estructura_lista = datos
    estructura_set = set(datos)
    estructura_diccionario = {i: datos[i] for i in range(n)}

    elemento_existente = random.choice(datos)
    elemento_no_existente = -1

    return estructura_lista, estructura_set, estructura_diccionario, elemento_existente, elemento_no_existente

# Realizamos una búsqueda recursiva de un elemento en una lista.
def busqueda_recursiva(list, elemento, index = 0):
    if index >= len(list): # Si el índice excede la longitud de la lista, el elemento no se encontró.
        return False
    if list[index] == elemento: # Si el elemento actual en el índice coincide, el elemento se encontró.
        return True
    # Buscamos en el resto de la lista.
    return busqueda_recursiva(list, elemento, index + 1) 

# Medimos el tamaño de una estructura de datos en MiB (Megabytes).
def medir_memoria(estructura):
    return sys.getsizeof(estructura) / (1024 * 1024)

# Evaluamos el tiempo de ejecución y el uso de memoria para la búsqueda de un elemento.
def evaluar_busqueda(estructura, elemento, tipo_estructura):
    
    # Realizamos la búsqueda de acuerdo al tipo de estructura.
    def buscar():
        if tipo_estructura == "list": # Buscamos la pertenencia en una lista.
            return elemento in estructura
        elif tipo_estructura == "set": # Buscamos la pertenencia en un conjunto.
            return elemento in estructura
        elif tipo_estructura == "dict": # Buscamos la pertenencia en un diccionario.
            return elemento in estructura

    inicio = time.time() # Registramos el tiempo de inicio antes de la búsqueda.
    resultado = buscar() # Ejecutamos la función de búsqueda.
    fin = time.time() # Registramos el tiempo de finalización después de la búsqueda.
    
    tiempo_ejecucion = fin - inicio # Calculamos el tiempo de la búsqueda.
    memoria_utilizada = medir_memoria(estructura) # Medimos la memoria utilizada por la estructura.
    
    return tiempo_ejecucion, memoria_utilizada

# Evaluamos el tiempo de ejecución y el uso de memoria para la búsqueda recursiva.
def evaluar_busqueda_recursiva(lista, elemento):
    inicio = time.time() # Registramos el tiempo de inicio antes de la búsqueda recursiva.
    resultado = busqueda_recursiva(lista, elemento) # Ejecutamos la función de búsqueda recursiva.
    fin = time.time() # Registramos el tiempo de finalización después de la búsqueda recursiva.
    
    tiempo = fin - inicio # Calculamos el tiempo de la búsqueda.
    memoria = medir_memoria(lista) # Medimos la memoria utilizada por la estructura.
    
    return tiempo, memoria

# Realizamos la comparación de búsquedas para diferentes tamaños de estructuras.
def comparar_busquedas(tamanios):
    resultados = {'list': [], 'set': [], 'dict': [], 'recursiva': []}

    # Iteramos sobre cada tamaño de estructura.
    for n in tamanios:
        lista, conj, dicc, existe, no_existe = generar_estructuras(n)

        # Evaluamos la búsqueda para cada tipo de estructura.
        for estructura, tipo in [(lista, 'list'), (conj, 'set'), (dicc, 'dict')]:
            tiempo_existe, mem_existe = evaluar_busqueda(estructura, existe, tipo) # Medimos para elemento existente.
            tiempo_no, mem_no = evaluar_busqueda(estructura, no_existe, tipo) # Medimos para elemento no existente.

            # Guaramos los datos en el diccionario resultados.
            resultados[tipo].append({
                'n': n,
                'tiempo_existente': tiempo_existe,
                'tiempo_inexistente': tiempo_no,
                'memoria_existente': mem_existe,
                'memoria_inexistente': mem_no
            })

        if n <= 1000:  # Evitamos stack overflow con listas grandes.
            tiempo_rec_ex, mem_rec_ex = evaluar_busqueda_recursiva(lista, existe) # Evaluamos la búsqueda recursiva para elemento existente.
            tiempo_rec_no, mem_rec_no = evaluar_busqueda_recursiva(lista, no_existe) # Evaluamos la búsqueda recursiva para elemento no existente.

            # Guaramos los datos en el diccionario resultados.
            resultados['recursiva'].append({
                'n': n,
                'tiempo_existente': tiempo_rec_ex,
                'tiempo_inexistente': tiempo_rec_no,
                'memoria_existente': mem_rec_ex,
                'memoria_inexistente': mem_rec_no
            })

    return resultados

# Imprimimos los resultados de las comparaciones en la consola de manera formateada.
def mostrar_resultados_consola(resultados, tamanios):
    print("\n=== RESULTADOS DE BÚSQUEDA ===")
    for tipo in ['list', 'set', 'dict', 'recursiva']:
        if tipo not in resultados:
            continue
        print(f"\nTIPO DE ESTRUCTURA: {tipo.upper()}\n")
        print(f"{'Tamaño':>10} | {'Tiempo (ex)':>12} | {'Tiempo (no)':>12} | {'Mem (ex)':>10} | {'Mem (no)':>10}")
        print("-" * 62)
        for res in resultados[tipo]:
            print(f"{res['n']:>10} | {res['tiempo_existente']:.6f}s | {res['tiempo_inexistente']:.6f}s | "
                f"{res['memoria_existente']:.4f} MiB | {res['memoria_inexistente']:.4f} MiB")

# Bloque principal de ejecución del script.
if __name__ == "__main__":
    tamanios = [100, 500, 1000, 10000, 100000, 1000000, 10000000] # Definimos los tamaños de las estructuras a probar.
    resultados = comparar_busquedas(tamanios) # Ejecutamos la comparación de búsquedas.
    mostrar_resultados_consola(resultados, tamanios) # Mostramos los resultados en la consola.
