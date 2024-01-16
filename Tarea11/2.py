nombres=[]
notas=[]
for x in range(10):
    nombre=input("introduce un nombre:")
    nombres.append(nombre)
    nota=int(input("introduce un nota"))
    notas.append(nota)
print("Alumnos aprobados:")
for x in range(10):
    if notas[x]>=5:
        print(nombres[x],"",notas[x])
print("Alumnos suspensos:")
for x in range(10):
    if notas[x]<5:
        print(nombres[x],"",notas[x])

