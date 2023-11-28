positivos=0
negativos=0
multiplo15=0
sumapar=0
for x in range(10):
    n=int(input("Ingrese un número:"))
    if n>0:
        
        positivos=positivos+1
    else:
        negativos=negativos+1
    if n%15==0:
        multiplo15=multiplo15+1
    if n%2==0:
        sumapar=sumapar+n
print("Positivos:",positivos)
print("Negativos:",negativos)
print("Multiplos de 15:",multiplo15)
print("Suma de los pares:",sumaPares)
