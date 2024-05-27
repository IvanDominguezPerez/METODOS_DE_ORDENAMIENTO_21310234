#Practica: 007_METODOS_DE_ORDENAMIENTO__RADIXSORT
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

def counting_sort(arr, exp):
    n = len(arr)
    # Resultado temporal que almacena la lista ordenada por los dígitos actuales
    output = [0] * n
    # Inicializa el contador para los dígitos (0-9)
    count = [0] * 10

    # Cuenta las ocurrencias de cada dígito en el lugar actual (exp)
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Modifica count[i] para que contenga la posición real de este dígito en output
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Construye el arreglo output
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copia el arreglo output en arr, de modo que arr contenga los números ordenados según el dígito actual
    for i in range(n):
        arr[i] = output[i]

def radix_sort(arr):
    # Encuentra el número máximo para saber el número de dígitos
    max_num = max(arr)

    # Realiza counting sort para cada dígito
    # exp es 10^i donde i es el dígito actual
    exp = 1
    while max_num // exp > 0:
        counting_sort(arr, exp)
        exp *= 10

# Lista de ejemplo para ordenar
arr = [170, 45, 75, 90, 802, 24, 2, 66]

# Llamada a la función de ordenamiento RadixSort
radix_sort(arr)

# Imprime la lista ordenada
print("Lista ordenada es:", arr)



#Descripción del Código:
#Función counting_sort(arr, exp):

#Esta función realiza el Counting Sort en función del dígito representado por exp (unidad, decena, centena, etc.).
#Inicializa variables y estructuras:

#n = len(arr): Obtiene el tamaño del arreglo arr.
#output = [0] * n: Inicializa un arreglo de salida de tamaño n con ceros.
#count = [0] * 10: Inicializa un arreglo de contadores para los dígitos (0-9).
#Cuenta las ocurrencias de cada dígito en el lugar actual (exp):

#for i in range(n):: Recorre cada elemento del arreglo.
#index = arr[i] // exp: Calcula el dígito actual de arr[i].
#count[index % 10] += 1: Incrementa el contador correspondiente a ese dígito.
#Modifica count para que contenga la posición real de cada dígito en output:

#for i in range(1, 10):: Recorre los contadores.
#count[i] += count[i - 1]: Acumula los conteos para obtener las posiciones finales.
#Construye el arreglo output:

#i = n - 1: Empieza desde el final del arreglo.
#index = arr[i] // exp: Calcula el dígito actual de arr[i].
#output[count[index % 10] - 1] = arr[i]: Coloca arr[i] en su posición correcta en output.
#count[index % 10] -= 1: Decrementa el contador correspondiente.
#i -= 1: Decrementa el índice.
#Copia el arreglo output en arr:

#for i in range(n):: Recorre cada elemento del arreglo output.
#arr[i] = output[i]: Copia cada elemento a arr.
#Función radix_sort(arr):

#Ordena el arreglo arr utilizando el algoritmo RadixSort.
#Encuentra el número máximo para saber el número de dígitos:

#max_num = max(arr): Encuentra el número máximo en arr.
#Realiza Counting Sort para cada dígito:

#exp = 1: Inicializa el factor de expansión (dígito actual) en 1 (unidades).
#while max_num // exp > 0: Mientras haya más dígitos que ordenar.
#counting_sort(arr, exp): Realiza Counting Sort en función del dígito actual.
#exp *= 10: Incrementa exp por un factor de 10 para pasar al siguiente dígito (decenas, centenas, etc.).
#Lista de ejemplo para ordenar:

#arr = [170, 45, 75, 90, 802, 24, 2, 66]: Define una lista de ejemplo que se desea ordenar.
#Llamada a la función de ordenamiento RadixSort:

#radix_sort(arr): Llama a la función radix_sort pasando la lista arr como argumento.
#Imprime la lista ordenada:

#print("Lista ordenada es:", arr): Imprime la lista arr ya ordenada.
