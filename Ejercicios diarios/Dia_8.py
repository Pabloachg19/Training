'''
Día 8 Ejercicio con diccionarios
Reto:
Escribe un programa que simule un registro de estudiantes.
El programa debe:
- Pedir al usuario el nombre y la edad de 3 estudiantes.
- Guardar cada estudiante en un diccionario con las claves "nombre" y "edad".
- Guardar esos diccionarios dentro de una lista.
- Al final, mostrar:
- La lista completa de estudiantes.
- El estudiante con mayor edad.
- El estudiante con menor edad.

Condiciones mínimas:
- Validar que la edad sea un número entero positivo.
- Validar que el nombre no esté vacío.
- Usar diccionarios para cada estudiante y una lista para agruparlos.
- Mostrar los resultados en un formato claro, por ejemplo:
Lista: [{'nombre': 'Ana', 'edad': 20}, {'nombre': 'Luis', 'edad': 22}, {'nombre': 'Marta', 'edad': 19}]
Mayor edad: Luis (22)
Menor edad: Marta (19)
'''
Estudiantes = {
    "nombre",
    "edad"
}
for i in range(3):
    Estudiantes["nombre"] = input(f'Nombre: ')
    Estudiantes["edad"] = int(input(f'Edad: '))
Estudiantes