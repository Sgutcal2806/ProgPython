suma=0
n=int(input("¿cuantas alturas vas a ingresar"))
x=1
while x<=n:
    altura=float(input("introduce una altura:"))
    x=x+1
    suma=suma+altura
media=suma/n
print("La altura media es",media)
