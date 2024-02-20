class Cuenta:
    def __init__(self):
        self.nombre=input("introduce nombre")
        self.monto=int(input("introduce monto"))

    def imprimir(self):
        print(self.nombre,"tiene un monto de ",self.monto)

class CajaAhorro(Cuenta):
    def __init__(self):
        super().__init__()


    def imprimir(self):
        super().imprimir()
    
class PlazoFijo(Cuenta):
    def __init__(self):
        super().__init__()
        self.interes=float(input("intereses:"))
        self:imposicion=int(input("plazo de imposicion"))


    def imprimir(self):
        super().imprimir()
        print("intereses:",self.interes)
        print("plazo de imposicion",self.imposicion)


    def ganancia(self):
        ganancia=self.monto*self.interes/100
        print("Ganancia:",ganancia)

caja=CajaAhorro()
caja.imprimir()

plazo=PlazoFijo()
plazo.imprimir()
plazo.ganancia()
