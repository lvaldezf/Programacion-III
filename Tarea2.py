def convertir_a_binario(numero):
    if numero == 0:
        return '0'
    else:
        return convertir_a_binario(numero // 2) + str(numero % 2)

def contar_digitos(numero):
    if numero < 10:
        return 1
    else:
        return 1 + contar_digitos(numero // 10)

def menu_interactivo():
    print("Menú Interactivo:")
    print("1. Convertir a Binario")
    print("2. Contar Dígitos")
    opcion = int(input("Selecciona una opción (1-2): "))

    if opcion == 1:
        numero = int(input("Ingresa un número entero: "))
        print("En binarios", convertir_a_binario(numero))
    elif opcion == 2:
        numero = int(input("Ingresa un número entero: "))
        print("Cantidad de dígitos:", contar_digitos(numero))
    else:
        print("Opción no válida. Inténtalo nuevamente.")

if __name__ == "__main__":
    menu_interactivo()
