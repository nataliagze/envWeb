from models.dNodo import TreeNode
from models.BinaryTree import BinaryTree


# Crear una instancia del arbol
my_tree = BinaryTree()

# Insertar varios nodos
print("Insertando nodos en el arbol...")
my_tree.insert(50)
my_tree.insert(30)
my_tree.insert(70)
my_tree.insert(20)
my_tree.insert(40)
my_tree.insert(60)
my_tree.insert(80)

print("Nodos insertados.")

# Verificar la estructura
print("\nVerificando la estructura del arbol:")
print(f"Nodo raiz: {my_tree.root.value}")
print(f"Hijo izquierdo de la raiz: {my_tree.root.left.value}")
print(f"Hijo derecho de la raiz: {my_tree.root.right.value}")

# Para correr: python test_arbol.py