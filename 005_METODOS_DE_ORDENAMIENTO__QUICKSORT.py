#Practica: 005_METODOS_DE_ORDENAMIENTO__QUICKSORT
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

def quicksort(arr):
    # Función auxiliar para realizar la partición
    def partition(low, high):
        # Elige el último elemento como pivote
        pivot = arr[high]
        # Índice del menor elemento
        i = low - 1
        for j in range(low, high):
            # Si el elemento actual es menor o igual al pivote
            if arr[j] <= pivot:
                i += 1
                # Intercambia arr[i] con arr[j]
                arr[i], arr[j] = arr[j], arr[i]
        # Intercambia el pivote con el elemento en arr[i+1]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    # Función recursiva para aplicar QuickSort
    def quicksort_recursive(low, high):
        if low < high:
            # Obtiene el índice de partición
            pi = partition(low, high)
            # Ordena los elementos antes y después de la partición
            quicksort_recursive(low, pi - 1)
            quicksort_recursive(pi + 1, high)

    # Llama a la función recursiva con los índices iniciales
    quicksort_recursive(0, len(arr) - 1)

# Lista de ejemplo para ordenar
arr = [64, 34, 25, 12, 22, 11, 90]

# Llamada a la función de ordenamiento QuickSort
quicksort(arr)

# Imprime la lista ordenada
print("Lista ordenada es:", arr)



#Descripción del Código:
#Definición de la función quicksort(arr):

#Esta función toma una lista arr como argumento y la ordena en su lugar utilizando el algoritmo QuickSort.
#Función auxiliar partition(low, high):

#Esta función realiza la partición del arreglo y devuelve el índice de partición.
#Elige el último elemento del subarreglo como pivote (pivot = arr[high]).
#Inicializa el índice del menor elemento (i = low - 1).
#Recorre los elementos del subarreglo desde low hasta high - 1:
#Si el elemento actual es menor o igual al pivote, incrementa i y lo intercambia con el elemento en arr[i].
#Intercambia el pivote con el elemento en arr[i + 1] para colocar el pivote en su posición correcta.
#Retorna el índice de partición (i + 1).
#Función recursiva quicksort_recursive(low, high):

#Aplica recursivamente QuickSort a los subarreglos.
#Si low es menor que high, realiza la partición y obtiene el índice de partición (pi).
#Llama a quicksort_recursive para los subarreglos a la izquierda (low a pi - 1) y a la derecha (pi + 1 a high) del pivote.
#Llama a la función recursiva con los índices iniciales

#quicksort_recursive(0, len(arr) - 1): Inicia QuickSort en toda la lista desde el primer hasta el último índice.
#Lista de ejemplo para ordenar:

#arr = [64, 34, 25, 12, 22, 11, 90]: Define una lista de ejemplo que se desea ordenar.
#Llamada a la función de ordenamiento QuickSort:

#quicksort(arr): Llama a la función quicksort pasando la lista arr como argumento.
#Imprime la lista ordenada:

#print("Lista ordenada es:", arr): Imprime la lista arr ya ordenada.
