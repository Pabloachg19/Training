"""
#Nivel 1: Fundamentos
#Ejercicio 1
class Producto:
    #Atributos
    def __init__(self,nombre,precio):
        self.nombre = nombre
        self.precio = precio
    #Metodos
    def mostrar_info(self):
        print(f'El nombre es {self.nombre} y el precio es {self.precio}')
    
Producto1 = Producto('Chocomilk',78)
Producto1.mostrar_info()

#Ejercicio 2
class Rectangulo:
    #Atributos
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
    #Metodos
    def calcular_area(self):
        print(f'El area del rectangulo es: {self.base * self.altura}')

base = int(input(f'Ingresa la base del rectangulo: '))
altura = int(input(f'Ingresa la altura del rectangulo: '))
area1 = Rectangulo(base,altura)
area1.calcular_area()

#Ejercicio 3
class Estudiante:
    #Atributos
    def __init__(self,nombre,notas):
        self.nombre = nombre
        self.notas = notas
    #Metodos
    def promedio(self):
        promedio = sum(notas)/len(notas)
        print(f'El promedio del alumno: {self.nombre} es de {self.notas}')

nombre = str(input(f'Ingresa el nombre '))
notas = []
a = int(input(f'Cuantas notas agregaras? '))
while (a > 0):
    notas.append(int(input(f'Ingresa la nota: ')))
    a -= 1
promedio = sum(notas)/len(notas)
print(f'El promedio de las notas del alumno {nombre} es de {promedio}')"""

'''#Ejercicio 4
class CuentaBancaria:
    #Atributos
    def __init__(self,titular,saldo):
        self.titular = titular
        self.saldo = saldo
    #Metodos
    def depositar(self,cantidad):
        self.saldo += cantidad
    def retirar(self,cantidad):
        if(self.saldo > cantidad):
            self.saldo -= cantidad
        else:
            print(f'Fondos insuficientes, tienes ${self.saldo}')
    def mostrar_saldo(self):
        print(f'Tu saldo actual es: ${self.saldo}')

CB1 = CuentaBancaria('Pablo',5000)
CB1.depositar(500)
CB1.mostrar_saldo()
CB1.retirar(8000)'''

'''#Ejercicio 5
class Temperatura:
    #Atributo
    def __init__(self,grados_celsius):
        self.grados_celsius = grados_celsius
    #Metodos
    def a_fahrenheit(self):
        self.Far = self.grados_celsius*(9/5) + 32
        print(self.Far)
    def estado(self):
        if(self.grados_celsius > 50):
            print(f'Esta muy caliente')
        elif(self.grados_celsius < 15):
            print(f'El clima es muy frio')
        else:
            print(f'El clima es templano')
temp1 = Temperatura(10)
temp1.a_fahrenheit()
temp1.estado()'''

'''#Ejercicio 6
class Carro:
    #Atributos
    def __init__(self,marca,modelo,encendido):
        self.marca = marca
        self.modelo = modelo
        self.encendido = encendido
    #Metodos
    def encender(self):
        self.encendido = True
    def apagar(self):
        self.encendido = False
    def estado(self):
        print(f'El estado del vehiculo es el siguiente: \nMarca: {self.marca}\nModelo: {self.modelo}\nEncendido? {self.encendido}')

Carro1 = Carro("Seat",'Ibiza',False)
Carro1.estado()
Carro1.encender()
Carro1.estado()
Carro1.apagar()
Carro1.estado()'''

#Ejercicio 7
class Libro:
    #Atributos
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
    #Metodos
    def mostrar_info(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}")

class Biblioteca:
    #Atributos
    def __init__(self):
        self.libros = [] #Lista para guardar objetos Libro
    #Metodos
    def agregar_libro(self,libro):
        self.libros.append(libro)
        print(f'Libro {libro.titulo} agregado a la biblioteca.')
    def mostrar_libros(self):
        if not self.libros:
            print("La biblioteca está vacía.")
        else:
            print("Libros en la biblioteca:")
            for libro in self.libros:
                libro.mostrar_info()
    def eliminar_libro(self,titulo):
       for libro in self.libros:
            if libro.titulo == titulo:
                self.libros.remove(libro)
                print(f"Libro '{titulo}' eliminado de la biblioteca.")
                return
            print(f"No se encontró el libro '{titulo}'.")



libro1 = Libro("1984", "George Orwell")
libro2 = Libro("Cien años de soledad", "Gabriel García Márquez")

mi_biblioteca = Biblioteca()
mi_biblioteca.agregar_libro(libro1)
mi_biblioteca.agregar_libro(libro2)

mi_biblioteca.mostrar_libros()

mi_biblioteca.eliminar_libro("1984")
mi_biblioteca.mostrar_libros()

mi_biblioteca.eliminar_libro("El Principito")  # No existe

    

