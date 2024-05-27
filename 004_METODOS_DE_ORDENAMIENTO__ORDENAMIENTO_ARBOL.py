#Practica: 004_METODOS_DE_ORDENAMIENTO__ORDENAMIENTO_ARBOL
#Alumno: Ivan Dominguez
#Registro: 21310234
#Grupo: 6E1

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    # Si el árbol está vacío, devuelve un nuevo nodo
    if root is None:
        return TreeNode(key)
    else:
        # De lo contrario, recorre el árbol
        if key < root.val:
            # Si el valor es menor que el root, inserta en el subárbol izquierdo
            root.left = insert(root.left, key)
        else:
            # Si el valor es mayor que el root, inserta en el subárbol derecho
            root.right = insert(root.right, key)
    return root

def inorder_traversal(root, sorted_list):
    if root:
        # Recorre el subárbol izquierdo
        inorder_traversal(root.left, sorted_list)
        # Agrega el valor del nodo a la lista ordenada
        sorted_list.append(root.val)
        # Recorre el subárbol derecho
        inorder_traversal(root.right, sorted_list)

def tree_sort(arr):
    if len(arr) == 0:
        return arr

    # Inicializa el árbol binario de búsqueda
    root = TreeNode(arr[0])

    # Inserta los elementos en el árbol
    for i in range(1, len(arr)):
        insert(root, arr[i])

    # Realiza el recorrido en orden para obtener la lista ordenada
    sorted_list = []
    inorder_traversal(root, sorted_list)

    # Copia los elementos de la lista ordenada de nuevo al arreglo original
    for i in range(len(arr)):
        arr[i] = sorted_list[i]

# Lista de ejemplo para ordenar
arr = [64, 34, 25, 12, 22, 11, 90]

# Llamada a la función de ordenamiento por árbol
tree_sort(arr)

# Imprime la lista ordenada
print("Lista ordenada es:", arr)



#Descripción del Código:
#Definición de la clase TreeNode:

#Esta clase define un nodo de un árbol binario de búsqueda (BST) con un valor (val), y punteros al hijo izquierdo (left) y al hijo derecho (right).
#Función insert(root, key):

#Inserta un nuevo nodo con el valor key en el árbol BST.
#Si el árbol está vacío, crea un nuevo nodo y lo devuelve.
#Si el valor key es menor que el valor del nodo actual (root.val), inserta el nodo en el subárbol izquierdo.
#Si el valor key es mayor o igual al valor del nodo actual, inserta el nodo en el subárbol derecho.
#Función inorder_traversal(root, sorted_list):

#Realiza un recorrido en orden (in-order traversal) del árbol BST y agrega los valores de los nodos a sorted_list.
#Primero recorre el subárbol izquierdo, luego el nodo actual, y finalmente el subárbol derecho.
#Función tree_sort(arr):

#Ordena la lista arr utilizando un árbol binario de búsqueda.
#Si la lista está vacía, retorna la lista vacía.
#Inicializa el árbol BST con el primer elemento de la lista.
#Inserta los elementos restantes de la lista en el árbol BST.
#Realiza un recorrido en orden del árbol y almacena los valores en sorted_list.
#Copia los elementos de sorted_list de nuevo a la lista original arr.
#Lista de ejemplo para ordenar:

#arr = [64, 34, 25, 12, 22, 11, 90]: Define una lista de ejemplo que se desea ordenar.
#Llamada a la función de ordenamiento por árbol:

#tree_sort(arr): Llama a la función tree_sort pasando la lista arr como argumento.
#Imprime la lista ordenada:

#print("Lista ordenada es:", arr): Imprime la lista arr ya ordenada.
