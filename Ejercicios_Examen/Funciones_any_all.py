#Ejemplo any
valores = [False, True, False]

if any(valores):
    print("Hay al menos un valor verdadero en la lista")
else:
    print("No hay valores verdaderos")

#Ejemplo all
valores = [True, True, True]

if all(valores):
    print("todos son valores verdaderos en la lista")
else:
    print("No hay valores verdaderos")

#Verifica si todos los elementos de una lista son mayores que 0
numeros = [45,2,54,365]
if all(num > 0 for num in numeros):
    print("Todos son mayores que 0")
else:
    print("Hay un numero menor o igual que 0")

#Verifica si al menos uno es divisible entre 3
numeros = [45,2,54,365]
if any(num % 3 == 0 for num in numeros):
    print("Hay un numero divisible entre 3")
else:
    print("Hay un numero que no es divisible")