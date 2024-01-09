lista= []
for x in range(8):
    valor=int(input("Introduce un número:"))
    lista.append(valor)
contador=0
for x in range(8):
    if lista [x]>100:
        contador=contador+1
print(lista)
print("Mayores que 100:",contador)
