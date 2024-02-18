class Node:
    def __init__(self, carnet, nombre, apellido):
        self.carnet = carnet
        self.nombre = nombre
        self.apellido = apellido
        self.next = None
        self.prev = None

class colainicio:
    def __init__(self):
        self.head = None
        self.tail = None

    def push(self, carnet, nombre, apellido, at_end=False):
        new_node = Node(carnet, nombre, apellido)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        elif at_end:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def eliminar_por_valor(self, dato):
        current = self.head
        while current:
            if current.carnet == dato:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev
                return
            current = current.next
        print("El valor no existe")

    def mostrar_lista(self):
        current = self.head
        print("--", end="-- ")
        while current:
            print(f"{current.carnet} {current.nombre} {current.apellido} --", end=" ")
            current = current.next
        print("None")


def menu():
    print("Menú:")
    print("1. Insertar al inicio de la lista")
    print("2. Insertar al final de la lista")
    print("3. Eliminar de la lista")
    print("4. Ver lista")
    print("5. Salir")
    opcion = input("Ingrese el numero de la opcion")
    return opcion


if __name__ == "__main__":
    lista = colainicio()

    while True:
        opcion = menu()

        if opcion == "1":
            carnet = input("Ingrese el carnet: ")
            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido: ")
            lista.push(carnet, nombre, apellido)
        elif opcion == "2":
            carnet = input("Ingrese el carnet: ")
            nombre = input("Ingrese el nombre: ")
            apellido = input("Ingrese el apellido: ")
            lista.push(carnet, nombre, apellido, at_end=True)
        elif opcion == "3":
            dato = input("Ingrese el carnet para eliminar los registros ")
            lista.eliminar_por_valor(dato)
        elif opcion == "4":
            lista.mostrar_lista()
        elif opcion == "5":
            print("Adios")
            break
        else:
            print("Digite un valor valido")

