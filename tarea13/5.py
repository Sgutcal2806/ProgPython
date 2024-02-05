#crear una lista de la forma [("hola")],("mundo",5)...

def cargar_palabras():
    palabras=[]
    longitud=1;
    while longitud>0:
        palabra=input("introduce una palabra:")
        longitud=len(palabra)
        palabras.append((palabra,longitud))
    return palabras
#Visualizar palabra de más de 5 caracteres
def visualizar_palabras(palabras):
    for palabra in palabras:
        totalVotos=0
        if palabra[1]>5:
            print(palabra[0])

#programa principal
palabras=cargar_palabras()
visualizar_palabras(palabras)
