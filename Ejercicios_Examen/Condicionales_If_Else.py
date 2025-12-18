#Recibe un numero y clasificalo como positivo, negativo o cero
x = float(input("Ingresa cualquier numero: "))

if x > 0:
    print("Tu numero es positivo")
elif x < 0:
    print("Tu numero es negativo")
else:
    print("Tu numero es cero")


#- Recibe una nota (0–100) y devuelve A, B, C, D o F
x = int(input("Ingresa la nota del 0 a 100: "))

if x <= 20:
    print("Tu nota es F")
elif x > 20 & x <= 40:
    print("Tu nota es D")
elif x > 40 & x <= 60:
    print("Tu nota es C")
elif x > 60 & x <= 80:
    print("Tu nota es B")
else:
    print("Tu nota es A")