suma=0
producto=1
for x in range(10):
    numero=int(input("Número:"))
    if x<5:
        suma=suma+numero
    else:
        producto=producto*numero
print("La suma de los 5 primeros es :",suma)
print("El producto de los 5 últimos es :",producto) 
    
