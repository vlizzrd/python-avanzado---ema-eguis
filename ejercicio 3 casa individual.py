from abc import ABC, abstractmethod


class empleado(ABC):
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    @abstractmethod
    def calcular_salario(self):
        pass

    def presentarse(self):
        return self.nombre + " " + self.apellido


class empleadofijo(empleado):
    def __init__(self, nombre, apellido, sueldo_mensual):
        super().__init__(nombre, apellido)
        self._sueldo_mensual = sueldo_mensual

    def calcular_salario(self):
        return self._sueldo_mensual

class freelancer(empleado):
    def __init__(self, nombre, apellido, horas, tarifa):
        super().__init__(nombre, apellido)
        self._horas = horas
        self._tarifa = tarifa

    def calcular_salario(self):
        return self._horas * self._tarifa


class nomina:
    def __init__(self):
        self.empleados = []

    def agregar_empleado(self, empleado):
        self.empleados.append(empleado)

    def calcular_total(self):
        total = 0
        for empleado in self.empleados:
            total += empleado.calcular_salario()
        return total


emp1 = empleadofijo("carolina", "sanchez", 2000)
emp2 = freelancer("jonathan", "joestar", 40, 20)
emp3 = freelancer("liam", "gallagher", 80, 10)

n = nomina()
n.agregar_empleado(emp1)
n.agregar_empleado(emp2)
n.agregar_empleado(emp3)

for e in n.empleados:
    print(e.presentarse(), e.calcular_salario())

print("total nomina:", n.calcular_total())