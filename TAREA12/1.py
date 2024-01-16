#crear una cuenta
def crear(cantidad):
    saldo=cantidad
    return saldo
def consulta(saldo):
    print("Su saldo actual es 2:",saldo)
#Consultar saldo
def ingresar(saldo,cantidad):
    saldo=saldo+cantidad
    return saldo
#Retirar cantidad
def retirar(saldo,cantidad):
    if cantidad>saldo:
        print("No tiene saldo suficiente")
    else:
        saldo=saldo-cantidad
    return saldo
#menu
def menu(saldo):
    op=5
    while op!=4:
        print("1.Ingresar saldo")
        print("2.Retirar saldo")
        print("3.Consultar saldo")
        print("4.Salir")
        op=int(input("Introduce una opcion"))
        if op==1:
              cantidad=int(input("Que cantidad quieres ingresar?"))
              saldo=ingresar(saldo,cantidad)
        if op==2:
              cantidad=int(input("Que cantidad quieres retirar?"))
              saldo=retirar(saldo,cantidad)
        if op==3:
              consulta(saldo)
        if op==4:
              print("Gracias por su visita")
#Programa principal
saldo=int(input("Saldo inicial para crear la cuenta"))
menu(saldo)
  
  
