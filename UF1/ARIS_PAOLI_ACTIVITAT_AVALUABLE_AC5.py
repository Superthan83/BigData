#TAREA2
# Parte a) Crear una lista de números que sean el doble de otra lista
lista_numeros = [1, 2, 3, 4, 5]
lista_doble = list(map(lambda x: x * 2, lista_numeros))
print(lista_doble)
# Parte b) Crear una lista que convierta a mayúsculas todas las palabras de otra lista
lista_palabras = ["garza", "urraca", "gorrión", "petirrojo"]
lista_mayusculas = list(map(lambda x: x.upper(), lista_palabras))
print(lista_mayusculas)

#TAREA3
# Parte a) Crea una tupla a partir de una lista usando la función constructora de tuplas
lista_a = [1, 2, 3]
tupla_a = tuple(lista_a)
print(tupla_a)

# Parte b) Crea una lista a partir de una tupla usando la función constructora de listas
tupla_b = (4, 5, 6)
lista_b = list(tupla_b)
print(lista_b)

# Parte c) Crea tres listas de dos elementos cada una y luego crea una tupla que las contenga
lista_c1 = [1, 2]
lista_c2 = [3, 4]
lista_c3 = [8, 2]
tupla_x = (lista_c1, lista_c2, lista_c3)
print(tupla_x)

# Parte d) Prueba a modificar la posición 0 de la lista que ocupa la posición 0 de la tupla
# ¿Has podido realizar la modificación? ¿Cómo es posible, si las tuplas son inmodificables?

# Intentamos modificar la posición 0 de la lista en la posición 0 de la tupla
tupla_x[0][0] = 99

# Comprobamos el resultado
print(tupla_x)

#TAREA4
#PRIMERA PARTE
# Lista que representa la cola de pedidos en el almacén
cola_pedidos = []

# a) Función procesarPedido
def procesarPedido():
    if cola_pedidos:
        pedido = cola_pedidos.pop(0)
        print(f"Procesando {pedido}...")
    else:
        print("La cola de pedidos está vacía.")

# b) Función encolarPedido
def encolarPedido(pedido):
    cola_pedidos.append(pedido)
    print(f"Pedido {pedido} añadido a la cola.")

# c) Función vaciarCola
def vaciarCola():
    cola_pedidos.clear()
    print("La cola de pedidos ha sido vaciada.")

# Pruebas de las funciones
encolarPedido("pedido345671")
encolarPedido("pedido628316")
encolarPedido("pedido235252")

procesarPedido()
procesarPedido()

vaciarCola()

#SEGUNDA PARTE

# Lista que representa la pila de pedidos en el almacén
pila_pedidos = []

# a) Función procesarPedido
def procesarPedidoPila():
    if pila_pedidos:
        pedido = pila_pedidos.pop()
        print(f"Procesando {pedido}...")
    else:
        print("La pila de pedidos está vacía.")

# b) Función encolarPedido
def encolarPedidoPila(pedido):
    pila_pedidos.append(pedido)
    print(f"Pedido {pedido} añadido a la pila.")

# c) Función vaciarCola
def vaciarPila():
    pila_pedidos.clear()
    print("La pila de pedidos ha sido vaciada.")

# Pruebas de las funciones con una pila
encolarPedidoPila("pedido345671")
encolarPedidoPila("pedido628316")
encolarPedidoPila("pedido235252")

procesarPedidoPila()
procesarPedidoPila()

vaciarPila()

#TAREA5
dicc_prefijos = {
    "91": "Madrid",
    "93": "Barcelona",
    "95": "Sevilla",
    # Agrega más prefijos y comunidades según sea necesario
}

def buscarComunidadAutonoma(prefijo):
    if prefijo in dicc_prefijos:
        return dicc_prefijos[prefijo]
    else:
        return "No se encontró la comunidad autónoma para el prefijo proporcionado."

def agregarPrefijoComunidad(prefijo, comunidad):
    dicc_prefijos[prefijo] = comunidad
    print(f"Prefijo {prefijo} añadido para la comunidad autónoma de {comunidad}.")

# Solicitar al usuario que ingrese un prefijo telefónico
prefijo_usuario = input("Introduce un prefijo telefónico: ")

# Verificar si el prefijo ya está en el diccionario
comunidad_autonoma = buscarComunidadAutonoma(prefijo_usuario)
print(f"Comunidad Autónoma: {comunidad_autonoma}")

# Dar la opción de agregar un nuevo prefijo y comunidad autónoma
opcion_agregar = input("¿Quieres agregar un nuevo prefijo y comunidad autónoma? (Sí/No): ").lower()

if opcion_agregar == "si":
    nuevo_prefijo = input("Introduce el nuevo prefijo: ")
    nueva_comunidad = input("Introduce la nueva comunidad autónoma: ")
    agregarPrefijoComunidad(nuevo_prefijo, nueva_comunidad)

# Imprimir el diccionario actualizado
print("Diccionario de prefijos actualizado:")
print(dicc_prefijos)

#TAREA6
def contar_ocurrencias(cadena):
    # Paso b) Utiliza el método split para separar palabras
    palabras = cadena.split()

    # Paso c) Almacena la información en un diccionario
    diccionario_ocurrencias = {}
    for palabra in palabras:
        # Utiliza el método get() para contar las ocurrencias
        diccionario_ocurrencias[palabra] = diccionario_ocurrencias.get(palabra, 0) + 1

    return diccionario_ocurrencias

# Paso a) Pide al usuario una cadena de texto
cadena_usuario = input("Introduce una cadena de texto: ")

# Paso d) Imprime el diccionario por pantalla
resultado = contar_ocurrencias(cadena_usuario)
print("Diccionario de ocurrencias:")
print(resultado)