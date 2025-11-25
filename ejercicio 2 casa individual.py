from abc import ABC, abstractmethod
import math


class figura(ABC):
    _color_borde = "negro"

    @abstractmethod
    def calcular_area(self):
        pass

    @abstractmethod
    def calcular_perimetro(self):
        pass


class rectangulo(figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calcular_area(self):
        return self.base * self.altura

    def calcular_perimetro(self):
        return 2 * (self.base + self.altura)

class circulo(figura):
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        return math.pi * self.radio ** 2

    def calcular_perimetro(self):
        return 2 * math.pi * self.radio


rectangulo1 = rectangulo(4, 6)
circulo1 = circulo(3)
rectangulo1 = rectangulo(2, 5)

figuras = [rectangulo1, circulo1, rectangulo1]

for figura in figuras:
    print("area:", figura.calcular_area())
    print("perímetro:", figura.calcular_perimetro())
    print("color de borde:", figura._color_borde)