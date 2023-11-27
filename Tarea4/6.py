lista1=0
lista2=0
x=1
while x<=5:
    valor=int(input("Introduce un valor de lista1"))
    x=x+1
    lista1=lista1+valor
x=1
while x<=5:
    valor=int(input("Introduce un valor de lista2"))
    x=x+1
    lista1=lista2+valor
if lista1>lista2:
    print("la lista 1 es mayor con un valor de:",lista1)
else:
    if lista1<lista2:
        
       print("la lista 1 es mayor con un valor de:",lista1)
    else:
       print("ambas son iguales con un valor de:",lista1)  
