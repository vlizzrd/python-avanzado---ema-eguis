class persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def presentarse(self):
        print(f"hola, soy {self.nombre} y tengo {self.edad} años.")


class profesor(persona):
    def __init__(self, nombre, edad, materia):
        super().__init__(nombre, edad)  
        self.materia = materia

    def dictar_clase(self):
        print(f"el profesor {self.nombre} esta dictando la clase de {self.materia}.")


p1 = persona("juana", 22)
p1.presentarse()


prof1 = profesor("carlos", 40, "matematicas")
prof1.presentarse()     
prof1.dictar_clase() 