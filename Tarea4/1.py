aprobados=0
suspensos=0
x=1
while x<=10:
    nota=int(input("ingrese una nota"))
    x=x+1
    if nota>=5:
        aprobados=aprobados+1
    else:
        suspensos=suspensos+1
print("aprobados:",aprobados)
print("suspensos:",suspensos) 


    
