oración=input("Introduce una oración:")
palabras=1
longitud=len(oración)
x=0
while x<longitud:
    if(oración[x]==" "):
        palabras=palabras+1
    x=x+1
print("Palabras:",palabras)
