from abc import ABC, abstractmethod

class empleado(ABC):
    def __init__(self, nombre, apellido, id):
        self.nombre = nombre
        self.apellido = apellido
        self.id = id

    @abstractmethod
    def calcular_salario(self):
        pass

    @abstractmethod
    def describir_rol(self):
        pass


class diseñadoragrafica(empleado):
    def __init__(self, nombre, apellido, id, trabajos_mes, base=1200, comision=300):
        super().__init__(nombre, apellido, id)
        self.trabajos_mes = trabajos_mes
        self.base = base
        self.comision = comision

    def calcular_salario(self):
        return self.base + self.comision * self.trabajos_mes

    def describir_rol(self):
        print(f"{self.nombre} {self.apellido} (ID {self.id}) es diseñadora grafica: realiza {self.trabajos_mes} trabajos este mes")


class odontologo(empleado):
    def __init__(self, nombre, apellido, id, guardias_realizadas, base=900, extra=100):
        super().__init__(nombre, apellido, id)
        self.limpiezas_realizadas = guardias_realizadas
        self.base = base
        self.extra = extra

    def calcular_salario(self):
        return self.base + self.extra * self.limpiezas_realizadas

    def describir_rol(self):
        print(f"{self.nombre} {self.apellido} (ID {self.id}) es odontologo: realizo {self.limpiezas_realizadas} limpiezas este mes")


class gerente(empleado):
    def __init__(self, nombre, apellido, id, departamento, sueldo_fijo=3500):
        super().__init__(nombre, apellido, id)
        self.departamento = departamento
        self.sueldo_fijo = sueldo_fijo

    def calcular_salario(self):
        return self.sueldo_fijo

    def describir_rol(self):
        print(f"{self.nombre} {self.apellido} (ID {self.id}) es gerente del departamento de {self.departamento}.")


diseñadoragrafica1 = diseñadoragrafica("marian", "socorro", 1001, 4)
odontologo1 = odontologo("marco", "alvarado", 1002, 6)
gerente1 = gerente("maximilian", "pietro", 1003, "administración")

staff = [diseñadoragrafica1, odontologo1, gerente1]

for empleado in staff:
    empleado.describir_rol()
    print(f"salario de {empleado.nombre}: ${empleado.calcular_salario()}\n")