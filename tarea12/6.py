#función creamos una lista de articulos y de precios
def crearLista(n):
    articulos=[]
    precios=[]
    for x in range(n):
        articulo=input("introduce el nombre de un articulo:")
        precio=int(input("introduce el precio del articulo:"))
        articulos.append(articulo)
        precios.append(precio)
    return [articulos,precios]
#función visualizar los articulos y sus sueldos
def verArticulos(articulos,precios):
    for x in range(len(articulos)):
        print(articulos[x],":",precios[x])
#función ariculo más caro
def articuloMasCaro(articulos,precios):
    masCaro=precios[0]
    pos=0
    for x in range(1,len(precios)):
        if precios[x]>masCaro:
            masCaro=precios[x]
            pos=x
        print("el articulo mas caro es",articulos[pos],"con un precio de",masCaro)
#función articulos con precio menor a uno dado
def articulosMenores(articulos,precios,importe):
    for x in range(len(precios)):
        if precios[x]<importe:
            print(articulos[x],"tiene un precio menor a ",importe,"y es",precios[x])

                
#Programa principal
n=int(input("Cuantos articulos hay?:"))
articulos,precios=crearLista(n)
verArticulos(articulos,precios)
articuloMasCaro(articulos,precios)
importe=int(input("importe a comparar:"))
articulosMenores(articulos,precios,importe)
      
