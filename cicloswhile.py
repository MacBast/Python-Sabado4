observador=100

print("**MENU**")
print("0.SALIR")
print("1.SALUDAR")
print("2.DESPEDIR")

while(observador !=0):
    observador=int(input("Digite una opcion  (▀̿̿Ĺ̯̿▀̿ ̿): "))
    if(observador==0):
        break
    elif(observador==1):
        print("Hola lindo ( ͡° ͜ʖ ͡°)  ٩(♡ε♡ )۶")
    elif(observador==2):
        print("Chao pichurria 凸-_-凸")
    else:
        print("Digite los numeros del menu pendejo (-_-;)")
else:
    print("termine")