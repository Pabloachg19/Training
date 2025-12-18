#Generador de Email

#1 Colocar los valores que llevará el email
nombre = 'Pablo Antonio Chavez Gongora'
empresa = 'Capgemini Engineering'
dominio = 'com.mx'

#Acomodar los valores
nombre = nombre.lower()
nombre = nombre.replace(" ",".")

empresa = empresa.lower().replace(" ","")

#Imprimir el email
print(nombre + "@" + empresa + "." + dominio)