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
    
