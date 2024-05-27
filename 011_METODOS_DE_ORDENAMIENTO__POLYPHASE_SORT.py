#Practica: 011_METODOS_DE_ORDENAMIENTO__POLYPHASE_SORT
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

import heapq

# Función para generar runs (sublistas ordenadas)
def generate_runs(arr, run_size):
    runs = []
    for i in range(0, len(arr), run_size):
        runs.append(sorted(arr[i:i + run_size]))
    return runs

# Función para mezclar k sublistas usando un mínimo montículo
def k_way_merge(runs):
    min_heap = []
    for i, run in enumerate(runs):
        if run:
            heapq.heappush(min_heap, (run[0], i, 0))
    
    result = []
    while min_heap:
        value, run_index, elem_index = heapq.heappop(min_heap)
        result.append(value)
        if elem_index + 1 < len(runs[run_index]):
            next_value = runs[run_index][elem_index + 1]
            heapq.heappush(min_heap, (next_value, run_index, elem_index + 1))
    
    return result

# Función principal del algoritmo de Polyphase Sort
def polyphase_sort(arr, run_size):
    # Genera las sublistas ordenadas (runs)
    runs = generate_runs(arr, run_size)
    
    while len(runs) > 1:
        # Mezcla las sublistas en la fase actual
        merged_run = k_way_merge(runs)
        
        # Genera nuevas sublistas del tamaño de run_size
        runs = generate_runs(merged_run, run_size)
    
    # Copia la lista ordenada final de nuevo en arr
    arr[:] = runs[0]

# Lista de ejemplo para ordenar
arr = [64, 34, 25, 12, 22, 11, 90]
run_size = 3  # Tamaño de cada run

# Llamada a la función de ordenamiento Polyphase Sort
polyphase_sort(arr, run_size)

# Imprime la lista ordenada
print("Lista ordenada es:", arr)




#Descripción del Código:
#Importación de la biblioteca heapq:

#heapq proporciona una implementación de la cola de prioridad (mínimo montículo), que es útil para la mezcla de múltiples vías.
#Definición de la función generate_runs(arr, run_size):

#Genera sublistas ordenadas (runs) a partir de la lista arr dividiéndola en partes de tamaño run_size.
#Recorre arr en pasos de run_size y ordena cada sublista antes de agregarla a runs.
#Función k_way_merge(runs):

#Mezcla k sublistas ordenadas (runs) en una lista ordenada utilizando un mínimo montículo (min_heap).
#Inicializa min_heap y agrega el primer elemento de cada sublista junto con el índice de la sublista y el índice del elemento.
#Mientras min_heap no esté vacío, extrae el menor elemento y lo agrega a la lista result.
#Si hay más elementos en la sublista correspondiente, agrega el siguiente elemento al min_heap.
#Función principal polyphase_sort(arr, run_size):

#Genera las sublistas ordenadas (runs) a partir de la lista arr llamando a generate_runs(arr, run_size).
#Realiza la mezcla k-way hasta que solo quede una sublista:
#Mezcla las sublistas en la fase actual utilizando k_way_merge(runs).
#Actualiza runs con el resultado de la mezcla, generando nuevas sublistas ordenadas.
#Copia la lista ordenada final de nuevo en arr.
#Lista de ejemplo para ordenar:

#arr = [64, 34, 25, 12, 22, 11, 90]: Define una lista de ejemplo que se desea ordenar.
#Tamaño de cada run:

#run_size = 3: Define el tamaño de cada sublista ordenada (run).
#Llamada a la función de ordenamiento Polyphase Sort:

#polyphase_sort(arr, run_size): Llama a la función polyphase_sort pasando la lista arr y el tamaño de cada run run_size como argumentos.
#Imprime la lista ordenada:

#print("Lista ordenada es:", arr): Imprime la lista arr ya ordenada.
