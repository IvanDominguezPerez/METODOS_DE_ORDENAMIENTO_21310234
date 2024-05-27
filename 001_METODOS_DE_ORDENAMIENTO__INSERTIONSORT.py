#Practica: 001_METODOS_DE_ORDENAMIENTO__INSERTIONSORT
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

def insertion_sort(arr):
    # Recorre desde el segundo elemento hasta el último
    for i in range(1, len(arr)):
        # Almacena el valor del elemento actual
        key = arr[i]
        # Inicializa j con el índice del elemento anterior
        j = i - 1
        # Mueve los elementos de arr[0..i-1] que son mayores que key
        # una posición hacia adelante para hacer espacio para el key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        # Coloca el key en su posición correcta dentro de la parte ordenada
        arr[j + 1] = key

# Lista de ejemplo para ordenar
arr = [12, 11, 13, 5, 6]

# Llamada a la función de ordenamiento por inserción
insertion_sort(arr)

# Imprime la lista ordenada
print("Lista ordenada es:", arr)



#Descripción del Código:
#Definición de la función insertion_sort(arr):

#Esta función toma una lista arr como argumento y la ordena en su lugar utilizando el algoritmo de ordenamiento por inserción.
#Recorre desde el segundo elemento hasta el último:

#El bucle for i in range(1, len(arr)): recorre la lista empezando desde el segundo elemento (índice 1) hasta el último.
#Almacena el valor del elemento actual:

#key = arr[i]: Guarda el valor del elemento actual en la variable key.
#Inicializa j con el índice del elemento anterior:

#j = i - 1: Inicializa j con el índice del elemento anterior al actual.
#Mueve los elementos de arr[0..i-1] que son mayores que key una posición hacia adelante:

#while j >= 0 and arr[j] > key:: Este bucle while se ejecuta mientras j sea mayor o igual a 0 y arr[j] sea mayor que key. Esto garantiza que se sigan desplazando los elementos mayores hacia la derecha.
#arr[j + 1] = arr[j]: Mueve el elemento arr[j] una posición hacia adelante.
#j -= 1: Decrementa j para seguir comparando con el siguiente elemento a la izquierda.
#Coloca key en su posición correcta dentro de la parte ordenada:

#arr[j + 1] = key: Coloca el key en su posición correcta en la lista, que es justo después del último elemento menor que key.
#Lista de ejemplo para ordenar:

#arr = [12, 11, 13, 5, 6]: Define una lista de ejemplo que se desea ordenar.
#Llamada a la función de ordenamiento por inserción:

#insertion_sort(arr): Llama a la función insertion_sort pasando la lista arr como argumento.
#Imprime la lista ordenada:

#print("Lista ordenada es:", arr): Imprime la lista arr ya ordenada.
#Este código ordenará la lista [12, 11, 13, 5, 6] en orden ascendente, resultando en [5, 6, 11, 12, 13]
