from calculadora import sumar_dos_numeros, restar_dos_numeros

#Programa Principal (interfaz gráfica - print, input)
while True:
    opcion=input("Ingrese S para sumar, R para restar, M para multiplicar y X para Salir").lower()

    if opcion=="x":
        break
    elif opcion=="s":
        n1=int(input("Ingrese el número 1: "))
        n2=int(input("Ingrese el número 2: "))
        print(f"El resultado de la suma es : {sumar_dos_numeros(n1,n2)}")
    elif opcion=="r":
        n1=int(input("Ingrese el número 1: "))
        n2=int(input("Ingrese el número 2: "))
        print(f"El resultado de la resta es : {restar_dos_numeros(n1,n2)}")
    else:
        print("El valor ingresado no es válido. Por favor intente nuevamente.")