print("*** Suma Acumulativa ***")

# Sumar los primeros 5 numeros
Maximo = 5
numero = 1
acumulador_suma = 0

#Empezamos a iterar
while numero <= Maximo:
    acumulador_suma += numero
    numero += 1
print(f'\nLa suma de todos los numeros es {acumulador_suma}')