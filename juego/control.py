from random import randint
from personajes import Enemigo, Personaje
def combate(j, e):
    # Presentamos al enemigo
    print('')
    print('******NUEVO COMBATE*******')
    print('Ha aparecido un ' + e.nombre)  
    print('')

    # Comenzamos combate
    while j.vivo == True and e.vivo == True :
        # Informacion personajes
        print('****************************')
        print('Tu vida: ' + str(j.vida))
        print('Tu energia: ' + str(j.energia))
        print('Vida del enemigo: ' + str(e.vida))
        print('Ataque del enemigo: ' + str(e.ataque))

        respuesta = ''
        respuesta = input('¿Qué deseas hacer? a-Atacar ('+ str(j.ataque)+'). / c-Curar(coste='+ str(j.coste_curacion)+' , cantidad= '+str(j.curacion)+': ')

        if respuesta == 'a':
            print('¡Has decido atacar!')
            e.perder_vida(j.ataque)
            if e.vivo == False:
                break

        elif respuesta == 'c' and j.energia >= j.coste_curacion:
            print('¡Has decidido curarte!')
            j.curar()

        print('El ' + e.nombre + ' te ataca ' + str(e.ataque))
        j.perder_vida(e.ataque)

    print('Has vencido a tu oponente')

def recompensa(personaje):
    print('Recibes un poco de xp')
    personaje.experiencia += 100
    print('Recibes 50 almas desoladas')
    personaje.oro += 50
    p = randint(1, 4)
    if p == 1:
        print('Te has curado 20hp!')
        personaje.vida += 20
    
    elif p == 2:
        print('Recargas 25 puntos de energia!')
        personaje.energia += 25

    elif p == 3:
        print('Recoges un amuleto de fuerza... +5 de ataque!')
        personaje.ataque += 5
    elif p == 4:
        print('Has encontrado un botín (150 almas)')
        personaje.oro += 150

# def gachapon(tienda):
#     g = randint(1, 4)
#     if g == 1:
#         print('Te ha tocado una espada de luz!!' + str(Personaje.ataque))
#         Personaje.ataque += 4
#     elif g == 2:
#         print('Te ha tocado un arco luminoso!!' + 'Tu daño a aumentado a' + str(Personaje.ataque))
#         Personaje.ataque += 3
#     elif g == 3:
#         print('Te ha tocado un tirachinas!!' + str(Personaje.ataque))
#         Personaje.ataque += 0.5
#     elif g == 4:
#         print('Te ha tocado un moco, ¡TEN CUIDADO QUE ES PEGAJOSO!' + str(Personaje.ataque))
#         Personaje.ataque -= 2



# def tienda(j):
#     respuesta = ''
#     print('Ha aparecido la tienda de las sombras' + '¿Hay algo que te gustaria comprar?')
#     respuesta = input('¿Que desas hacer?: g = gachapon(objeto aleatorio)(200 almas desoladas). / ')
#     print('Tu oro' + str(Personaje.oro))

#     if respuesta == g:
#         gachapon()
        
        

    


