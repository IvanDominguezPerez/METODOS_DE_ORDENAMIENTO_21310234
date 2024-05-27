#Practica: 003_METODOS_DE_ORDENAMIENTO__INTERCAMBIO
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

def bubble_sort(arr):
    # Obtiene la longitud de la lista
    n = len(arr)
    # Recorre todos los elementos de la lista
    for i in range(n):
        # Inicializa una bandera que indica si hubo intercambios en esta pasada
        swapped = False
        # Recorre la lista desde el inicio hasta el penúltimo elemento no ordenado
        for j in range(0, n-i-1):
            # Compara el elemento actual con el siguiente
            if arr[j] > arr[j + 1]:
                # Si están en el orden incorrecto, intercámbialos
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Marca que hubo un intercambio
                swapped = True
        # Si no hubo intercambios, la lista ya está ordenada
        if not swapped:
            break

# Lista de ejemplo para ordenar
arr = [64, 34, 25, 12, 22, 11, 90]

# Llamada a la función de ordenamiento por burbuja
bubble_sort(arr)

# Imprime la lista ordenada
print("Lista ordenada es:", arr)



#Descripción del Código:
#Definición de la función bubble_sort(arr):

#Esta función toma una lista arr como argumento y la ordena en su lugar utilizando el algoritmo de ordenamiento por burbuja.
#Obtiene la longitud de la lista:

#n = len(arr): Calcula la longitud de la lista y la almacena en la variable n.
#Recorre todos los elementos de la lista:

#for i in range(n):: Este bucle recorre todos los índices de la lista desde 0 hasta n-1.
#Inicializa una bandera que indica si hubo intercambios en esta pasada:

#swapped = False: Inicializa la variable swapped como False. Esta variable se utilizará para detectar si hubo algún intercambio durante la iteración actual.
#Recorre la lista desde el inicio hasta el penúltimo elemento no ordenado:

#for j in range(0, n-i-1):: Este bucle recorre la lista desde el inicio hasta el último elemento no ordenado (el cual está en n-i-1).
#Compara el elemento actual con el siguiente:

#if arr[j] > arr[j + 1]:: Compara el elemento en la posición j con el elemento en la posición j + 1.
#Si están en el orden incorrecto, intercámbialos:

#arr[j], arr[j + 1] = arr[j + 1], arr[j]: Si el elemento actual es mayor que el siguiente, los intercambia.
#Marca que hubo un intercambio:

#swapped = True: Si se realiza un intercambio, se establece swapped como True.
#Si no hubo intercambios, la lista ya está ordenada:

#if not swapped: break: Si no hubo intercambios en la iteración actual, se rompe el bucle for, ya que la lista está ordenada.
#Lista de ejemplo para ordenar:

#arr = [64, 34, 25, 12, 22, 11, 90]: Define una lista de ejemplo que se desea ordenar.
#Llamada a la función de ordenamiento por burbuja:

#bubble_sort(arr): Llama a la función bubble_sort pasando la lista arr como argumento.
#Imprime la lista ordenada:

#print("Lista ordenada es:", arr): Imprime la lista arr ya ordenada.
