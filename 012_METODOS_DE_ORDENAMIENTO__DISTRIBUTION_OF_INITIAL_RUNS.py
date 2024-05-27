#Practica: 012_METODOS_DE_ORDENAMIENTO__DISTRIBUTION_OF_INITIAL_RUNS
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

import heapq

# Función para generar ejecuciones iniciales
def generate_initial_runs(arr, run_size):
    runs = []
    for i in range(0, len(arr), run_size):
        runs.append(sorted(arr[i:i + run_size]))
    return runs

# Función para mezclar las ejecuciones iniciales
def merge_initial_runs(initial_runs):
    min_heap = []
    for i, run in enumerate(initial_runs):
        if run:
            heapq.heappush(min_heap, (run[0], i, 0))
    
    result = []
    while min_heap:
        value, run_index, elem_index = heapq.heappop(min_heap)
        result.append(value)
        if elem_index + 1 < len(initial_runs[run_index]):
            next_value = initial_runs[run_index][elem_index + 1]
            heapq.heappush(min_heap, (next_value, run_index, elem_index + 1))
    
    return result

# Función principal del algoritmo de Distribution of Initial Runs
def distribution_of_initial_runs(arr, memory_size):
    initial_runs = []
    while len(arr) > 0:
        # Genera una ejecución inicial usando la cantidad de memoria disponible
        run_size = min(memory_size // (len(initial_runs) + 1), len(arr))
        initial_runs.append(sorted(arr[:run_size]))
        arr = arr[run_size:]

    # Mezcla las ejecuciones iniciales hasta que solo quede una ejecución
    while len(initial_runs) > 1:
        merged_run = merge_initial_runs(initial_runs)
        initial_runs = [merged_run]

    # Copia la lista ordenada final de nuevo en arr
    arr[:] = initial_runs[0]

# Lista de ejemplo para ordenar
arr = [64, 34, 25, 12, 22, 11, 90]
memory_size = 4  # Tamaño de la memoria disponible

# Llamada a la función de ordenamiento Distribution of Initial Runs
distribution_of_initial_runs(arr, memory_size)

# Imprime la lista ordenada
print("Lista ordenada es:", arr)




#Descripción del Código:
#Importación de la biblioteca heapq:

#heapq proporciona una implementación de la cola de prioridad (mínimo montículo), que es útil para la mezcla de múltiples vías.
#Definición de la función generate_initial_runs(arr, run_size):

#Genera ejecuciones iniciales (initial_runs) a partir de la lista arr dividiéndola en partes de tamaño run_size.
#Recorre arr en pasos de run_size y ordena cada ejecución antes de agregarla a initial_runs.
#Función merge_initial_runs(initial_runs):

#Mezcla las ejecuciones iniciales usando un mínimo montículo (min_heap).
#Inicializa min_heap y agrega el primer elemento de cada ejecución junto con el índice de la ejecución y el índice del elemento.
#Mientras min_heap no esté vacío, extrae el menor elemento y lo agrega a la lista result.
#Si hay más elementos en la ejecución correspondiente, agrega el siguiente elemento al min_heap.
#Función principal distribution_of_initial_runs(arr, memory_size):

#Genera las ejecuciones iniciales (initial_runs) a partir de la lista arr utilizando la cantidad de memoria disponible como tamaño máximo de cada ejecución.
#Mezcla las ejecuciones iniciales hasta que solo quede una ejecución.
#Copia la lista ordenada final de nuevo en arr.
#Lista de ejemplo para ordenar:

#arr = [64, 34, 25, 12, 22, 11, 90]: Define una lista de ejemplo que se desea ordenar.
#Tamaño de la memoria disponible:

#memory_size = 4: Define el tamaño de la memoria disponible para generar las ejecuciones iniciales.
#Llamada a la función de ordenamiento Distribution of Initial Runs:

#distribution_of_initial_runs(arr, memory_size): Llama a la función distribution_of_initial_runs pasando la lista arr y el tamaño de la memoria disponible memory_size como argumentos.
#Imprime la lista ordenada:

#print("Lista ordenada es:", arr): Imprime la lista arr ya ordenada.
