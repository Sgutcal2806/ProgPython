cordx=int(input("introduce una cordenada x:"))
cordy=int(input("introduce una cordenada y:"))
if cordx>0 and cordy>0:
    print("Está en el primer cuadrante")
else:
    if   cordx<0 and cordy<0:
        print("Está en el cuarto cuadrante")
    else:
        if   cordx<0 and cordy>0:
            print("Está en el segundo cuadrante")
        else:
            print("Está en el tercer cuadrante")
        
        
