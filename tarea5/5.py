n=int(input("Puntos en el plano?"))
tercer=0
primer=0
segundo=0
cuarto=0
for x in range(n):
    x=float(input("cordenada x:"))
    y=float(input("coordenada y:"))
    
    if x>0 and y>0:
        print("Primer cuadrante")
        primer=primer+1
    
    else:
        if x>0 and y>0:
             print("Segundo cuadrante")
             segundo=segundo+1
        else:
            if x<0 and y>0:
                print("tercer cuadrante")
                tercer=tercer+1
            else:
                print("cuarto cuadrante")
                cuarto=cuarto+1
            
print("Primer cuadrante:",primer)       
print("Segundo cuadrante:",segundo)
print("Tercer cuadrante:",tercer)
print("Cuarto cuadrante:",cuarto)
