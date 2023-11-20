from math import sqrt
a=int(input("introduce una número a"))
b=int(input("introduce una número b"))
c=int(input("introduce una número c"))
aux=b*b-4*a*c
if aux<0:
    print("soluciones complejas")
else:
    raiz=sqrt(aux)
    x1=(-b+raiz)/2*a
    x2=(-b-raiz)/2*a
    print("solución 1:",x1)
    print("solución 2:",x2)
