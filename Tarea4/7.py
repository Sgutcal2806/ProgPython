n=int(input("cuantos números?"))
x=1
pares=0
impares=0
while x<=n:
    valor=int(input("introduce un valor"))
    x=x+1
    if valor%2==0:
        pares=pares+1
    else:
        impares=impares+1
print("Pares:",pares)
print("Impares:",impares)


