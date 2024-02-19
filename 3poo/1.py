#Clase Socio con los campos nombre y antiguedad
class Socio:
    def __init__(self):
        self.nombre = input("Ingrese el nombre del socio: ")
        self.antiguedad = int(input("Ingrese la antigüedad del socio en años: "))

#visualizar un socio
    def imprimir(self):
        print(self.nombre,"tiene una antiguedad en años de",self.antiguedad)

#retornar antiguedad
    def verantiguedad(self):
        return self.antiguedad
#Clase Club con una lista de socios
class Club:
    def _init_(self):
        self.socios=[]
#agregar un socio
    def agregarSocio(self):
        socio=Socio()
        self.socio.append(socios)

#Mostrar todos los socios
    def mostrarSocios(self):
        for socio in self.socios:
            socio.imprimir()

#Mostrar un socio
    def mostrarUnSocio(self):
        pos=int(input("introduce la posicion del socio a visualizar:"))
        if (pos<len(self.socios)):
            self.socios[pos].imprimir()
#Visualizar el socio de mayor antiguedad
    def mostrarMayorAntiguedad(self):
        mayor=self.socios[0]
        for socio in self.socios:
            if socio.verAntiguedad()>mayor.verAntiguedad():
                mayor=socio
        print("Socio de mayor antiguedad:")
        mayor.imprimir


#Principal
club=Club()
club.agregarSocio()
club.agregarSocio()
club.agregarSocio()
club.mostrarSocio()
club.mostrarUnSocio()
cllub.mostrarMayorAntiguedad()
    
