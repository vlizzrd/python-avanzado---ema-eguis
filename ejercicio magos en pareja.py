
class hechizo:
    def __init__(self, nombre, dano, costo_mana):
        self.nombre = nombre
        self.dano = dano
        self.costo_mana = costo_mana


class persona:
    def __init__(self, nombre, vida, mana):
        self.nombre = nombre
        self.vida = vida
        self.mana = mana
    
    def mostrar_estado(self):
        print(self.nombre, "- vida:", self.vida, "- mana:", self.mana)


class estudiante(persona):
    def __init__(self, nombre):
       
        super().__init__(nombre, 100, 50)
        self.hechizos_conocidos = []

    def aprender_hechizo(self, hechizo):
        self.hechizos_conocidos.append(hechizo)
        print(self.nombre, "ha aprendido el hechizo:", hechizo.nombre)

    def atacar(self, objetivo, hechizo):

        if hechizo in self.hechizos_conocidos:

            if self.mana >= hechizo.costo_mana:
                self.mana -= hechizo.costo_mana
                objetivo.vida -= hechizo.dano
                print(self.nombre, "lanza", hechizo.nombre, "a", objetivo.nombre)
                print("Daño causado:", hechizo.dano)
            else:
                print(self.nombre, "no tiene suficiente mana.")
        else:
            print(self.nombre, "no conoce ese hechizo.")


class profesor(persona):
    def __init__(self, nombre):
        super().__init__(nombre, 200, 100)

    def ensenar(self, estudiante, hechizo):
        print("El profesor", self.nombre, "esta enseñando...")
        estudiante.aprender_hechizo(hechizo)




fuego = hechizo("Bola de Fuego", 30, 20)
rayo = hechizo("Rayo", 40, 30)


profesor = Profesor("Snape")
estudiante1 = estudiante("Harry")
estudiante2 = estudiante("Draco")


profesor.ensenar(estudiante1, fuego)
profesor.ensenar(estudiante2, rayo)

print(" INICIO DEL DUELO")


estudiante1.mostrar_estado()
estudiante2.mostrar_estado()

print(" Turno 1")


print("--- Turno 2 ---")

estudiante2.atacar(estudiante1, rayo)

print("--- ESTADO FINAL ---")
estudiante1.mostrar_estado()
estudiante2.mostrar_estado()