num1=int(input("introduce una nota"))

if num1>5:
    print("El examen está aprobado con un:",num1)
else:
    print("El examen está suspenso con un:",num1)

    if num1>=6:
        print("Tienes un bien")
    else:
        if num1>=7:
            print("Tienes un notable",num1)
        else:
            if num1>=9:
                print("Tienes un sobresaliente",num1)
                    
                    
