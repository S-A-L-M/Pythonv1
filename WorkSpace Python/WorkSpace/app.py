x = 4         # x is now of type int
x = "Wendy"   # x is now of type str
print(x)

#--------------------------------------------------------------------

'''
 MENSAJE D EPRUE
 Otro mensaje de prueba
'''

#--------------------------------------------------------------------

#Casting
x = str(3)   # x will be '3'
print(x)  #Imprimos el valor d x

z = float(4) # x will be '4.0' mean decimal
print(z) #Imprimimos el valor de z

#--------------------------------------------------------------------

#Get the Type

x = 5
y = "3"
print(type(x)) #Sabe el Tipo de Dato és
print(type(y)) #Sabe el Tipo de Dato és

#--------------------------------------------------------------------

#Pedir dato y luego Imprimirlo
nombre  = input("Ingresa tu Nombre") #Pedir dato
print("Tu Nombre ingresado es:", nombre) #Imprimir dato

#--------------------------------------------------------------------

#SuMAR NUMERO
numero1 = input ("Ingresa el Primer Numero: ") #Pedimos un Numero tipo input(es como un Systemout.print)
numero2 = input ("Ingresa el Segundo Numero: ") #Pedimos otro  Numero tipo input(es como un Systemout.print)

numero1 = int(numero1) #Declaramos que numero1 es tipo entero o numérico
numero2 = int(numero2) #Declaramos que también numero2 es tipo entero o numérico
    
resultado = numero1 + numero2 #Realizamos la operación siguiente, es decir el resultado es igual al valor que el usuario haya ingresado en el numero 1 y numero 2

print("El Resultado es", resultado) #Imprimir el resultado
          
#--------------------------------------------------------------------

#Condicionales
numero = int(input('favor digitar un numero:'))
if numero > 0:
    print(f'el valor del numero es: {numero} y es positivo')
elif numero < 0:
    print(f'el valor del numero es: {numero} y es negativo')
else:
    print(f'el valor del numero es: {numero} cero')
    
#---------------------------------------------------------------------
# Pedimos al usuario que ingrese el día de la semana y el tiempo de estacionamiento en minutos
dia = input("Ingrese el día de la semana (Lunes, Martes, Miércoles, Jueves, Viernes, Sábado o Domingo): ")
tiempo = int(input("Ingrese el tiempo de estacionamiento en minutos: "))

# Si el tiempo es menor a 5 minutos, no se cobra nada y se muestra un mensaje
if tiempo < 5:
    print("El tiempo de estacionamiento es menor a 5 minutos, no se cobra nada.")
else:
    # Convertimos el tiempo a horas y determinamos el costo de estacionamiento según el día de la semana
    horas = tiempo / 60
    
    if dia in ("Lunes", "Martes", "Miércoles"):
        costo = round(horas * 2, 2) # $2.00 por hora o fracción
    elif dia in ("Jueves", "Viernes"):
        costo = round(horas * 2.5, 2) # $2.50 por hora o fracción
    elif dia == "Sábado" or dia == "Domingo":
        costo = round(horas * 3, 2) # $3.00 por hora o fracción
    else:
        print("Día de la semana no válido.")
        costo = None
    
    # Si se determinó el costo, lo mostramos al usuario
    if costo is not None:
        print(f"El costo de estacionamiento para el día {dia} es de ${costo}.")

#---------------------------------------------------------------------

#Capitulo 1 Pyton While:
i = 1
while i < 6:
    print(i)
    i+=1

#---------------------------------------------------------------------

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

#---------------------------------------------------------------------

i=0
while i < 6:
    i +=1
    if i == 3:
        continue
    print(i)

#---------------------------------------------------------------------

i = 1
while i < 6:
    print(i)
    continue
print(i)

#---------------------------------------------------------------------

i = 1
while i < 6:
    print(i)
    i +=1
else:
    print("i no es menir a 6")

#---------------------------------CAPITULO #2-----------------------------------

#MANEJO DE DATOS:
'''
01 LISTAS
02 DICIONARIOS
03 ADMINISTRACIÓN DE LISTAS
04 ADMINISTRACIÓN DE DICCIONARIOS
'''
'''
01 lIST
La lista son usado para almacenar multiple objectos en un sola variable
USAMOS SQUARE BRACKETS:
'''

