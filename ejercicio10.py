# Crea un programa que calcule quien gana más partidas al piedra, papel, tijera. 
# - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate) 
# - La función recibe un listado que contiene pares, representando cada jugada.
# - El par puede contener combinaciones de "R" (piedra), "P" (papel) o "S" (tijera). 
# - Ejemplo. Entrada: [("R","S"), ("S","R"), ("P","S")]. Resultado: "Player 2".
import random

def generar_jugada():
    # Generar una jugada aleatoria para cada jugador
    jugadas = [("R", "piedra"), ("P", "papel"), ("S", "tijera")]
    return random.choice(jugadas), random.choice(jugadas)

def calcular_ganador(jugadas):
    # Diccionario para contar las victorias de cada jugador
    victorias = {"Player 1": 0, "Player 2": 0}
    
    # Reglas del juego: R > S, S > P, P > R
    reglas = {"R": "S", "S": "P", "P": "R"}
    
    # Función para obtener el nombre completo de la jugada
    def obtener_nombre(opcion):
        opciones = {"R": "piedra", "P": "papel", "S": "tijera"}
        return opciones[opcion]

    # Iterar sobre las jugadas
    for i, jugada in enumerate(jugadas):
        jugador1, jugador2 = jugada
        
        # Mostrar la jugada actual
        print(f"Jugada {i+1}: Player 1 sacó {obtener_nombre(jugador1[0])} ({jugador1[0]}), Player 2 sacó {obtener_nombre(jugador2[0])} ({jugador2[0]})")

        # Si las jugadas son iguales, es un empate
        if jugador1[0] == jugador2[0]:
            print("Empate en esta jugada.")
            continue
        
        # Determinar el ganador de esta jugada
        if reglas[jugador1[0]] == jugador2[0]:
            victorias["Player 1"] += 1
            print("Player 1 gana esta jugada.")
        else:
            victorias["Player 2"] += 1
            print("Player 2 gana esta jugada.")
    
    # Determinar quién ha ganado más partidas
    if victorias["Player 1"] > victorias["Player 2"]:
        return "Player 1"
    elif victorias["Player 2"] > victorias["Player 1"]:
        return "Player 2"
    else:
        return "Tie (empate)"

# Solicitar al usuario el número de jugadas
num_jugadas = int(input("Ingrese el número de jugadas que desea realizar: "))

# Lista para almacenar las jugadas
jugadas = []

# Jugar las partidas y contar las victorias
for _ in range(num_jugadas):
    # Generar una jugada para cada jugador
    jugada = generar_jugada()
    jugadas.append(jugada)

# Calcular el ganador
ganador = calcular_ganador(jugadas)
print("El ganador es:", ganador)