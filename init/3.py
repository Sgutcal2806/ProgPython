class Operaciones:
     def _init_(self):
         
        self.numero1=int(input("numero1"))
        self.numero2=int(input("numero2"))
        
     def suma(self):
         resultado=self.numero1+self.numero2
         print("la suma es ",resultado)
     def resta(self):
         resultado=self.numero1-self.numero2
         print("la resta es ",resultado)
     def multiplicar(self):
         resultado=self.numero1*self.numero2
         print("la multiplicacion es ",resultado)
     def division(self):
         resultado=self.numero1/self.numero2
         print("la division es ",resultado)
#principal
operacion=Operaciones()
operacion.suma()
operacion.resta()
operacion.multiplicar()
operacion.division()
