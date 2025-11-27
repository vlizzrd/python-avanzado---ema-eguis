from abc import ABC, abstractmethod
import math


class figurageometrica(ABC):
    
    @abstractmethod
    def calcular_area(self):
        pass

class Rectangulo(figurageometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

class Circulo(figurageometrica):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):

        return math.pi * (self.radio ** 2)


mi_rectangulo = Rectangulo(base=10, altura=5)
mi_circulo = Circulo(radio=3)


lista_figuras = [mi_rectangulo, mi_circulo]

print("calculando áreas de figuras mixtas:\n")

for figura in lista_figuras:

    nombre = type(figura).__name__
    area = figura.calcular_area()
    
    print(f"🔹 figura: {nombre}")

    print(f"   area: {area:.2f} unidades cuadradas")