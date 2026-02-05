'''Día 7 Ejercicio de lógica con listas
Reto:
Escribe un programa que pida al usuario una lista de números enteros positivos (la cantidad la decides tú, por ejemplo 7).
El programa debe:
- Rechazar entradas no numéricas y números menores o iguales a 0.
- Guardar todos los números en una lista.
- Mostrar la lista completa.
- Mostrar solo los números pares de la lista.
- Mostrar solo los números impares de la lista.
- Mostrar la suma de los pares y la suma de los impares por separado.

Condiciones mínimas:
- Usa un bucle para pedir los números.
- Usa condiciones (if) para separar pares e impares.
- El resultado debe mostrarse claramente en el formato:
Lista: [2, 5, 7, 10, 3, 8, 4]
Pares: [2, 10, 8, 4]
Impares: [5, 7, 3]
Suma pares: 24
Suma impares: 15
'''
while True:
    try:
        x = []
        y = []
        z = []
        a = 0
        b = 0
        c = 0
        print("Da 7 numeros positivos")
        for i in range (7):
            a = int(input(f'Dame el {i+1}° numero: '))
            if (a > 0):
                x.append(a)
                if (a % 2 == 0):
                    y.append(a)
                    #b += 1 
                else:
                    z.append(a)
                    #c += 1

        print(f'Lista: {x}')
        print(f'Pares: {y}')
        print(f'Impares: {z}')
        print(f'Suma pares: {sum(y)}')
        print(f'Suma impares: {sum(z)}')
        break
    except ValueError: 
        print("Debe ser un numero")