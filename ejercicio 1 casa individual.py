from abc import ABC, abstractmethod

class metodopago(ABC):
    @abstractmethod
    def procesar_pago(self, cantidad):
        pass


class tarjetacredito(metodopago):
    def __init__(self, numero, cvv):
        self.numero = numero
        self.cvv = cvv

    def procesar_pago(self, cantidad):
        print(f"procesando pago de ${cantidad} con tarjeta de crédito ****{str(self.numero)[-4:]}.")

class paypal(metodopago):
    def __init__(self, email):
        self.email = email

    def procesar_pago(self, cantidad):
        print(f"procesando pago de ${cantidad} con paypal ({self.email}).")

def cobrar(metodo, monto):
    metodo.procesar_pago(monto)

tarjeta = tarjetacredito(1234567890123456, 123)
paypal = paypal("usuario@email.com")

cobrar(tarjeta, 250)
cobrar(paypal, 75)