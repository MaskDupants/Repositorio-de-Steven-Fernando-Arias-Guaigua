import random  

print("BIENVENIDO AL JUEGO DE PIEDRA PAPEL O TIJERAS")
print("Escribe 'salir' para terminar.\n")
opciones = ("piedra", "papel", "tijeras")

while True:  
    jugador = input("ELIJE ENTRE: (piedra✊/papel✋/tijeras✌): ")

    if jugador in ("salir"):
        print("VUELVE PRONTO!")
        break  

    if jugador not in opciones:
        print("Entrada inválida. Intenta otra vez.\n")
        continue  

    pc = random.choice(opciones)
    print(f"Usuario:{jugador}  |  Computadora: {pc}")

    if jugador == pc:
        print("Resultado: ¡Empate!")
    elif (jugador == "piedra" and pc == "tijeras") or \
         (jugador == "papel" and pc == "piedra") or \
         (jugador == "tijeras" and pc == "papel"):
        print("Resultado: ¡Ganaste!")
    else:
        print("PARECE QUE HAZ PERDIDO! 😒")
