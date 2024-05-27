#Practica: 006_METODOS_DE_ORDENAMIENTO__MERGESORT
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

def merge_sort(arr):
    # Si la lista tiene uno o cero elementos, ya está ordenada
    if len(arr) > 1:
        # Encuentra el punto medio de la lista
        mid = len(arr) // 2
        # Divide la lista en dos mitades
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Llama recursivamente a merge_sort en cada mitad
        merge_sort(left_half)
        merge_sort(right_half)

        # Inicializa los índices para recorrer las sublistas y la lista principal
        i = j = k = 0

        # Recorre ambas mitades y copia los elementos ordenados a la lista principal
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Copia los elementos restantes de left_half, si hay alguno
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Copia los elementos restantes de right_half, si hay alguno
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Lista de ejemplo para ordenar
arr = [64, 34, 25, 12, 22, 11, 90]

# Llamada a la función de ordenamiento MergeSort
merge_sort(arr)

# Imprime la lista ordenada
print("Lista ordenada es:", arr)



#Descripción del Código:
#Definición de la función merge_sort(arr):

#Esta función toma una lista arr como argumento y la ordena en su lugar utilizando el algoritmo MergeSort.
#Verifica si la lista tiene más de un elemento:

#if len(arr) > 1:: Si la lista tiene uno o cero elementos, ya está ordenada y no se necesita hacer nada más.
#Encuentra el punto medio de la lista:

#mid = len(arr) // 2: Calcula el índice del punto medio de la lista.
#Divide la lista en dos mitades:

#left_half = arr[:mid]: La primera mitad de la lista.
#right_half = arr[mid:]: La segunda mitad de la lista.
#Llama recursivamente a merge_sort en cada mitad:

#merge_sort(left_half): Ordena la primera mitad.
#merge_sort(right_half): Ordena la segunda mitad.
#Inicializa los índices para recorrer las sublistas y la lista principal:

#i = j = k = 0: i es el índice para left_half, j es el índice para right_half, y k es el índice para la lista principal arr.
#Recorre ambas mitades y copia los elementos ordenados a la lista principal:

#while i < len(left_half) and j < len(right_half):: Recorre ambas mitades hasta que se alcance el final de una de ellas.
#if left_half[i] < right_half[j]: arr[k] = left_half[i]; i += 1: Si el elemento actual de left_half es menor que el de right_half, copia left_half[i] a arr[k] y avanza el índice i.
#else: arr[k] = right_half[j]; j += 1: Si el elemento actual de right_half es menor o igual, copia right_half[j] a arr[k] y avanza el índice j.
#k += 1: Avanza el índice k en la lista principal.
#Copia los elementos restantes de left_half, si hay alguno:

#while i < len(left_half): arr[k] = left_half[i]; i += 1; k += 1: Si quedan elementos en left_half, los copia a arr.
#Copia los elementos restantes de right_half, si hay alguno:

#while j < len(right_half): arr[k] = right_half[j]; j += 1; k += 1: Si quedan elementos en right_half, los copia a arr.
#Lista de ejemplo para ordenar:

#arr = [64, 34, 25, 12, 22, 11, 90]: Define una lista de ejemplo que se desea ordenar.
#Llamada a la función de ordenamiento MergeSort:

#merge_sort(arr): Llama a la función merge_sort pasando la lista arr como argumento.
#Imprime la lista ordenada:

#print("Lista ordenada es:", arr): Imprime la lista arr ya ordenada.
