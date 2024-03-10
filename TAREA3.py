import graphviz

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        # Implement your logic to insert a value into the tree
        pass

    def search(self, value):
        # Implement your logic to search for a value in the tree
        pass

    def delete(self, value):
        # Implement your logic to delete a value from the tree
        pass

    def load_from_file(self, filename):
        # Implement your logic to load data from a .txt file and build the tree
        pass

    def to_graphviz(self):
        # Generate Graphviz representation of the tree
        dot = graphviz.Digraph()
        self._add_nodes_to_graphviz(self.root, dot)
        return dot

    def _add_nodes_to_graphviz(self, node, dot):
        if node:
            dot.node(str(node.value))
            if node.left:
                dot.edge(str(node.value), str(node.left.value))
                self._add_nodes_to_graphviz(node.left, dot)
            if node.right:
                dot.edge(str(node.value), str(node.right.value))
                self._add_nodes_to_graphviz(node.right, dot)

def main():
    tree = BinarySearchTree()

    while True:
        print("\nMenú:")
        print("1. Insertar")
        print("2. Buscar")
        print("3. Eliminar")
        print("4. Cargar desde Archivo")
        print("5. Convertir a binario")
        print("6. Salir")

        choice = input("Selecciona una opción: ")

        if choice == "1":
            value = int(input("Ingresa el número a insertar: "))
            tree.insert(value)
        elif choice == "2":
            value = int(input("Ingresa el número a buscar: "))
            result = tree.search(value)
            print(f"El número {value} {'está' if result else 'no está'} en el árbol.")
        elif choice == "3":
            value = int(input("Ingresa el número a eliminar: "))
            tree.delete(value)
        elif choice == "4":
            filename = input("Ingresa la ruta del archivo .txt: ")
            tree.load_from_file(filename)
        elif choice == "5":
            dot = tree.to_graphviz()
            dot.render("tree", format="png", cleanup=True)
            print("Árbol binario convertido a formato binario (PNG).")
        elif choice == "6":
            break
        else:
            print("Opción inválida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
