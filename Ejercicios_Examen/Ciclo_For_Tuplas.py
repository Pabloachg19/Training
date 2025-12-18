#Ejemplo 1
for num in [1, 2, 3]:
    print(num)

#Ejemplo 2
#a, b, c = (10, 20, 30)
a = b = c = (10, 20, 30)

print(a,b)

#Recorre una lista de números e imprime solo los pares.
lista = [36,12747,6,75,8546,90,200]

for num in lista:
    if(num % 2 == 0):
        print(num)

#Desempaqueta una tupla (nombre, edad, ciudad) y muestra cada valor.
nombre, edad, ciudad = ('Pablo',25,'Tepecoacuilco')

print(f'El nombre es: {nombre}, su edad es: {edad} y su ciudad es: {ciudad}')