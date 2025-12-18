#Ejemplo 1
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre

#Crea una clase Libro con titulo, autor, mostrar_info().
class Libro:
    def __init__(self,titulo,autor):
        self.titulo = titulo
        self.autor = autor.upper()
    def mostrar_info(self):
        print(f'El nombre del libro es: "{self.titulo}" y el autor es: {self.autor}')

p1 = Libro('No me se ninguno','Aylin')
p1.mostrar_info()

#Crea una clase Cuenta con depositar() y retirar().
class Cuenta:
    #Atributos
    def __init__(self):
        self.saldo = 0
    #Metodos
    def depositar(self,cantidad):
        self.saldo += cantidad
        print(f'Has depositado ${cantidad}. Tu saldo actual es ${self.saldo}')

    def retirar(self,cantidad):
        if (self.saldo >= cantidad):
            self.saldo -= cantidad
            print(f'Retiraste ${cantidad}. Te queda ${self.saldo}')
        else:
            print(f'No te alcanza, tu saldo actual es de ${self.saldo}')

cuenta1 = Cuenta()
cuenta1.depositar(100)
cuenta1.retirar(30)
cuenta1.retirar(100)

