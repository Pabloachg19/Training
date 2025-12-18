#Sistema de reservacion de hotel

#1.- Pedimos los valores del cliente
nombre = input("Nombre: ")
dias = int(input("Dias de estancia: "))
tarifa = float(input("Precio: "))
Vista = bool(input("Quiere vista al mar? "))

#2.- Mostramos los valores
print("*** Sistema de Reserva de Hoteles ***\nCliente: ",nombre,
      "\nDias de estancia: ",dias,"\nTarifa diaria: ",tarifa,"\nHabitacion con vista al mar? ",Vista)
   