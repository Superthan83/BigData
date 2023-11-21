from colorama import Fore, Style, init
init(autoreset=True)

tablero = [["[ ]","[ ]","[ ]"],["[ ]","[ ]","[ ]"],["[ ]","[ ]","[ ]"]]

#Variables juego
jugador1 = f'{Fore.LIGHTRED_EX}[X]'
jugador2 = f'{Fore.CYAN}[O]'
volver_a_jugar = True
jugador_actual = jugador1

#Funcion para crear el tablero
def Creartablero(tablero):
    for fila in tablero:
        for col in fila:
            print(col, end="")
        print()
Creartablero(tablero)

#Funcion para cambiar la posicion de los jugadores
def cambia_posicion(fila, col):
    tablero[fila][col] = jugador_actual
    for fila in tablero:
        for col in fila:
            print(col, end="")
        print()

#Funcion para verificar si hay un ganador
def verificar_ganador(tablero, jugador):
    # Verificar filas
    for fila in tablero:
        if fila.count(jugador) == 3:
            return True

    # Verificar columnas
    for col in range(3):
        if tablero[0][col] == jugador and tablero[1][col] == jugador and tablero[2][col] == jugador:
            return True

    # Verificar diagonal principal
    if tablero[0][0] == jugador and tablero[1][1] == jugador and tablero[2][2] == jugador:
        return True

    # Verificar diagonal secundaria
    if tablero[0][2] == jugador and tablero[1][1] == jugador and tablero[2][0] == jugador:
        return True

    return False

#Informacion sobre el juego
print(f"{Fore.RED}Para salir del juego escribe 111 en una de los dos campos")
print(f"{Fore.LIGHTBLUE_EX}Recuerda que las posiciones comienzan desde el 0")

print(f"{Fore.LIGHTBLUE_EX}Por ejemplo si quieres en la esquina superior izquierda tendras que poner fil 0 y col 0")
print(f"{Fore.LIGHTBLUE_EX}Si quieres en la esquina inferior derecha tendras que poner fil 2 y col 2")
print("------------------------------------")

while(volver_a_jugar == True):
    for turno in range(9):  # Un máximo de 9 turnos para un tablero de 3x3
        print(f"Turno del jugador: {jugador_actual} - Turno: {turno + 1}")
        fila = int(input("Ingresa la fil que quieres "))
        col = int(input("Ingresa la col que quieres "))
        print("------------------------------------")
        if fila == 111 or col == 111:
            print("Gracias por jugar")
            exit()
        cambia_posicion(fila, col)
        if verificar_ganador(tablero, jugador_actual):
            print(f"Tres en raya!!!, El jugador {jugador_actual} ha ganado!")
            volver = input("Quieres volver a jugar (s/n)? ")
            if volver == "s":
                # volver_a_jugar = False
                volver_a_jugar = True
                tablero = [["[ ]","[ ]","[ ]"],["[ ]","[ ]","[ ]"],["[ ]","[ ]","[ ]"]]
                Creartablero(tablero)
            else:
                print("Gracias por jugar")
                volver_a_jugar = False
                exit()
        if jugador_actual == jugador1:
            jugador_actual = jugador2
        else:
            jugador_actual = jugador1
            