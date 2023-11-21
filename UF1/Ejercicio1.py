#TAREA 1. Realizar un fragmento de código en el que se pregunte al usuario su nombre, su edad
#y su mes de cumpleaños, y, seguidamente, se le presente un mensaje como éste:
#“Bienvenido NOMBRE USUARIO. Usted nació en el año AÑO”.
#
#
#Se declara la variable(nombre,edad,mes) y se guarda la respuesta que dara el usuario.
nombre=input("Como te llamas?")
edad=input("Que edad tienes?")
mes=input("Cual es tu mes de cumpleanos?")
#Se declara el mensaje y se concatena lo que se va a mostrar.
mensaje=f"Bienvenido {nombre} usted tiene {edad} anos y ha nacido en el mes de {mes}"
#Funcion para mostrar en pantalla el mensaje.
print(mensaje)

#TAREA 2. Escribir un fragmento de código que pida al usuario dos números enteros y muestre
#por pantalla el mensaje “La división de <n> entre <m> da un cociente <c> y un resto <r> “.
#
#
#Se declara la variable (numero uno y numero dos) y se dividen para obtener el cociente
#Y se restan para obtener el resto.
numero1=input("Escribe un numero entero")
numero2=input("Escribe otro numero entero")
cociente=numero1/numero2
resto=numero1-numero2
#Se declara el mensaje y se concatena lo que se va a mostrar.
mensaje=f"La división de {numero1} entre {numero2} da un cociente {cociente} y un resto {resto}"
#Funcion para mostrar en pantalla el mensaje.
print(mensaje)
#
#
#TAREA 4. Suponiendo una población inicial de 200, usa el print() y el los caracteres de escape necesarios
#(\n para salto de línea, \t para tabulador), para mostrar por pantalla una tabla como la
#siguiente:
#Hora   Número de bacterias
#0      200
#5      6400
#10     204800
#15     6553600
#Se declara el mensaje y se concatena lo que se va a mostrar.
mensaje=f"Hora\tNumero de bacterias\n0\t200\n5\t6400\n10\t204800\n15\t6553600"
#Funcion para mostrar en pantalla el mensaje.
print(mensaje)
#
#
#TAREA 5. Para hacer la declaración de la renta se debe ser mayor de 16 años y tener unos
#ingresos iguales o superiores a 22000 € anuales. Escribir un programa que pregunte al
#usuario cuál es edad y cuáles son sus ingresos anuales y muestre por pantalla si el usuario
#tiene que hacer la declaración o no. Usar la sentencia de control if.
#Se declaran las variables.
edad=input("Escribe tu edad para saber si tienes que hacer la declaracion de la renta")
if(edad > 16){
    ingresos=input("Escribe tus ingresos")
    if(ingresos > 22000){
        mensaje="Tienes que declarar"
        print(mensaje)
    }
    else{
        mensaje="No tienes que declarar"
        print(mensaje)
    }
            }
else{
    mensaje="No tienes que declarar"
    #Funcion para mostrar en pantalla el mensaje.
    print(mensaje)
    }
