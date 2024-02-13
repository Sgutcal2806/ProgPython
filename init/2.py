class Triangulo:
     def _init_(self,l1,l2,l3):
         
        self.lado1=l1
        self:lado2=l2
        self:lado3=l3
     def imprimirMayor(self):
         print("medida de lado mayor:")
         if self.lado1>self.lado2>self.lado3:
             print(self.lado1)
         else:
             if self.lado2>self.lado3:
                 print(self.lado2)
             else:
                 print(self.lado3)

     def equilatero(self):
         
         if (self.lado1==self.lado2==self.lado3):
             
             print("El triangulo es equilatero")
         else:
             print("El triangulo no es equilatero")
#principal
l1=int(input("lado1"))
l2=int(input("lado2"))
l3=int(input("lado3"))
triangulo1=triangulo(l1,l2,l3)
triangulo1.imprimirMayor()
triangulo.equilatero()
