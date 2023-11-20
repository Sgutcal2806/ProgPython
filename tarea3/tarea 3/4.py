num1=int(input("introduce primer número"))
num2=int(input("introduce segundo  número"))
num3=int(input("introduce tercer número"))
if num1>num2 and num1>num3:
    print("el mayor es",num1)
else:
        if num2>num3:
            print("el mayor es",num2)
        else:
            print("el mayor es",num3)

if num1<num2 and num1<num3:
    print("el menor es",num1)
else:
        if num2<num3:
            print("el menor es",num2)
        else:
            print("el menor es",num3)

