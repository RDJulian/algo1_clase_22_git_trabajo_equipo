from divisionEntera import divisionEntera
from suma import suma


def main():
    salir = False
    while not salir:
        opcion = input("Ingrese una operacion: ")
        unNumero = int(input("Ingrese un numero: "))
        otroNumero = int(input("Ingrese otro numero: "))
        if opcion == '1':
            suma(unNumero, otroNumero)
        elif opcion == '2':
            try:
                divisionEntera(unNumero, otroNumero)
            except ValueError:
                print("Intento hacer una division entera con divisor 0. Intente nuevamente.")
        elif opcion == '3':
            salir = True


main()
