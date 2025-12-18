'''
Día 3 – Ejercicio de lógica
Reto:
Escribe un programa que pida al usuario un número entero positivo y genere la tabla de multiplicar de ese número, desde 1 hasta 10.
Condiciones mínimas:
- El programa debe rechazar entradas no numéricas con try/except.
- El programa debe rechazar números menores o iguales a 0.
- El resultado debe mostrarse en formato claro, por ejemplo:
7 x 1 = 7
7 x 2 = 14
...
7 x 10 = 70
- Debe usar un bucle para generar la tabla, no imprimir línea por línea manualmente.
'''
while True:
    try:
        x = int(input("Ingresa un numero para saber la multiplicacion: "))
        res = 0
        if(x > 0):
            for i in range(10):
                    res = x * (i+1)
                    print(f'{x} x {i+1} = {res}')
            break
        else:
            print("Debe ser mayor que 0")        
    except ValueError:
        print("Debe ser un numero y un valor mayor que 0")
