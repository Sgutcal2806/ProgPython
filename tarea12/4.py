def mayor(n1,n2):
    if n1>n2:
        return n1
    else:
        return n2





n1=int(input("introduce el valor1:"))
n2=int(input("introduce el valor2:"))
n3=int(input("introduce el valor3:"))
n4=int(input("introduce el valor4:"))
print("El mayor de los 4 valores es:",mayor(mayor(n1,n2),mayor(n3,n4)))
