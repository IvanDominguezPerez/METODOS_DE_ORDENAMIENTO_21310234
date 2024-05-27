#Practica: 008_METODOS_DE_ORDENAMIENTO__STRAIGHT_MERGING
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

def straight_merge_sort(arr):
    # Función para mezclar dos sublistas ordenadas
    def merge(left, right):
        # Lista de resultado
        result = []
        i = j = 0

        # Recorre ambas sublistas y mezcla sus elementos en orden
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # Agrega los elementos restantes de left, si hay alguno
        while i < len(left):
            result.append(left[i])
            i += 1

        # Agrega los elementos restantes de right, si hay alguno
        while j < len(right):
            result.append(right[j])
            j += 1

        return result

    # Función recursiva para dividir la lista y mezclar las sublistas ordenadas
    def merge_sort(arr):
        if len(arr) <= 1:
            return arr
        
        # Encuentra el punto medio de la lista
        mid = len(arr) // 2
        
        # Divide la lista en dos mitades
        left_half = merge_sort(arr[:mid])
        right_half = merge_sort(arr[mid:])
        
        # Mezcla las dos mitades ordenadas
        return merge(left_half, right_half)

    # Llama a la función recursiva merge_sort y copia el resultado en la lista original
    arr[:] = merge_sort(arr)

# Lista de ejemplo para ordenar
arr = [64, 34, 25, 12, 22, 11, 90]

# Llamada a la función de ordenamiento Straight Merging
straight_merge_sort(arr)

# Imprime la lista ordenada
print("Lista ordenada es:", arr)



#Descripción del Código:
#Definición de la función straight_merge_sort(arr):

#Esta función toma una lista arr como argumento y la ordena en su lugar utilizando el algoritmo de Straight Merging.
#Función merge(left, right):

#Mezcla dos sublistas ordenadas (left y right) en una lista ordenada.
#Inicializa una lista result vacía para almacenar el resultado de la mezcla.
#Inicializa los índices i y j para recorrer las sublistas left y right, respectivamente.
#Compara los elementos de left y right, y agrega el menor a result.
#Si se agotan los elementos de left, agrega los elementos restantes de right a result.
#Si se agotan los elementos de right, agrega los elementos restantes de left a result.
#Retorna la lista result mezclada y ordenada.
#Función recursiva merge_sort(arr):

#Ordena la lista arr utilizando el algoritmo de MergeSort.
#Si la lista tiene uno o cero elementos, ya está ordenada y se retorna.
#Encuentra el punto medio de la lista (mid = len(arr) // 2).
#Divide la lista en dos mitades y las ordena recursivamente.
#Mezcla las dos mitades ordenadas utilizando la función merge(left, right).
#Retorna la lista ordenada resultante.
#Llama a la función recursiva merge_sort(arr) y copia el resultado en la lista original:

#arr[:] = merge_sort(arr): Ordena la lista arr y copia el resultado en la lista original arr.
#Lista de ejemplo para ordenar:

#arr = [64, 34, 25, 12, 22, 11, 90]: Define una lista de ejemplo que se desea ordenar.
#Llamada a la función de ordenamiento Straight Merging:

#straight_merge_sort(arr): Llama a la función straight_merge_sort pasando la lista arr como argumento.
#Imprime la lista ordenada:

#print("Lista ordenada es:", arr): Imprime la lista arr ya ordenada.
