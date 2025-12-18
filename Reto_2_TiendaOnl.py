compra = int(input("Cuanto compro? "))
miembro = str(input("Es miembro? "))

if (miembro == 'Si' or miembro == 'SI' or miembro == 'si'):
    miembro = True
    if (compra >= 1000 and miembro == True):
        compra = compra - (0.1*compra)
    elif(compra < 1000 and miembro == True):
         compra = compra - (0.05*compra)
elif(compra > 1000):
     compra = compra - (0.05*compra)
else:
    print(f'No hay descuento, el total es: {compra}')
print(f'El total a pagar es: {compra}')