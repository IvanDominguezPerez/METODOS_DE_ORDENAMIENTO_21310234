#Practica: 002_METODOS_DE_ORDENAMIENTO__SELECTIONSORT
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

def selection_sort(arr):
    # Recorre todos los elementos de la lista
    for i in range(len(arr)):
        # Encuentra el índice del elemento mínimo en la sublista arr[i..len(arr)-1]
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # Intercambia el elemento mínimo encontrado con el primer elemento de la sublista
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Lista de ejemplo para ordenar
arr = [64, 25, 12, 22, 11]

# Llamada a la función de ordenamiento por selección
selection_sort(arr)

# Imprime la lista ordenada
print("Lista ordenada es:", arr)



#Descripción del Código:
#Definición de la función selection_sort(arr):

#Esta función toma una lista arr como argumento y la ordena en su lugar utilizando el algoritmo de ordenamiento por selección.
#Recorre todos los elementos de la lista:

#for i in range(len(arr)):: Este bucle recorre todos los índices de la lista desde 0 hasta len(arr) - 1.
#Encuentra el índice del elemento mínimo en la sublista arr[i..len(arr)-1]:

#min_idx = i: Inicializa min_idx con el índice actual i. Este índice almacenará la posición del elemento mínimo encontrado en la sublista.
#for j in range(i + 1, len(arr)):: Este bucle anidado recorre los elementos de la sublista que comienza en i + 1 hasta el final de la lista.
#if arr[j] < arr[min_idx]:: Compara cada elemento arr[j] de la sublista con el elemento en arr[min_idx]. Si arr[j] es menor, actualiza min_idx con j.
#Intercambia el elemento mínimo encontrado con el primer elemento de la sublista:

#arr[i], arr[min_idx] = arr[min_idx], arr[i]: Intercambia el elemento en el índice i con el elemento mínimo encontrado en min_idx.
#Lista de ejemplo para ordenar:

#arr = [64, 25, 12, 22, 11]: Define una lista de ejemplo que se desea ordenar.
#Llamada a la función de ordenamiento por selección:

#selection_sort(arr): Llama a la función selection_sort pasando la lista arr como argumento.
#Imprime la lista ordenada:

#print("Lista ordenada es:", arr): Imprime la lista arr ya ordenada.
