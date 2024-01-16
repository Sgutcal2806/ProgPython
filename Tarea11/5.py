lista1=[]
lista2=[]
lista3=[]

for x in range(4):
    valor=int(input("introduce un número a la lista1:"))
    lista1.append(valor)
    valor=int(input("introduce un número a la lista2:"))
    lista2.append(valor)
muybueno=0
for x in range(4):
    suma=lista1[x]+lista2[x]
    lista3.append(suma)
print("La lista resultante:",lista3)
