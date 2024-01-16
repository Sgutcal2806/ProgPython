nombres=[]
sueldos=[]
for x in range(5):
    nombre=input("introduce un nombre:")
    nombres.append(nombre)
    valor=int(input("introduce un sueldo"))
    sueldos.append(valor)
mayor=0
menor=9999999
posMayor=0
posMenor=0
for x in range(5):
    if sueldos[x]>mayor:
        mayor=sueldos[x]
        posMayor=x
    if sueldos[x]<menor:
        menor=sueldos[x]
        posMenor=x
print("El sueldo mayor es ",mayor,"y pertenecea",nombres[posMayor])
print("El sueldo menor es ",menor,"y pertenecea",nombres[posMenor])
    
