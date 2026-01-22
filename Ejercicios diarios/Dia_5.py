'''Día 5 – Ejercicio de lógica con cadenas
Reto:
Escribe un programa que pida al usuario una palabra y determine:
- Si la palabra es un palíndromo (se lee igual de izquierda a derecha que de derecha a izquierda).
- La longitud de la palabra.
- La palabra en mayúsculas y en minúsculas.

Condiciones mínimas:
- El programa debe rechazar entradas vacías (no se puede aceptar un string vacío).
- El programa debe funcionar con cualquier palabra, sin importar mayúsculas o minúsculas.
- El resultado debe mostrarse claramente en el formato:
Palabra: radar
Es palíndromo: Sí
Longitud: 5
Mayúsculas: RADAR
Minúsculas: radar
- Debe usar un bucle para validar que la entrada no esté vacía.
'''
while True:
    x = input("Escribe una palabra para saber si es palindromo: ")
    if len(x) != 0:
        x2 = "".join(reversed(x))
        if x == x2:
            print("Es palíndromo: Sí")
            print(f'Longitud: {len(x)}')
            print(f'Mayúsculas: {x.upper()}')
            print(f'Minúsculas: {x.lower()}')
        else:
            print("Es palindromo: No")
        break
    else:
        print("No se aceptan entradas vacias")


