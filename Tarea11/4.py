alumnos=[]
notas=[]
for x in range(4):
    nombre=input("introduce un alumno:")
    alumnos.append(nombre)
    nota=int(input("introduce una nota:"))
    notas.append(nota)
muybueno=0
for x in range(4):
    if notas[x]<4:
        print(alumnos[x],"Insuficiente")
    else:
        if notas[x]<=7:
            print(alumnos[x],"Bueno")
        else:
            muybueno=muybueno+1
            print(alumnos[x],"Muy bueno")
print("Alumnos muy bueno:",muybueno)
