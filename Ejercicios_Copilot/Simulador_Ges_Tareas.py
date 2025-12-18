class Tarea:
    #Atributos
    def __init__(self,titulo,descripcion,completada = False):
        self.titulo = titulo
        self.descripcion = descripcion
        self.completada = completada
    #Metodos
    def marcar_completada(self):
        self.completada = True
    def mostrar_info(self):
        if self.completada: #(self.completada == True):
            print(f'El titulo es: {self.titulo} \nLa descripcion es: {self.descripcion} \nEstado: ✅ Completada')
        else:
            print(f'El titulo es: {self.titulo} \nLa descripcion es: {self.descripcion} \nEstado: ⏳ Pendiente')

t1 = Tarea("Enviar informe", "Enviar el informe mensual al jefe")
t1.mostrar_info()
t1.marcar_completada()
t1.mostrar_info()

class GestorTareas:
    #Atributos
    def __init__(self):
        self.tareas = []
    #Metodos
    def agregar_tarea(self,titulo, descripcion):
        nueva_tarea = Tarea(titulo, descripcion)
        self.tareas.append(nueva_tarea)
    def mostrar_todas(self):
        if not self.tareas:
            print("No hay tareas registradas")
        else:
            print("📋 Lista de todas las tareas:")
            for tarea in self.tareas:
                tarea.mostrar_info()
                print("-" * 30)
    def mostrar_pendientes(self):
        print("📋 Lista de todas las tareas pendientes:")
        print("*" * 30)
        for tarea in self.tareas:
            if (tarea.completada == False):
                tarea.mostrar_info()
                print("*" * 30)
            else:
                print("No hay tareas pendientes")
    def marcar_completada(self,titulo):
        self.titulo = titulo
        for tarea in self.tareas:
            if tarea.titulo.upper() == titulo.upper():
                if tarea.completada == False:
                    tarea.completada = True
                    print("Se ha completado la tarea")
                else:       
                    print("Esta tarea ya se ha completado")
            else:
                print("Esta tarea no está en la lista")

                

gestor = GestorTareas()
gestor.agregar_tarea("Enviar informe", "Enviar el informe mensual al jefe")
gestor.agregar_tarea("Revisar código", "Revisar el módulo de autenticación")
gestor.mostrar_todas()
gestor.mostrar_pendientes()
gestor.marcar_completada("Enviar informe")
gestor.mostrar_pendientes()
#gestor.eliminar_tarea("Revisar código")
#gestor.mostrar_todas()

