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

def comparar_busquedas(tamanios):
    resultados = {'list': [], 'set': [], 'dict': [], 'recursiva': []}

    for n in tamanios:
        lista, conj, dicc, existe, no_existe = generar_estructuras(n)

        for estructura, tipo in [(lista, 'list'), (conj, 'set'), (dicc, 'dict')]:
            tiempo_existe, mem_existe = evaluar_busqueda(estructura, existe, tipo)
            tiempo_no, mem_no = evaluar_busqueda(estructura, no_existe, tipo)

            resultados[tipo].append({
                'n': n,
                'tiempo_existente': tiempo_existe,
                'tiempo_inexistente': tiempo_no,
                'memoria_existente': mem_existe,
                'memoria_inexistente': mem_no
            })

        if n <= 1000:  # Evitamos stack overflow con listas grandes
            tiempo_rec_ex, mem_rec_ex = evaluar_busqueda_recursiva(lista, existe)
            tiempo_rec_no, mem_rec_no = evaluar_busqueda_recursiva(lista, no_existe)

            resultados['recursiva'].append({
                'n': n,
                'tiempo_existente': tiempo_rec_ex,
                'tiempo_inexistente': tiempo_rec_no,
                'memoria_existente': mem_rec_ex,
                'memoria_inexistente': mem_rec_no
            })

    return resultados

def mostrar_resultados_consola(resultados, tamanios):
    print("\n=== RESULTADOS DE BÚSQUEDA ===")
    for tipo in ['list', 'set', 'dict', 'recursiva']:
        if tipo not in resultados:
            continue
        print(f"\nEstructura: {tipo.upper()}")
        print(f"{'Tamaño':>10} | {'Tiempo (ex)':>12} | {'Tiempo (no)':>12} | {'Mem (ex)':>10} | {'Mem (no)':>10}")
        print("-" * 62)
        for res in resultados[tipo]:
            print(f"{res['n']:>10} | {res['tiempo_existente']:.6f}s | {res['tiempo_inexistente']:.6f}s | "
                f"{res['memoria_existente']:.4f} MiB | {res['memoria_inexistente']:.4f} MiB")