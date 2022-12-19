from personajes import Enemigo, Personaje, Soldado, Arquero, Alma_perdida, Trotamundos, Cofre
from control import combate, recompensa
from random import randint
# Propiedades del Jugador
jugador = Personaje('', 100, 15, 100, 20, 30)

# Propiedades Enemigos


# Comienzo del juego
print('Bienvenido al sueño del cazador...')
jugador.nombre = input('¿Cómo te llamas, cazador?')
print('Encantado de conocerte, ' + jugador.nombre)

#Primera dungeon
nivel1 = [Soldado(randint(0, 2)), Arquero(randint(0, 2)), Soldado(randint(0, 2)), Alma_perdida(randint(0, 2))]

for enemigo in nivel1:
    combate(jugador, enemigo)
    recompensa(jugador)
    jugador.comprobar_nivel()

print('Has pasado la 1 mazmorra!')




