#** 🟢 Nivel 1: Revisión de condiciones **
#Ejercicio 1
#Recorre una lista de números e imprime solo los que sean positivos.
lista = [40,25,-5,77]

for num in lista:
    if(num > 0):
        print(num)

#Ejercicio 2
#Cuenta cuántos números en una lista son pares.
lista = [40,25,-5,77,78]
x = 0

for num in lista:
    if(num % 2 == 0):
        x = x + 1
print(x)

#** 🟡 Nivel 2: Acumulación y transformación
#Ejercicio 3
#Suma todos los números mayores que 5 en una lista.
lista = [0,25,5,77,2]
x = 0

for num in lista:
    if(num > 5):
        x = x + num
print(x)

#Ejercicio 4
#Crea una nueva lista que contenga los cuadrados de los números originales.
lista = [0,25,5,77,2]
x = []

for num in lista:
    num = num**2
    x.append(num)
print(lista)
print(x)

#** 🟠 Nivel 3: Lógica combinada y validaciones
#Ejercicio 5
#Verifica si todos los números de una lista son múltiplos de 3.
lista = [36,27,6,75,90]

if all(num % 3 == 0 for num in lista):
    print("Todos son multiples de 3")
else:
    print("Hay uno o mas numeros no multiples de 3")

#Ejercicio 6
#Clasifica los números en dos listas: una para pares y otra para impares.
lista = [36,27,6,75,90]
x = []
y = []

for num in lista:
    if(num % 2 == 0):
        x.append(num)
    else:
        y.append(num)
print(lista)
print(f'La lista de pares es: {x}')
print(f'La lista de impares es: {y}')

#** 🔴 Nivel 4: Aplicaciones más complejas
#Ejercicio 7
#Encuentra el número más grande en una lista sin usar max().
lista = [36,12747,6,75,8546,90,200]
Mayor = lista[0]

for num in lista:
    if(num >= Mayor):
        Mayor = num
print(f'El numero mayor es: {Mayor}')

#Ejercicio 7.5
#Recorre una lista de números y encuentra el valor más pequeño sin usar la función min().
lista = [36,12747,6,75,8546,90,200]
menor = lista[0]

for num in lista:
    if(num <= menor):
        menor = num
print(f'El numero menor es: {menor}')

#Ejercicio 8
#Crea una lista que contenga solo los números que son divisibles por 2 y por 5.
lista = [36,12747,6,75,10000,90,200]
x = []

for num in lista:
    if(num % 2 == 0 and num % 5 == 0):
        x.append(num)
print(x)

