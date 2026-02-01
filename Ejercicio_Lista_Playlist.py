print('***  Playlist de canciones ***')

#Creamos la lista vacia
Lista_Reproduccion = []

#Empezamos a agregar canciones
Lista_Reproduccion.append('Hotel California - Eagles')
Lista_Reproduccion.append('Staying Alive - Bee Gees')
Lista_Reproduccion.append('Dream on - Aerosmith')

#Obtener la lista en orden alfabetico.sort
#Lista_Reproduccion.sort(reverse=True)
Lista_Reproduccion.sort()

#Mostrar lista de canciones
print(f'\n Lista de canciones en orden alfabetico: {Lista_Reproduccion}')

for cancion in Lista_Reproduccion:
    print(f'- {cancion}')