thislist = ["apple", "banana", "Cherry"]
print(len(thislist))
#---------------------------------------------------------------------
thislist = ["apple", "banana", "Cherry"]
print(thislist)
#---------------------------------------------------------------------
mylist = ["apple", "banana", "Cherry"]
print(type(mylist))

'''
03
Administración de Lista
'''

thislist = ["apple", "banana", "cherry"]
print(thislist[1])

#---------------------------------------------------------------------

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

#---------------------------------------------------------------------

thislist = ["apple", "banana", "cherry"]
print(thislist[2:5])

#---------------------------------------------------------------------

thislist = ["apple", "banana", "cherry"]
print(thislist[:4])

#---------------------------------------------------------------------

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])

#----------------------------------OTRA ADMINISTRACION DE LISTA----------------------------------
thislist = ["apple", "banana", "cherry", "orange","kiwi", "melon", "mango"]
print(thislist[-4:-1])

#---------------------------------------------------------------------

thislist = ["apple", "banana", "cherry"]
if "Apple" in thislist:
    print("Yes, 'apple' is in the fruits list")

#---------------------------------------------------------------------

thislist = ["apple", "banana", "cherry", "orange","kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)

#---------------------------------------------------------------------

thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#----------------------------------Nuevamente OTRA ADMINISTRACION DE LISTA----------------------------------
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)

thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana") #Ojo, si quieres eliminarlo desde alguna posicion usas pop
print(thislist)

thislist = ["apple", "banana", "cherry"]
thislist.pop[1]
print(thislist)

#----------------------------------Nuevamente OTRA ADMINISTRACION DE LISTA----------------------------------
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

#---------------------------------------------------------------------

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

#----------------------------------Nuevamente OTRA ADMINISTRACION DE LISTA----------------------------------

thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

#---------------------------------------------------------------------

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i +1

#---------------------------------------------------------------------

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

#---------------------------------------------------------------------


thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

#---------------------------------Nuevamente ADMINISTRACION DE LISTA COMPREHENSION------------------------------------

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)


#---------------------------------Nuevamente ADMINISTRACION DE TUPLAS------------------------------------

thistuple = ("apple", "banna", "cherry")
print(thistuple) #Para el manejo de tuplas, se puede usar la misma metodologia de las listas, la diferencia radica en que las tuplas no se pueden mutar


#---------------------------------------------------------------------
'''
04 Diccionario Python
'''

thisdict = {
    "brand": "Ford",
    "Model": "Mustang",
    "year": 1964
}

#---------------------------------------------------------------------

thisdict = {
    "brand": "Ford",
    "Model": "Mustang",
    "year": 1964
}
print(thisdict["brand"])

print(len(thisdict))#Saber Longitud
print(type(thisdict))#Saber el tipo de valor

x = thisdict.get("model")

x = thisdict.keys()

#---------------------------------------------------------------------
car = {
    "brand": "Ford",
    "Model": "Mustang",
    "year": 1964
}
x = car.keys()
print(x) #Before the change

car["color"] = "white"

print(x) #after the change

#---------------------------------------------------------------------

car = {
    "brand": "Ford",
    "Model": "Mustang",
    "year": 1964
}
x = car.values()
print(x) #Before the change

car["year"] = 2020

print(x) #after the change

#---------------------------------------------------------------------


thisdict = {
    "brand": "Ford",
    "Model": "Mustang",
    "year": 1964
}
if "model" in thisdict:
    print("Si, 'Model' esta en una de la llaves en el thisdict diccionario")

#---------------------------------------------------------------------

thisdict = {
    "brand": "Ford",
    "Model": "Mustang",
    "year": 1964
}
thisdict["year"] = 2018

#---------------------------------------------------------------------
thisdict = {
    "brand": "Ford",
    "Model": "Mustang",
    "year": 1964
}
thisdict.update({"year": 2020})

#---------------------------------------------------------------------
thisdict = {
    "brand": "Ford",
    "Model": "Mustang",
    "year": 1964
}
thisdict["color"] = "red"
print(thisdict)

#---------------------------------------------------------------------



































