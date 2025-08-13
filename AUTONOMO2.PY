#JUEGO DE PIEDRA PAPEL O TIJERAS
import random

piedra=1
papel=2
tijera=3
opciones=("PIEDRA","PAPEL","TIJERAS")
print("BIENVENIDO AL JUEGO PIEDRA, PAPEL O TIJERAS!!")
jugador= str(input(print("ELIGE PIEDRA PAPEL O TIJERA")))
pc=random.choice(opciones)
print("TU ELEGISTE:", jugador, "Y LA COMPUTADORA ELIGIO", pc)
if jugador == pc:
    print("ES UN EMPATE!!!!!")
elif jugador == ("PIEDRA") and pc == ("TIJERAS"):
    print("GANASTE!")
elif jugador == ("PAPEL") and pc == ("PIEDRA"): 
    print("GANASTE!")
elif jugador == ("TIJERAS") and pc == ("PAPEL"):
    print("GANASTE!")
else:
    print("HAS PERDIDO :C ")