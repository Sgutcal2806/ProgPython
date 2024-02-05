#función que crea una lista de n elementos de caracteres
def crearLista():
    lista=[]
    n=int(input("Cuantos elementos tiene la lista"))
    for x in range(n):
        valor=int(input("Introduce un elemento de la lista:"))
        lista.append(valor)
    return lista
#función que multiplica los elementos de una lista por un valor
def mascaracteres(lista,n):
    palabra=lista[0]
    for x in ramge(1,len(lista)):
        if len(lista[x])>len(palabra):
            palabra=lista[x]
        return palabra
        
        

#Programa principal
palabras=crear(lista)
print(lista)
print("palabra con más caracteres:",mascaracteres(palabras))
