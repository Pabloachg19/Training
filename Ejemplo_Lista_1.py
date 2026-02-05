print('*** Manejo de listas ***')
mi_lista = [1,2,3,4,5]
print(f'{mi_lista}')

#Largo de una lista
print(f'Largo de mi lista: {len(mi_lista)}')

#Acceder a los elementos de la lista
print(f'Accedemos al valor del indice 4: {mi_lista[4]}')
print(f'Accedemos al ultimo indice de la lista: {mi_lista[-1]}')

#Modificar elementos por medio del indice
mi_lista[1] = 10
print(f'{mi_lista}')

#Agregar elementos a una lista
mi_lista.append(6)
print(f'Lista con el nuevo elemento agregado: {mi_lista}')

#Añadir un numero elemento a un indice especifico
mi_lista.insert(2, 15)
print(f'Se cambió un elemento en el indice 2 --> {mi_lista}')

#Eliminar elementos de una lista usando el metodo remove
mi_lista.remove(15)
print(f'{mi_lista}')

#Removemos con el indice con el metodo pop
mi_lista.pop(1) #Remueve el elemento del indice 1
print(f'{mi_lista} -> Se eliminó el indice 1')

#Eliminar usando la palabra del
del mi_lista[2]
print(f'{mi_lista}')

#Obtener sublistas
sublista = mi_lista[1:3] #Genera una sublista del indice 1 al 2 (3 no se incluye)
print(f'La vieja lista es: {mi_lista} y la nueva lista es: {sublista}')