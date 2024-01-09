lista=[]
for x in range(5):
    valor=float(input("Introduce una altura:"))
    lista.append(valor)
suma=0
for x in range(5):
    suma=suma+lista[x]
promedio=suma/5
print("La altura mediaes",promedio)
supera=0
nosupera=0
for x in range(5):
    if lista[x]>promedio:
        supera=supera+1
print("Personas superior a la media",supera)
print("Personas inferior a la media:",nosupera)
print()
