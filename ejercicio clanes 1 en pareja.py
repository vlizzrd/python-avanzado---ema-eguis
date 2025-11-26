import random

class Guerrero:
    def __init__(self, nombre, vida, atk, defensa):
        self.nombre = nombre
        self.vida = vida
        self.atk = atk
        self.defensa = defensa

    def vivo(self):
        return self.vida > 0

    def atacar(self, otro):
        daño = max(1, self.atk - otro.defensa)
        otro.vida -= daño

class Clan:
    def __init__(self, nombre):
        self.nombre = nombre
        self.guerreros = []

    def agregar(self, g):
        self.guerreros.append(g)

    def vivos(self):
        return [g for g in self.guerreros if g.vivo()]

class Batalla:
    def __init__(self, c1, c2):
        self.c1 = c1
        self.c2 = c2

    def pelear(self):
        turno = 0
        while self.c1.vivos() and self.c2.vivos():
            atacante = random.choice(self.c1.vivos())
            defensor = random.choice(self.c2.vivos())
            atacante.atacar(defensor)
            if self.c2.vivos():
                atacante2 = random.choice(self.c2.vivos())
                defensor2 = random.choice(self.c1.vivos())
                atacante2.atacar(defensor2)
            turno += 1
        if self.c1.vivos():
            print(self.c1.nombre, "gana")
        else:
            print(self.c2.nombre, "gana")


a = Clan("Azul")
r = Clan("Rojo")
a.agregar(Guerrero("A1", 20, 7, 2))
a.agregar(Guerrero("A2", 18, 6, 3))
r.agregar(Guerrero("R1", 19, 8, 2))
r.agregar(Guerrero("R2", 17, 7, 3))

batalla = Batalla(a, r)
batalla.pelear()