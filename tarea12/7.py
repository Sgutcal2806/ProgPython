#función que crea una lista de n elementos
def crearLista():
    lista=[]
    n=int(input("cuantos elementostiene la lista?:"))
    for x in range(n):
        valor=int(input("introduce un elemento de la lista"))
        lista.append(valor)
    return lista
#funcion que crea dos lista positivos y negativos
def dosListas(lista):
    positivos=[]
    negativos=[]
    for x in range(len(lista)):
        if lista[x]>=o:
            positivos.append(lista[x])
        else:
            negativos.append(lista[x])
    return [positivos,negativos]
def visualizar(positivos,negativos):
    print("positivos:",positivos)
    print("negativos:",negativos)
#programa principoal
lista=crearLista()
print(lista)
positivos,negativos=dosListas(lista)
visualizar(positivos,negativos)
                            
                    
