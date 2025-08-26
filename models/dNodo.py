"""Módulo que implementa la estructura de datos de un nodo de árbol binario."""


class TreeNode:
    """Representa un nodo en un árbol binario."""

    def __init__(self, value):
        """
        Inicializa un nuevo nodo con el valor proporcionado.

        Args:
            value: El valor que almacenará el nodo.
        """
        self._value = value
        self._left = None
        self._right = None

    @property
    def value(self):
        """Devuelve el valor del nodo."""
        return self._value

    @value.setter
    def value(self, new_value):
        """Establece un nuevo valor para el nodo."""
        self._value = new_value

    @property
    def left(self):
        """Devuelve el nodo hijo izquierdo."""
        return self._left

    @left.setter
    def left(self, new_node):
        """Establece el nodo hijo izquierdo."""
        self._left = new_node

    @property
    def right(self):
        """Devuelve el nodo hijo derecho."""
        return self._right

    @right.setter
    def right(self, new_node):
        """Establece el nodo hijo derecho."""
        self._right = new_node