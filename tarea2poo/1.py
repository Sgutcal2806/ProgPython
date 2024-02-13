class Agenda:
    def _init_(self):
         self.listaAgenda[]
        
        
    def cargar(self):
        nombre=input("nombre")
        telefono=input("telefono")
        email=input("email")
        lista=[]
        lista.append(nombre)
        lista.append(telefono)
        lista.append(email)
        self.lista.append(lista)
    def listar(self):
        for usuario in self.listaAgenda:
            print(usuario[0],":",usuario[1],":",usuario[2])
    def consultarNombre(self):
        nombre=input("nombre")
        encontrado=0
        longitud=len(self.listaAgenda)
        indice=0
        while encontado==0 and indice<longitud:
            if self.listaAgenda[indice][0]==nombre:
                print("Telefono:",self.listaAgenda[indice][1])
                print("email:",self.listaAgenda[indice][2])
                encontrado=1
            indice=indice+1
        if encontrado==0:
            print(nombre,"no se encuentra en la agenda")
                 
        else:
            return indice-1

     def modificar(self):
         pos=self.consultarNombre()
         telefono=input("telefono")
         email=input("email")
         self.listaAgenda[pos][1]=telefono
         self.listaAgenda[pos][2]=email
         
         
             
     def menu(self):
         op=6
         while op!=5
         print("1.cargar datos en la agenda")
         print("2.Listar datos en lagenda")
         print("3.consultar por nombre")
         print("4.modificar telefono y email")
         print("5.finalizar")
         op=int(input("introduce una opcion"))
         if op==1:
             self.cargar()
         if op==2:
             self.listar()
         if op==3:
             self.consultarNombre
         if op==4:
             self.modificar()
         
         
#principal
miagenda=Agenda()
miagenda.menu()
