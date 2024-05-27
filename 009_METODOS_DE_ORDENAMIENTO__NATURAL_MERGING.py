#Practica: 009_METODOS_DE_ORDENAMIENTO__NATURAL_MERGING
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

def natural_merge_sort(arr):
    # Función para encontrar las subsecuencias ordenadas naturales en la lista
    def find_runs(arr):
        runs = []
        new_run = [arr[0]]
        
        for i in range(1, len(arr)):
            if arr[i] >= arr[i - 1]:
                new_run.append(arr[i])
            else:
                runs.append(new_run)
                new_run = [arr[i]]
        runs.append(new_run)
        
        return runs

    # Función para mezclar dos sublistas ordenadas
    def merge(left, right):
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        while i < len(left):
            result.append(left[i])
            i += 1
        
        while j < len(right):
            result.append(right[j])
            j += 1
        
        return result

    # Función principal del algoritmo de mezcla natural
    def merge_pass(runs):
        new_runs = []
        i = 0
        
        while i < len(runs):
            if i + 1 < len(runs):
                new_runs.append(merge(runs[i], runs[i + 1]))
                i += 2
            else:
                new_runs.append(runs[i])
                i += 1
        
        return new_runs

    # Realiza la ordenación por mezcla natural
    runs = find_runs(arr)
    
    while len(runs) > 1:
        runs = merge_pass(runs)
    
    # Copia la lista ordenada de nuevo en arr
    arr[:] = runs[0]

# Lista de ejemplo para ordenar
arr = [64, 34, 25, 12, 22, 11, 90]

# Llamada a la función de ordenamiento Natural Merging
natural_merge_sort(arr)

# Imprime la lista ordenada
print("Lista ordenada es:", arr)



#Descripción del Código:
#Definición de la función natural_merge_sort(arr):

#Esta función toma una lista arr como argumento y la ordena en su lugar utilizando el algoritmo de Natural Merging.
#Función find_runs(arr):

#Encuentra las subsecuencias ordenadas naturales en la lista arr.
#Inicializa una lista runs para almacenar las subsecuencias.
#Inicializa new_run con el primer elemento de arr.
#Recorre la lista arr:
#Si el elemento actual es mayor o igual al anterior, lo agrega a new_run.
#Si el elemento actual es menor, añade new_run a runs y empieza una nueva subsecuencia.
#Añade la última subsecuencia a runs.
#Función merge(left, right):

#Mezcla dos sublistas ordenadas (left y right) en una lista ordenada.
#Inicializa una lista result vacía para almacenar el resultado de la mezcla.
#Inicializa los índices i y j para recorrer las sublistas left y right, respectivamente.
#Compara los elementos de left y right, y agrega el menor a result.
#Si se agotan los elementos de left, agrega los elementos restantes de right a result.
#Si se agotan los elementos de right, agrega los elementos restantes de left a result.
#Retorna la lista result mezclada y ordenada.
#Función merge_pass(runs):

#Realiza una pasada de mezcla sobre las subsecuencias ordenadas en runs.
#Inicializa una lista new_runs para almacenar las nuevas subsecuencias mezcladas.
#Recorre runs de dos en dos:
#Si hay dos subsecuencias, las mezcla y añade el resultado a new_runs.
#Si hay una sola subsecuencia, la añade directamente a new_runs.
#Retorna new_runs.
#Realiza la ordenación por mezcla natural:

#Encuentra las subsecuencias ordenadas naturales en arr llamando a find_runs(arr).
#Mientras haya más de una subsecuencia en runs, realiza pasadas de mezcla llamando a merge_pass(runs).
#Copia la lista ordenada resultante de nuevo en arr.
#Lista de ejemplo para ordenar:

#arr = [64, 34, 25, 12, 22, 11, 90]: Define una lista de ejemplo que se desea ordenar.
#Llamada a la función de ordenamiento Natural Merging:

#natural_merge_sort(arr): Llama a la función natural_merge_sort pasando la lista arr como argumento.
#Imprime la lista ordenada:

#print("Lista ordenada es:", arr): Imprime la lista arr ya ordenada.
