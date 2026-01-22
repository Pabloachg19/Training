'''Día 6  Ejercicio de lógica con números y texto
Reto:
Escribe un programa que pida al usuario una frase y un número entero positivo.
El programa debe:
- Rechazar frases vacías.
- Rechazar números menores o iguales a 0.
- Mostrar la frase repetida tantas veces como indique el número.
- Numerar cada repetición en el formato:
1: Hola mundo
2: Hola mundo
3: Hola mundo
Condiciones mínimas:
- Usa un bucle para controlar las repeticiones.
- Valida tanto la frase como el número.
- El resultado debe ser claro y ordenado.
'''
while True:
    x = input("Ingresa una frase: ")
    y = int(input("Ingresa un valor: "))
    if len(x) != 0 and y >= 0:
        for i in range(y):
            print(f'{i+1}: {x}')
        break
    else:
        print("Debe haber una frase para continuar")
