'''
Día 2 Ejercicio de lógica
Reto:
Escribe un programa que pida al usuario un número entero positivo y calcule la suma de todos los números desde 1 hasta ese número.
Condiciones mínimas:
- El programa debe rechazar entradas no numéricas con try/except.
- El programa debe rechazar números menores o iguales a 0.
- El resultado debe mostrarse claramente:
- Ejemplo: "La suma de los números del 1 al 10 es 55".
- El cálculo debe hacerse con un bucle, no con funciones predefinidas como sum(range(...)). Quiero ver tu lógica, no un atajo.'''
while True:
    try:
        x = int(input("Ingresa un numero de 1 en adelante: "))
        y = 1
        res = 0
        if(x > 0):
            while y <= x:
                res += y
                y += 1
            print(f'La suma de los números del 1 al {x} es {res}')
            break
        else:
            print("Debe ser mayor que 0")        
    except ValueError:
        print("Debe ser un numero y un valor mayor que 0")
