#** Calculadora ***
x = 0
while x != 5:
    x = int(input("Operaciones que puedes realizar:\n 1.- Suma\n 2.- Resta\n 3.- Multiplicacion\n 4.- Division\n 5.- Salir\n"))
    if x == 1:
        a= int(input("Ingresa el primer valor para sumar: "))
        b= int(input("Ingresa el primer valor para sumar: "))
        res = a + b
        print(f'La suma es : {res}')
    elif x == 2:
        a= int(input("Ingresa el primer valor para restar: "))
        b= int(input("Ingresa el primer valor para restar: "))
        res = a - b
        print(f'La resta es : {res}')
    elif x == 3:
        a= int(input("Ingresa el primer valor para multiplicar: "))
        b= int(input("Ingresa el primer valor para multiplicar: "))
        res = a * b
        print(f'La multiplicacion es : {res}')
    elif x == 4:
        a= int(input("Ingresa el primer valor para dividir: "))
        b= int(input("Ingresa el primer valor para dividir: "))
        res = a / b
        print(f'La division es : {res}')
    elif x == 5:
        print("Gracias por usar la calculadora :)")
    else:
        print("Ingresa una opcion del menu")