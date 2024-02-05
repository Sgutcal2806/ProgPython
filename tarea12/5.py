#función creamos una lista de n empleados
def crearLista(n):
    lista=[]
    for x in range(n):
        sueldo=int(input("introduce un sueldo:"))
        lista.append(sueldo)
    return lista
#función visualizar sueldos
def verSueldos(lista):
    print(lista)
#función sueldos superiores a 4000
def superior4000(lista):
    cantidad=0
    for x in range(len(lista)):
        if lista[x]>4000:
            cantidad=cantidad+1
        print("sueldos superior a 4000:",cantidad)
#función sueldo medio
def sueldoMedio(lista):
    sueldo=0
    for x in range(len(lista)):
        sueldo=sueldo+lista[x]
    promedio=sueldo/len(lista)
    return promedio
#función sueldos por debajo de la media
def debajoMedia(lista):
    media=sueldoMedio(lista)
    print("Los sueldos por debajo de la media son:")
    for x in range(len(lista)):
        if lista[x]<media:
            print(lista[x])
                
#Principal
n=int(input("Cuantos empleados hay?"))
lista=crearLista(n)
verSueldos(lista)
superior4000(lista)
print("El sueldo medio es",sueldoMedio(lista))
debajoMedia(lista)
