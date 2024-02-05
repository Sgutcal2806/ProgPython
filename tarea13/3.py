#Leer una lista de 5 empleados nombre y tres sueldos
def cargar_empleados():
    empleados=[]
    
    for x in range(5):
        nombre=input("Cargar un nombre:")
        sueldo1=int(input("cargar un sueldo"))
        sueldo2=int(input("cargar otro sueldo"))
        sueldo3=int(input("cargar otro sueldo"))
        empleado=[]

        empleado.append(nombre)
        empleado.append((sueldo1,sueldo2,sueldo3))
        empleado.append(empleado)
    return empleados
#visualizar el mayor sueldo de dos empleados
def visualizar(empleados):
    
    for empleado in empleados:
        total=0
        for sueldo in empleado[1]:
            total=total+sueldo
        
        print(empleado[0],"tiene un sueldo trimestral de",total)
    
#visualizar empleados con un monto trimestral mayor a 10000
def visualizarSuperior(empleados):
    print("los empleados con un monto trimestral superior a 10000 son:")
    for empleado in empleados:
        total=0
        for sueldo in empleado[1]:
            total=total+sueldo
        if total>10000:
            print(empleado[0],"tiene un sueldo trimestral de",total)      
#programa principal
empleados=cargar_empleados()
visualizar(empleados)
visualizarSuperior(empleados)
        
