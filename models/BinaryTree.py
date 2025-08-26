"""Módulo que implementa la estructura de datos del árbol binario."""

from .dNodo import TreeNode


class BinaryTree:
    """Representa una estructura de datos de árbol binario."""

    def __init__(self):
        """Inicializa un nuevo árbol binario con un nodo raíz nulo."""
        self.root = None

    def insert(self, value):
        """
        Inserta un nuevo nodo en el árbol.

        El método inserta el valor como un nuevo nodo en una posición
        que mantiene la propiedad de un árbol binario de búsqueda:
        los valores menores van a la izquierda y los mayores o iguales a la derecha.

        Args:
            value: El valor a insertar en el árbol.
        """
        new_node = TreeNode(value)
        if self.root is None:
            self.root = new_node
            return

        current_node = self.root
        while True:
            # ¡Aquí está el cambio! Usamos 'value' en lugar de 'data'
            if value < current_node.value:
                if current_node.left is None:
                    current_node.left = new_node
                    return
                current_node = current_node.left
            else:
                if current_node.right is None:
                    current_node.right = new_node
                    return
                current_node = current_node.right