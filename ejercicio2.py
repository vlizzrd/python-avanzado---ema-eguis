class cafetera:
    def __init__(self, capacidad_maxima):
        self.capacidad_maxima = capacidad_maxima  
        self.cantidad_actual = 0 
        self.cafe_molido = False 

def llenar_agua(self, ml):
        if self.cantidad_actual + ml > self.capacidad_maxima:
            self.cantidad_actual = self.capacidad_maxima
            print(f"la cafetera está llena. capacidad máxima: {self.capacidad_maxima} ml")
        else:
            self.cantidad_actual += ml
            print(f"se añadieron {ml} ml de agua. cantidad actual: {self.cantidad_actual} ml")

def poner_cafe (self):
        self.cafe_molido = True
        print("se ha puesto café molido en la cafetera")

def servir_taza(self):
    def servir_taza(self):
        if self.cantidad_actual >= 250 and self.cafe_molido:
            self.cantidad_actual -= 250
            self.cafe_molido = False
            print("se sirvió una taza de café")
        elif self.cantidad_actual < 250:
            print("error: no hay suficiente agua para servir una taza")
        elif not self.cafe_molido:
            print("error: no hay café en el filtro.")

def mostrar_estado(self):
        print(f"capacidad máxima: {self.capacidad_maxima} ml")
        print(f"cantidad actual de agua: {self.cantidad_actual} ml")
        print(f"filtro de café cargado: {'sí' if self.cafe_molido else 'no'}")