#Practica: 010_METODOS_DE_ORDENAMIENTO__BALANCED_MULTIWAY_MERGING
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

import heapq

def balanced_multiway_merge_sort(arr, num_ways):
    # Divide la lista en num_ways sublistas
    def divide(arr, num_ways):
        sublists = []
        length = len(arr)
        step = length // num_ways
        for i in range(0, length, step):
            sublists.append(arr[i:i + step])
        return sublists

    # Función principal del algoritmo de mezcla múltiple balanceada
    def multiway_merge(sublists):
        min_heap = []
        for i, sublist in enumerate(sublists):
            if sublist:
                heapq.heappush(min_heap, (sublist[0], i, 0))

        result = []
        while min_heap:
            value, list_index, element_index = heapq.heappop(min_heap)
            result.append(value)
            if element_index + 1 < len(sublists[list_index]):
                next_value = sublists[list_index][element_index + 1]
                heapq.heappush(min_heap, (next_value, list_index, element_index + 1))
        return result

    # Realiza la ordenación por mezcla múltiple balanceada
    sublists = divide(arr, num_ways)
    for i in range(len(sublists)):
        sublists[i] = sorted(sublists[i])

    arr[:] = multiway_merge(sublists)

# Lista de ejemplo para ordenar
arr = [64, 34, 25, 12, 22, 11, 90]
num_ways = 3  # Número de vías para la mezcla

# Llamada a la función de ordenamiento Balanced Multiway Merging
balanced_multiway_merge_sort(arr, num_ways)

# Imprime la lista ordenada
print("Lista ordenada es:", arr)



#Descripción del Código:
#Importación de la biblioteca heapq:

#heapq es una biblioteca que proporciona una implementación de la cola de prioridad (mínimo montículo), que es útil para la mezcla de múltiples vías.
#Definición de la función balanced_multiway_merge_sort(arr, num_ways):

#Esta función toma una lista arr y un número num_ways que indica en cuántas sublistas dividir la lista original para realizar la mezcla balanceada.
#Función divide(arr, num_ways):

#Divide la lista arr en num_ways sublistas.
#length = len(arr): Obtiene la longitud de la lista arr.
#step = length // num_ways: Calcula el tamaño de cada sublista.
#Recorre la lista arr en pasos de tamaño step y agrega cada sublista a sublists.
#Función multiway_merge(sublists):

#Mezcla num_ways sublistas ordenadas en una lista ordenada utilizando un mínimo montículo (min_heap).
#Inicializa min_heap y agrega el primer elemento de cada sublista junto con el índice de la sublista y el índice del elemento.
#Mientras min_heap no esté vacío, extrae el menor elemento y lo agrega a la lista result.
#Si hay más elementos en la sublista correspondiente, agrega el siguiente elemento al min_heap.
#Realiza la ordenación por mezcla múltiple balanceada:

#Divide la lista arr en sublistas llamando a divide(arr, num_ways).
#Ordena cada sublista individualmente.
#Mezcla las sublistas ordenadas utilizando multiway_merge(sublists).
#Copia la lista ordenada resultante de nuevo en arr.
#Lista de ejemplo para ordenar:

#arr = [64, 34, 25, 12, 22, 11, 90]: Define una lista de ejemplo que se desea ordenar.
#Número de vías para la mezcla:

#num_ways = 3: Define el número de sublistas en las que se dividirá la lista original para realizar la mezcla múltiple balanceada.
#Llamada a la función de ordenamiento Balanced Multiway Merging:

#balanced_multiway_merge_sort(arr, num_ways): Llama a la función balanced_multiway_merge_sort pasando la lista arr y el número de vías num_ways como argumentos.
#Imprime la lista ordenada:

#print("Lista ordenada es:", arr): Imprime la lista arr ya ordenada.
