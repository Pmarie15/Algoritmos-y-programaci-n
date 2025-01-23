#Paola Haiek

import random

# Función para generar el mazo de cartas
def generar_mazo():
    pintas = ["treboles", "diamantes", "picas", "corazones"]
    mazo = []
    for i in range(1, 14):  # Números del 1 al 13
        for pinta in pintas:
            mazo.append(f"{i} de {pinta}")
    return mazo

# Función para barajar el mazo
def barajar_mazo(mazo):
    random.shuffle(mazo)

# Función principal para manejar el juego
def jugar():
    mazo = generar_mazo()
    barajar_mazo(mazo)
    
    mazo_barajado = []
    while len(mazo) > 0:
        indice = random.randint(0, len(mazo) - 1)
        carta = mazo.pop(indice)
        mazo_barajado.append(carta)
    
    puntos_jugador = 0
    puntos_computadora = 0
    carta_anterior = None
    
    print("Bienvenido a Batalla de Cartas!")
    print("Comencemos... cada vez que veas dos cartas seguidas del mismo número, puedes escribir 'batalla'.")
    print("¡Escribe 'salir' para terminar el juego!")

    # Se juega hasta que no haya más cartas
    while len(mazo_barajado) > 0:
        carta_actual = mazo_barajado.pop(0)  # Sacar la primera carta del mazo barajado
        print(f"\nCarta actual: {carta_actual}")
        
        if carta_anterior and carta_anterior.split()[0] == carta_actual.split()[0]:
            respuesta = input("¿Batalla? (escribe 'batalla' para sumar un punto o 'siguiente' para continuar): ").lower()
            if respuesta == "batalla":
                puntos_jugador += 1
                print("¡Batalla! Tu punto.")
            else:
                puntos_computadora += 1
                print("¡Batalla! La computadora suma un punto.")
        
        carta_anterior = carta_actual
        
        # Preguntar si desea ver la siguiente carta
        if len(mazo_barajado) > 0:
            respuesta = input("Presiona Enter para ver la siguiente carta, o escribe 'salir' para terminar el juego: ").lower()
            if respuesta == 'salir':
                break

    # Al agotarse las cartas, se muestra el resultado final
    print("\n¡Juego terminado!")
    print(f"Puntos del jugador: {puntos_jugador}")
    print(f"Puntos de la computadora: {puntos_computadora}")
    
    if puntos_jugador > puntos_computadora:
        print("¡Has ganado!")
    elif puntos_computadora > puntos_jugador:
        print("¡La computadora ha ganado!")
    else:
        print("¡Es un empate!")

# Llamar a la función para jugar
jugar()
