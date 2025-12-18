'''Reto:
Escribe un programa que pida al usuario un número entero positivo y determine si es par o impar.
Condiciones mínimas:
- El programa debe rechazar entradas no numéricas (ejemplo: “hola” → error controlado).
- El programa debe rechazar números negativos o cero.
- El resultado debe ser claro: "El número X es par" o "El número X es impar".
Pistas (no solución completa):
- Usa input() para pedir el número.
- Convierte con int(), pero captura errores con try/except.
- Valida que el número sea mayor que 0.
- Usa el operador módulo % para comprobar si es par o impar.
'''
while True:
    try:
        x = int(input("¿Cual es el numero? "))
        if(x > 0):
            if(x % 2 == 0):
                print(f'El numero {x} es par')
                break
            else:
                print(f'El numero {x} es impar')
                break
    except ValueError:
        print("Debe ser un numero y un valor mayor que 0")
