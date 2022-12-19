class Enemigo: 
    def __init__(self, nombre, vida, ataque, nivel):
        self.nombre = nombre
        self.vida = vida + 5*nivel
        self.ataque = ataque + 2*nivel
        self.vivo = True
        self.nivel = nivel 

    #Metodo para perder vida
    def perder_vida(self, cantidad):
        if self.vivo == True:
            self.vida -= cantidad
            if self.vida <= 0:
                self.vivo = False

class Soldado(Enemigo):
    def __init__(self, nivel):
            super().__init__('Soldado', 35, 6, nivel)

class Arquero(Enemigo):
    def __init__(self, nivel):
        super().__init__('Arquero', 28, 8, nivel)

class Alma_perdida(Enemigo):
    def __init__(self, nivel):
        super().__init__('Alma perdida', 40, 10, nivel)

class Trotamundos(Enemigo):
    def __init__(self, nivel):
        super().__init__('Trotamundos', 40, 15, nivel)

class Cofre(Enemigo):
    def __init__(self, nivel):
        super().__init__('Cofre', 1, 0, nivel)

class Personaje:
    def __init__(self, nombre, vida, ataque, energia, curacion, coste_curacion):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.energia = energia
        self.curacion = curacion
        self.coste_curacion = coste_curacion
        self.vivo = True
        self.experiencia = 0
        self.nivel = 1
        self.oro = 50
        self.xpSiguienteNivel = 150

    def perder_vida(self, cantidad):
        if self.vivo == True:
            self.vida -= cantidad
            if self.vida <= 0:
                self.vivo = False

    
    #Curacion magia
    def curar(self):
        self.vida += self.curacion
        self.energia -= self.coste_curacion
    
    def comprobar_nivel(self):
        if self.experiencia >= self.xpSiguienteNivel:
            self.nivel += 1
            self.xpSiguienteNivel = 550
            self.vida += 5
            self.ataque += 5
            self.energia += 5
            print('Has subido al nivel '+ str(self.nivel)+ '!')
            print('Tu nueva vida: '+ str(self.vida))
            print('Tu nuevo ataque: '+ str(self.ataque))
            print('Tu nueva energia: '+ str(self.energia))



