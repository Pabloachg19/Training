'''Día 4 – Ejercicio de lógica
Reto:
Escribe un programa que pida al usuario 5 números enteros positivos y los guarde en una lista.
Al final, el programa debe mostrar:
- La lista completa de números ingresados.
- El número mayor.
- El número menor.
- El promedio de los números.

Condiciones mínimas:
- El programa debe rechazar entradas no numéricas con try/except.
- El programa debe rechazar números menores o iguales a 0.
- Debe usar una lista para almacenar los valores.
- Debe usar un bucle para pedir los 5 números, no repetir código manualmente.
- El resultado debe mostrarse claramente en el formato:
Lista: [2, 5, 7, 10, 3]
Mayor: 10
Menor: 2
Promedio: 5.4
'''
try:
    x = []
    for i in range(5):
         a = int(input(f'Ingresa el {i+1}° valor: '))
         x.append(a)
    print(f'Lista: {x}')
    print(f'Mayor: {max(x)}')
    print(f'Menor: {min(x)}')
    print(f'Promedio: {sum(x)/len(x)}')
except ValueError:
    print("Debes ingresar 5 numeros enteros positivos")